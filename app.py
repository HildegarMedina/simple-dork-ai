import sys
from rich.console import Console
from rich.panel import Panel

from config.config import PANEL_DESCRIPTION, PANEL_TITLE, PANEL_SUBTITLE
from args import parser_arguments
from modules.chatgpt import ChatGPT
from services.configuration import Configuration
from services.dork_generator import DorkGenerator

def main():
    args = parser_arguments()

    console = Console()

    if len(sys.argv) == 1:
        console.print(Panel(PANEL_DESCRIPTION, title=PANEL_TITLE, subtitle=PANEL_SUBTITLE))
        sys.exit(1)

    if args.generate_dork:
        configuration = Configuration(console)
        configuration.verify_api_key_openai()

        chatgpt = ChatGPT(console, model=args.model)
        dork_generator = DorkGenerator(chatgpt)
        dork = dork_generator.generate(args.generate_dork)
        console.print(f'[bold green]{dork}[/bold green]')

    if args.search:
        pass

if __name__ == "__main__":
    main()