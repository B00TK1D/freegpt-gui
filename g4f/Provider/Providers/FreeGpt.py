import requests
import os
import time
import json
from ...typing import sha256, Dict, get_type_hints

url = 'https://api.github.com'
model = ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k',
         'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0613', 'gpt-4', 'gpt-4-1106-preview']
supports_stream = False
needs_auth = False

token = None

token_age = 0

def setup():
    resp = requests.post('https://github.com/login/device/code', headers={
            'accept': 'application/json',
            'editor-version': 'Neovim/0.6.1',
            'editor-plugin-version': 'copilot.vim/1.16.0',
            'content-type': 'application/json',
            'user-agent': 'GithubCopilot/1.155.0',
            'accept-encoding': 'gzip,deflate,br'
        }, data='{"client_id":"Iv1.b507a08c87ecfe98","scope":"read:user"}')


    # Parse the response json, isolating the device_code, user_code, and verification_uri
    resp_json = resp.json()
    device_code = resp_json.get('device_code')
    user_code = resp_json.get('user_code')
    verification_uri = resp_json.get('verification_uri')

    # Print the user code and verification uri
    print(f'Please visit {verification_uri} and enter code {user_code} to authenticate.')


    while True:
        time.sleep(5)
        resp = requests.post('https://github.com/login/oauth/access_token', headers={
            'accept': 'application/json',
            'editor-version': 'Neovim/0.6.1',
            'editor-plugin-version': 'copilot.vim/1.16.0',
            'content-type': 'application/json',
            'user-agent': 'GithubCopilot/1.155.0',
            'accept-encoding': 'gzip,deflate,br'
            }, data=f'{{"client_id":"Iv1.b507a08c87ecfe98","device_code":"{device_code}","grant_type":"urn:ietf:params:oauth:grant-type:device_code"}}')

        # Parse the response json, isolating the access_token
        resp_json = resp.json()
        access_token = resp_json.get('access_token')

        if access_token:
            break

    # Save the access token to a file
    with open('.copilot_token', 'w') as f:
        f.write(access_token)

    print('Authentication success!')

def get_token():
    global token
        # Check if the .copilot_token file exists
    while True:
        try:
            with open('.copilot_token', 'r') as f:
                access_token = f.read()
                break
        except FileNotFoundError:
            setup()
    # Get a session with the access token
    resp = requests.get('https://api.github.com/copilot_internal/v2/token', headers={
        'authorization': f'token {access_token}',
        'editor-version': 'Neovim/0.6.1',
        'editor-plugin-version': 'copilot.vim/1.16.0',
        'user-agent': 'GithubCopilot/1.155.0'
    })

    # Parse the response json, isolating the token
    resp_json = resp.json()
    token = resp_json.get('token')
    token_age = time.time()


def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    global token
    if not token or time.time() - token_age > 600:
        get_token()
    headers = {
        'authorization': f'Bearer {token}',
        'Editor-Version': 'vscode/1.80.1',
    }

    json_data = {
        'intent': False,
        'model': model,
        'temperature': 0,
        'top_p': 1,
        'n': 1,
        'stream': False,
        'messages': messages
    }

    response = requests.post('https://api.githubcopilot.com/chat/completions',
                             headers=headers, json=json_data)

    # for chunk in response.iter_lines():
    #     print("Response:", chunk)
    #     if b'content' in chunk:
    #         data = json.loads(chunk.decode().split('data: ')[1])
    #         yield (data['choices'][0]['delta']['content'])
    try:
        return response.json()['choices'][0]['message']['content']
    except:
        return "Error"


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
