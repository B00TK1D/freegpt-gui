from g4f import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str

    class gpt_35_turbo:
        name: str = 'gpt-3.5-turbo'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_35_turbo_0613:
        name: str = 'gpt-3.5-turbo-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_35_turbo_0301:
        name: str = 'gpt-3.5-turbo-0301'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_35_turbo_16k_0613:
        name: str = 'gpt-3.5-turbo-16k-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_35_turbo_16k:
        name: str = 'gpt-3.5-turbo-16k'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_4_dev:
        name: str = 'gpt-4-for-dev'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_4:
        name: str = 'gpt-4'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_4_0613:
        name: str = 'gpt-4-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt

    class gpt_4_1106_preview:
        name: str = 'gpt-4-1106-preview'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.FreeGpt


class ModelUtils:
    convert: dict = {
        'gpt-3.5-turbo': Model.gpt_35_turbo,
        'gpt-3.5-turbo-0613': Model.gpt_35_turbo_0613,
        'gpt-3.5-turbo-0301': Model.gpt_35_turbo_0301,
        'gpt-4': Model.gpt_4,
        'gpt-4-0613': Model.gpt_4_0613,
        'gpt-4-for-dev': Model.gpt_4_dev,
        'gpt-4-1106-preview': Model.gpt_4_1106_preview,
        'gpt-3.5-turbo-16k': Model.gpt_35_turbo_16k,
        'gpt-3.5-turbo-16k-0613': Model.gpt_35_turbo_16k_0613,
    }
