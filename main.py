import telebot
import requests
from time import sleep

chave_bot = "chave_do_bot"
chave_API = "chave_da_api"
grupo = "codigo_do_grupo"

bot = telebot.TeleBot(chave_bot)

def responder_tempo():
    cidade = "Lauro de freitas"                                 
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()

    descricao = requisicao_dic["weather"][0]["description"]
    temperatura = requisicao_dic["main"]["temp"] - 273.15

    if temperatura <= 27:
        tempo = f"Tempo: ☁️ {descricao}. ☁️\nTemperatura 🥶: {temperatura:.2f}°C 🥶"
    else:
        tempo = f"Tempo: ☁️ {descricao}. ☁️\nTemperatura ☀️: {temperatura:.2f}°C ☀️"

    bot.send_message(grupo, tempo)

while True:
    responder_tempo()
    sleep(10800)
