import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8812821991: AAGarLhuwa2mZQClFv64INwIBXsIqC_ofE4"


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(
        KeyboardButton("📝 Test ishlash"),
        KeyboardButton("🎯 Real imtihon")
    )
    markup.add(
        KeyboardButton("🚦 Yo'l belgilari"),
        KeyboardButton("📖 YHQ qoidalari")
    )
    markup.add(
        KeyboardButton("🏆 Reyting"),
        KeyboardButton("📊 Natijalarim")
    )
    markup.add(
        KeyboardButton("📸 Instagram")
    )

    bot.send_message(
        message.chat.id,
        "🚗 Assalomu alaykum!\n\n"
        "PRAVA TEST UZ botiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang 👇",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "📝 Test ishlash":
        bot.send_message(message.chat.id, "📝 Testlar bo'limi tez orada qo'shiladi.")
    elif message.text == "🎯 Real imtihon":
        bot.send_message(message.chat.id, "🎯 Real imtihon tez orada qo'shiladi.")
    elif message.text == "🚦 Yo'l belgilari":
        bot.send_message(message.chat.id, "🚦 Yo'l belgilari bo'limi tez orada qo'shiladi.")
    elif message.text == "📖 YHQ qoidalari":
        bot.send_message(message.chat.id, "📖 YHQ qoidalari bo'limi tez orada qo'shiladi.")
    elif message.text == "🏆 Reyting":
        bot.send_message(message.chat.id, "🏆 Reyting tez orada qo'shiladi.")
    elif message.text == "📊 Natijalarim":
        bot.send_message(message.chat.id, "📊 Natijalar bo'limi tez orada qo'shiladi.")
    elif message.text == "📸 Instagram":
        bot.send_message(
            message.chat.id,
            "Instagram: https://www.instagram.com/prava.test_uz"
        )

print("Bot ishga tushdi...")

bot.infinity_polling()
