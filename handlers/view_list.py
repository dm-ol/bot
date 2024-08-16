from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list


def view_list(update, context) -> None:
    # Generate a list of categories with navigation buttons
    keyboard = [[InlineKeyboardButton(
        category, callback_data=f'view_{category}')] for category in shopping_list.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the list of categories
    update.callback_query.message.reply_text(
        "Оберіть категорію для перегляду:", reply_markup=reply_markup)

    # Additional functionality for showing subcategories and items can be added here
