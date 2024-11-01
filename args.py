import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(description='Create a Simple One Page')
    parser.add_argument('-g', '--generate-dork', type=str, help='Generate a dork for a search engine. \nExample: "site:example.com"')
    parser.add_argument('-s', '--search', type=str, help='Search for a dork in a search engine. \nExample: "site:example.com"')
    return parser.parse_args()
