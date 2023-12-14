# Importar as bibliotecas
from selenium import webdriver
import time

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os


# Navegar até o whatsapp web
driver = webdriver.Chrome()  # (ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
# time.sleep(30)
# Esperar a tela do whatsapp carregar
while (
    len(driver.find_elements(By.ID, "side")) < 1
):  # elemento que diz que a tela carregou -> finds me tras uma lista com todos elementos com ID igual a side e se ela for vazia significa que não existe elemento ainda    time.sleep(2)
    time.sleep(2)
time.sleep(15)  # garatnia

# whatssapp carregou
tabela = pd.read_excel("mantenedorcs.xlsx")
# print(tabela[["nome", "telefone", "valor"]])


for linha in tabela.index:
    # enviar menssagem pessoa
    # nome = tabela.loc[linha, coluna]
    nome = tabela.loc[linha, "nome"]
    telefone = tabela.loc[linha, "telefone"]
    valor = tabela.loc[linha, "valor"]

    texto1 = "Olá, *Fulano!* Estamos muito felizes por você ter decidido ser parte do que Deus está fazendo em nossa cidade através do Centro Social da Lagoinha Salvador."
    texto2 = f"*Aqui está a chave pix para enviar a sua oferta deste mês, no valor de R${valor:.2f}:* centrosocial@lagoinhabahia.com.br"
    texto3 = "Que Jesus continue abençoando sua vida!!"
    texto4 = "O Centro Social agradece pela sua contribuição."

    texto = texto1.replace("Fulano", nome)

    # texto = urllib.parse.quote(texto)
    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}"  # &text={texto}"

    driver.get(link)
    # esperar a tela do whatsapp carregar
    while (
        len(driver.find_elements(By.ID, "side")) < 1
    ):  # elemento que diz que a tela carregou -> finds me tras uma lista com todos elementos com ID igual a side e se ela for vazia significa que não existe elemento ainda    time.sleep(2)
        time.sleep(10)
    time.sleep(10)  # garatnia

    # verificar se número existe
    # if len(driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
    # enviar a mensagem
    #   time.sleep(5)
    # if arquivo != 'N':
    # caminho_completo = os.path.abspath('cs.jpeg')
    # driver.find_element(By.XPATH, '//span[contains(@data-testid,"clip")]').click()
    # driver.find_element(By.XPATH, '//input[contains(@accept,"image/*,video/mp4,video/3gpp,video/quicktime")]').send_keys(caminho_completo)
    # time.sleep(10)
    time.sleep(10)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(texto)
    time.sleep(10)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(Keys.SHIFT + Keys.ENTER)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(Keys.SHIFT + Keys.ENTER)
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(texto2)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(Keys.SHIFT + Keys.ENTER)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(Keys.SHIFT + Keys.ENTER)
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(texto3)
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(Keys.SHIFT + Keys.ENTER)
    time.sleep(5)
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p',
    ).send_keys(texto4)

    time.sleep(3)
    caminho_completo = os.path.abspath("CSL_Lagoinha_ret.png")
    driver.find_element(
        By.XPATH,
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div/div/span',
    ).click()
    driver.find_element(
        By.XPATH,
        '//input[contains(@accept,"image/*,video/mp4,video/3gpp,video/quicktime")]',
    ).send_keys(caminho_completo)

    # campo_mensagem[1]
    time.sleep(3)
    # campo_mensagem.send_keys(texto)
    driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span',
    ).click()
    time.sleep(5)
