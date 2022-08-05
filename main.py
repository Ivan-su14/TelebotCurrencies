import telebot
import requests
from bs4 import BeautifulSoup as b


perevod = {'доллар':'dollar','евро':'evro','российский рубль': 'rossiyskiy-rubl',
           'usd':'dollar','eur':'evro','rub': 'rossiyskiy-rubl'}

bot = telebot.TeleBot('5466408435:AAGn6SMxmymtOnv7sAkarSUasEC2SDhrkNw')

@bot.message_handler()

def create_url(message):
    text = message.text.lower()
    if message.text == "/help":
        bot.send_message(message.chat.id,"Напиши один из курсов валют: usd -доллар США, eur - Евро, rub - Российский рубль")
    if text in perevod:
        url = f'https://select.by/kursy-valyut/natsbank-rb/{str(perevod[text])}/'
        r = requests.get(url)
        soup = b(r.text, 'html.parser')
        currency = soup.find('span', class_ ='font-size-3rem font-weight-500')
        if message.text == 'rub':
            bot.send_message(message.chat.id, f'{currency.next_element.text}, за 100 рос. руб.')
        else:
            bot.send_message(message.chat.id, f'{currency.next_element.text}')
    elif message.text != "/help":
        bot.send_message(message.from_user.id, 'Я Вас не понимаю. Напишите /help')
bot.polling(none_stop=True)


