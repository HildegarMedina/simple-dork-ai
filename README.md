# Simple Dork AI

Simple Dork AI
 is a tool designed to generate dorks and search for information using those dorks with Selenium. It automates the process of crafting search queries (dorks) to find specific information on the web, making it easier for users to gather data efficiently.

## Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

## Usage

![Python Main](https://i.postimg.cc/zB352GWx/Screenshot-from-2024-11-07-14-51-07.png)
![Python Main](https://i.postimg.cc/nL3p1Dss/Screenshot-from-2024-11-07-14-53-40.png)
![Python Main](https://i.postimg.cc/xdf9HRdD/Screenshot-from-2024-11-07-14-54-10.png)

## Example

Generate dork:
```
python app.py -g "I want to search information about Hildegar Medina, just social networks"
```

Search information with dork:
```
python app.py -d '"Hildegar Medina" site:facebook.com OR site:twitter.com OR site:instagram.com OR 
site:linkedin.com'
```

