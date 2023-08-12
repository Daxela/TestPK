import time
import telebot
from factorial import processing

bot = telebot.TeleBot('6439454068:AAENufLi3RLwaCFtQurVCd4CwLT2sB7V4iE')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Здравствуйте, я умею вычислить факториал числа, для этого введите число. Напоминаю, факториал отрицательного числа не существует.")
    elif message.text.isdigit():
        bot.send_message(message.from_user.id, processing(int(message.text)))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напишите /help.")


print("Bot listening")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
