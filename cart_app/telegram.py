import telebot

bot = telebot.TeleBot("6176361926:AAGLuN18PYJ7tadPiSIZYS-_HRT6GwGk-cw")
def send_message_tg(chat_id, message_text):
    bot.send_message(chat_id, message_text)