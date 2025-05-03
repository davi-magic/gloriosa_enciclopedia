import re

def validate_url(url):
    url_pattern = re.compile(r'http(s)?://(www\.)?challenge\.place/c/\w+/statistics')
    return bool(url_pattern.match(url))

def validate_data(headers, rows):
    if not headers or not rows:
        return False

    required_columns = ['Jogador', 'Gols', 'Assistências', 'Participações']
    if any(col not in headers for col in required_columns):
        return False

    return True
