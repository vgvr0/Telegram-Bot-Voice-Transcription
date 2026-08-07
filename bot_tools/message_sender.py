from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove




def send_message_with_keyboard(bot, message, answer):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    keyboard.add(
    KeyboardButton(text="🇺🇸 English"),
        KeyboardButton(text="🇪🇸 España"),
        KeyboardButton(text="🇰🇿 Қазақ"),
        KeyboardButton(text="🇷🇺 Русский")
    )


    bot.send_message(message.chat.id, answer, parse_mode='HTML', reply_markup=keyboard)


def send_message_without_keyboard(bot, message, answer):
    bot.send_message(message.chat.id, answer, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())



