import sys
from dotenv import load_dotenv, set_key, get_key
from config.config import COLOR_WARNING, COLOR_SUCCESS

class Configuration:
    def __init__(self, console):
        self.console = console
        load_dotenv()

    def verify_api_key_openai(self):
        if not get_key('.env', 'OPENAI_API_KEY'):
            self.console.print(f"\n[italic {COLOR_WARNING}]Please set the OPENAI_API_KEY environment variable[/italic {COLOR_WARNING}]\n")
            api_key = ""
            while not api_key:
                api_key = input('Enter your OpenAI API key: ')
            set_key('.env', 'OPENAI_API_KEY', api_key)
            self.console.print(f'\n[{COLOR_SUCCESS}]API key set successfully[/{COLOR_SUCCESS}]\n')
            sys.exit(1)
