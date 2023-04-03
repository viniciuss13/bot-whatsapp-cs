import pywhatkit
import pandas as pd
import keyboard
import time
from datetime import datetime


# Definir para quais contatos envias msgs
contatos = ["+559940675"]

# Definir intervalo de envio
while len(contatos) >= 1 :
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Olá', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(10)
    # keyboard.press_and_release('command + w')

# Testar
# tabela = pd.read_excel()
