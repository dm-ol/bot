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


def view_category(update, context, category) -> None:
    # Generate a list of subcategories within the selected category
    subcategories = shopping_list.get(category, {})
    keyboard = [[InlineKeyboardButton(
        subcategory, callback_data=f'view_{category}_{subcategory}')] for subcategory in subcategories.keys()]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the list of subcategories
    update.callback_query.message.reply_text(
        f"Оберіть підкатегорію в '{category}':", reply_markup=reply_markup)


def view_subcategory(update, context, category, subcategory) -> None:
    # Generate a list of items within the selected subcategory
    items = shopping_list.get(category, {}).get(subcategory, [])
    message = f"Продукти в підкатегорії '{subcategory}':\n"
    for item in items:
        quantity = item.get('quantity', 0)
        message += f"- {item['name']} (кількість: {quantity})\n"

    # Send a message with the list of items and their quantities
    update.callback_query.message.reply_text(message)


def button_handler(update, context) -> None:
    query = update.callback_query
    data = query.data

    if data.startswith('view_'):
        parts = data.split('_')
        if len(parts) == 2:
            view_category(update, context, parts[1])
        elif len(parts) == 3:
            view_subcategory(update, context, parts[1], parts[2])

    query.answer()
