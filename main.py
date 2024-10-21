# main.py
import pandas as pd
from funcoes_selenium import iniciar_navegador, fazer_lancamento_diario
import os

def main(url):
    # Carregar os dados do CSV em um DataFrame
    df = pd.read_csv('data/in/Dados Diário - Página1.csv')

    # Iniciar o navegador
    driver = iniciar_navegador()

    # Fazer os lançamentos diários
    fazer_lancamento_diario(driver, url, df)

    # Fechar o navegador
    driver.quit()

if __name__ == '__main__':
    url = os.getenv('URL_SITE')
    main(url)
