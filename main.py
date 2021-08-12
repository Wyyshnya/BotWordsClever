#!usr/bin/env python3

from random import randint, choice
from requests import get
from bs4 import BeautifulSoup
from threading import Timer
from telebot import TeleBot

TOKEN = '1938158787:AAGdf8NLw8upcmyw5NjTa2QqCj58TS5Laqw'
BOT = TeleBot(TOKEN)


def send_word():
    Timer(86400.0, send_word).start()
    BOT.send_message(586928099, get_random_word())


def get_random_word():
    random_page_number = str(randint(1, 34))
    webpage = get('https://app.memrise.com/course/861896/umnyi-slovar-1000-slov/' + random_page_number).text
    tags = BeautifulSoup(webpage, 'html.parser').find_all('div', class_='col_a col text')
    definitions = BeautifulSoup(webpage, 'html.parser').find_all('div', class_='col_b col text')
    words = []
    defins = []
    for tag in tags:
        tag_text = tag.get_text()
        words.append(tag_text)

    for definition in definitions:
        defin_text = definition.get_text()
        defins.append(defin_text)

    word_num = words.index(choice(words[:]))
    word = words[word_num]
    defin = defins[word_num]
    message = word + ' - ' + defin

    return message


if __name__ == '__main__':
    send_word()
