from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list


def start(update, context) -> None:
    # Create an inline keyboard with buttons for each category
    keyboard = [
        [InlineKeyboardButton(category, callback_data=category)]
        for category in shopping_list.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the initial message with the keyboard to select a category
    update.message.reply_text(
        'Будь ласка, оберіть категорію:', reply_markup=reply_markup)
