import os
import requests
from bs4 import BeautifulSoup
import json

def fetch_page_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_data_from_page(page_data):
    soup = BeautifulSoup(page_data, 'html.parser')
    table = soup.find('table')
    
    if not table:
        return None

    headers = [header.text.strip() for header in table.find_all('th')]
    rows = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            data = [col.text.strip() for col in cols]
            rows.append(data)
    
    return headers, rows

def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None
