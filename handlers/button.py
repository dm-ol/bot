from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list
from handlers.view_list import view_list  # Import view_list function
from handlers.add_category import add_category
from handlers.remove_category import remove_category
from handlers.edit_category import edit_category


def button(update, context) -> None:
    query = update.callback_query
    query.answer()

    # Handle different actions based on the callback_data
    if query.data == 'view_list':
        view_list(update, context)
    elif query.data == 'add_category':
        add_category_prompt(update, context)
    elif query.data == 'edit_category':
        edit_category_prompt(update, context)
    elif query.data == 'remove_category':
        remove_category_prompt(update, context)


def add_category_prompt(update, context):
    update.callback_query.message.reply_text("Введіть назву нової категорії:")


def edit_category_prompt(update, context):
    # Generate a list of categories for selection
    keyboard = [[InlineKeyboardButton(
        category, callback_data=f'edit_{category}')] for category in shopping_list.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        "Оберіть категорію для редагування:", reply_markup=reply_markup)


def remove_category_prompt(update, context):
    # Generate a list of categories for removal
    keyboard = [[InlineKeyboardButton(
        category, callback_data=f'remove_{category}')] for category in shopping_list.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        "Оберіть категорію для видалення:", reply_markup=reply_markup)
