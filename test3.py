import telebot
import os
from flask import Flask, request
from telebot import types

TOKEN = "555741179:AAFcnjKeq5n1u7Y2OQxApfypR7353lH-zSE"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.from_user.id, "Добро пожаловать")
    bot.register_next_step_handler(sent, hello)
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row("🍽Заказ еды🍽")
    markup.row("🚕Заказ такси🚕")
    markup.row("😂Развлечения😂")
    markup.row("💲Деньги💲")
    markup.row("🔍Пробив информации🔍")
    markup.row("⛱Путешествия✈")
    markup.row("✉sms/mail📧")
    markup.row("⌚Товары🖲")
    markup.row("Клуб профессионалов")
    markup.row("Документы")
    markup.row("Мобильная связь")
    markup.row("Гарант сервис")
    markup.row("Авто")
    markup.row("Музыка")
    markup.row("Заработок в сети")
    markup.row("Консультации специалистов")
    markup.row("Аренда жилья")
    markup.row("Обратная связь")
    bot.send_message(message.from_user.id,"Введите Ваше имя", reply_markup=markup)


def hello(message):
    bot.send_message(message.chat.id, 'Приветствую, {name}. Пользовательское соглашение между Ботом Easylife_bot и пользователем {name}\n\n'
'1. Easylife_bot - (далее бот) является информационной площадкой.\n'
'2. Бот, владельцы, и администраторы бота не несут никакой ответственности за ваши действия по использованию сервисов, а также за сделки финансового и иного характеров.\n'
'3. Сервисы вне бота не имеют никакого отношения к боту, лица, выдающие себя за сервисы, администраторов, владельцев бота, могут таковыми не являются.\n'
'*С администраторами и модераторами Вы можете связаться через кнопку обратной связи в боте.\n'
'4. С актуальным списком сервисов вы можете ознакомиться в соответствующем разделе бота.\n'
'**Администрация бота НЕ участвует в решение спорных ситуаций, со сторонними сервисами (сервисами вне бота).\n'
'5. За сделки с селлерами бота ответственность лежит полностью на Вас. Бот, администрация, модераторы не несут ответственности за ваши действия.\n'
'6. При возникновении спорных ситуаций необходимо решать напрямую с сервисом, при невозможности решения ситуации рекомендуем писать через кнопку обратной связи в боте, но Администрация не гарантирует решение ее в Вашу пользу.\n'
'7. С правилами работы сервисов, Вы можете ознакомится, попросив "правила использования сервисов" у любого из представленных сервисов.\n'
'8. Вы можете обезопасить свою сделку используя Гарант-сервис.\n'
'9. Используя Бот, вы даете свое согласие с данными правилами.\n'
'10. Данное соглашение может быть изменено в одностороннем порядке и без уведомления.\n\n'
'Выбери категорию.'.format(name=message.text))


@bot.message_handler(content_types=["text"])
def category(message):
    if message.text == "🍽Заказ еды🍽":
            bot.send_message(message.from_user.id,"cам")

    elif message.text == "🚕Заказ такси🚕":
            bot.send_message(message.from_user.id, "йцукен")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://app1301.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__": server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
bot.polling()

