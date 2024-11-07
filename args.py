import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(description='Simple Dork AI')
    parser.add_argument('-g', '--generate-dork', type=str, help='Generate a dork for a search engine. \nExample: "Create a dork for searching pdf files"')
    parser.add_argument('-d', '--dork', type=str, help='Search for a dork in a search engine. \nExample: "site:example.com"')
    parser.add_argument('-m', '--model', type=str, help='Model to use for the chatbot. \nExample: "gpt-3.5-turbo"', default='gpt-4o-mini')
    parser.add_argument('-p', '--pages', type=int, help='Number of pages to search. \nExample: 3', default=1)
    return parser.parse_args()
