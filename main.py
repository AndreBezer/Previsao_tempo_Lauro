import telebot
import requests
from time import sleep

chave_bot = "7770862620:AAEKKvTTNkFHK4GG21ZxUK-3zYbpCrhQXZg"
chave_API = "3854106ac8f16b66d9226ff557c5f947"
dono = "6234485725"

bot = telebot.TeleBot(chave_bot)

def mensagem():
    sleep(10800)

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

    bot.send_message(dono, tempo)

while True:
    mensagem()
