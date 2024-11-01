import sys
from rich.console import Console
from rich.panel import Panel
from config.config import PANEL_DESCRIPTION, PANEL_TITLE, PANEL_SUBTITLE
from modules.chatgpt import ChatGPT
from args import parser_arguments
from services.configuration import Configuration

def main():
    console = Console()
    if len(sys.argv) == 1:
        console.print(Panel(PANEL_DESCRIPTION, title=PANEL_TITLE, subtitle=PANEL_SUBTITLE))
        sys.exit(1)

    args = parser_arguments()

    if args.generate_dork:
        configuration = Configuration(console)
        configuration.verify_api_key_openai()

    if args.search:
        # chatgpt = ChatGPT(console, model=args.model)
        pass

if __name__ == "__main__":
    main()