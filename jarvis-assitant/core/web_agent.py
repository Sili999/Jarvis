import requests
from bs4 import BeautifulSoup

def fetch_web(query: str) -> str:
    res = requests.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query", "prop": "extracts", "exintro": "", "format": "json", "titles": query
    })
    data = res.json()
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        return page.get("extract", "")
    return "Keine Informationen gefunden."
