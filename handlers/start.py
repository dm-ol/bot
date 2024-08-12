from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list


def start(update, context) -> None:
    keyboard = [
        [InlineKeyboardButton(category, callback_data=category)]
        for category in shopping_list.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Оберіть категорію:', reply_markup=reply_markup)
