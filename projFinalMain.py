from gptSetup import getAnswerFromGpt
from OLEDSSD1306 import displayText,display
from speechRecog import recognizeSpeech
import re
from unidecode import unidecode
from gpiozero import LED,Button
from time import sleep

botao = Button(20)
led_verde = LED(16)   
led_vermelho = LED(21)
def limpar_texto(texto):
    # Remove acentos
    texto_sem_acento = unidecode(texto)
    
    # Remove caracteres especiais usando regex
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acento)
    
    return texto_limpo

while True:
    displayText("faca uma  afirmacao ou pergunta com resposta direta")
    pergunta = limpar_texto(recognizeSpeech())
    print(pergunta)
    if pergunta == "Nao entendi":
        displayText("Nao Entendi a pergunta")
    else:
        resposta = limpar_texto(getAnswerFromGpt(pergunta))
        if ("Sim" or "sim") in resposta:
            led_verde.on()
        if ("Nao" or "nao") in resposta:
            led_vermelho.on()

        displayText(resposta)
    while not(botao.is_pressed):
        print("fica por aqui")
        sleep(0.5)