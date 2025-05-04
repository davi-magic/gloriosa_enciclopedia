import pandas as pd
import re
from io import StringIO

def importar_tabela(texto):
    linhas = texto.strip().splitlines()
    linhas_tabela = [linha for linha in linhas if re.search(r'\S+\s{2,}\S+', linha)]

    if not linhas_tabela:
        raise ValueError("Não foi possível identificar linhas de tabela válidas.")

    tabela_bruta = "\n".join(linhas_tabela)
    tabela_formatada = re.sub(r'\s{2,}', '\t', tabela_bruta)

    df = pd.read_csv(StringIO(tabela_formatada), sep='\t')
    return df
