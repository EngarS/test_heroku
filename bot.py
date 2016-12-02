import config
import telebot
from flask import Flask, request

bot = telebot.TeleBot(config.token)

#server = Flask(__name__)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

bot.polling(none_stop=True, interval=0, timeout=3)

'''
@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=config.domain + config.token)
    return "CONNECTED", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
'''
