from playwright.sync_api import sync_playwright
import pandas as pd

def extrair_dados_challenge_place(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("table", timeout=10000)
        html = page.content()
        browser.close()
    dfs = pd.read_html(html)
    if not dfs:
        raise ValueError("Nenhuma tabela encontrada.")
    return dfs[0]