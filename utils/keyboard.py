import telebot

def default_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(text="🇺🇸 English")
    button2 = telebot.types.KeyboardButton(text="🇰🇿 Қазақ")
    button3 = telebot.types.KeyboardButton(text="🇷🇺 Русский")
    keyboard.add(button1, button2, button3)


    return keyboard