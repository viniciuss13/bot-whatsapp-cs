# Importar bibliotecas
import pywhatkit
import keyboard
import time
from datetime import datetime
import urllib
import pandas as pd
import numpy as np

# Definir para quais contatos envias msgs
tabela = pd.read_excel("mantenedores.xlsx")
print(tabela[["nome", "mensagem", "arquivo", "telefone"]])


menssagem = []
contatos = []

for linha in tabela.index:

    #enviar menssagem pessoa
    # nome = tabela.loc[linha, coluna]
    # nome = tabela.loc[linha, "nome"]
    # mensagem = tabela.loc[linha, "mensagem"]
    # arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    contatos = np.append(contatos, str(telefone))
    # contatos = np.append(contatos, telefone)
    
#     texto = mensagem.replace("Fulano", nome)
#     texto = urllib.parse.quote(texto)
#     #enviar a mensagem

print(contatos)
# print(menssagem)

# Definir intervalo de envio
while len(contatos) >= 1 :
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Olá, sou um bot feito pelo seu namorado. Passando pra dizer que ele te ama. Bjs!', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('command + w')
# Testar