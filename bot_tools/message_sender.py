import telebot


def language_selection_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(
        telebot.types.KeyboardButton(text="🇺🇸 English"),
        telebot.types.KeyboardButton(text="🇪🇸 España"),
        telebot.types.KeyboardButton(text="🇰🇿 Қазақ"),
        telebot.types.KeyboardButton(text="🇷🇺 Русский")
    )


    return keyboard



def admin_keyboard():
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton("Open admin panel", url="http://127.0.0.1:5000/")
    markup.add(button)

    return markup


def send_message_with_keyboard(bot, message, answer):
    bot.send_message(message.chat.id, answer, parse_mode='HTML', reply_markup=language_selection_keyboard())


def send_message_with_admin_button(bot, message, answer):
    bot.send_message(message.chat.id, answer, parse_mode='HTML', reply_markup=admin_keyboard())



def send_message_without_keyboard(bot, message, answer):
    bot.send_message(message.chat.id, answer, parse_mode='HTML', reply_markup=telebot.types.ReplyKeyboardRemove())



