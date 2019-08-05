import telebot

bot = telebot.telebot('908462451:AAHhAbKFAN1vOHA3SB_ph1xnXsCe_4NdeI8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Bem vindo ao BOT ! Aqui é o lugar perfeito para voce se ferrar')

bot.polling()
