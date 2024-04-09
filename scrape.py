import datetime
import requests
import os

from requests_html import HTML

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(BASE_DIR, 'Storage')

# def add_url_to_file(url: str, file: str) -> None:
#     with requests.get(url, stream=True) as req:
#         req.raise_for_status()
#         with open(file, 'w', encoding='utf-8') as f:
#             f.write(req.text)

def url_to_txt(url, filename="world.html", save=False):
    req = requests.get(url)
    if req.status_code == 200:
        html_text = req.text
        if save:
            with open(f"{STORAGE_FILE}/world-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return ""


if __name__=='__main__':
    os.makedirs(STORAGE_FILE, exist_ok=True)
    url = "https://www.boxofficemojo.com/year/world/"

    now = datetime.datetime.now()
    year = now.year

    url_to_txt(url)    