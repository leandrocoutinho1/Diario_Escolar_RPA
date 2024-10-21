import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os




# funcoes_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def iniciar_navegador():
    # Inicie o navegador e retorne o objeto do driver
    driver = webdriver.Chrome()  # ou o driver que você está usando
    return driver

def abrir_site(driver, url):
    # Exemplo de como preencher o formulário
        driver.get(url)
    
def fazer_login(driver):
    login = os.getenv('login')
    senha = os.getenv('senha')

    digitar(driver, '//*[@id="usuario"]', login)
    digitar(driver, '//*[@id="senha"]', senha)
    sleep(5)
    clicar(driver, '//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr/td/button')

def digitar(driver, xpath, texto):
    driver.find_element('xpath', xpath).send_keys(texto)

def clicar(driver, xpath):
    driver.find_element('xpath', xpath).click()

def fazer_lancamento_diario(driver, url, dados):
    abrir_site(driver, url)

    sleep(5)

    fazer_login(driver)

    sleep(15)


    # # Aqui você irá fazer o lançamento diário usando os dados do DataFrame
    # for index, row in dados.iterrows():
        
        
    #     # Supondo que você tenha um campo de texto com um ID específico
    #     campo_diario = driver.find_element(By.ID, 'id_do_campo')
    #     campo_diario.send_keys(row['coluna_que_tem_o_dado'])

    #     # Adicione mais campos conforme necessário
    #     # ...

    #     # Enviar o formulário (supondo que haja um botão de envio)
    #     botao_enviar = driver.find_element(By.ID, 'id_do_botao_enviar')
    #     botao_enviar.click()
