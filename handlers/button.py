from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list
from handlers.view_list import view_list  # Import the view_list function
from handlers.add_category import add_category
from handlers.remove_category import remove_category
from handlers.edit_category import edit_category
from handlers.add_item import add_item
from handlers.remove_item import remove_item
from handlers.edit_subcategory import edit_subcategory
from handlers.edit_item import edit_item


def button(update, context) -> None:
    query = update.callback_query
    query.answer()

    # Handle different actions based on the callback_data
    if query.data == 'start_interaction':
        show_main_menu(update)
    elif query.data == 'view_list':
        view_list(update, context)
    elif query.data == 'add_category':
        add_category_prompt(update, context)
    elif query.data.startswith('edit_'):
        edit_category(query, context)
    elif query.data.startswith('remove_'):
        remove_category(query, context)
    elif query.data.startswith('view_'):
        view_category(query, context)
    # You can add more options here as needed


def show_main_menu(update):
    # Create main menu buttons
    keyboard = [
        [InlineKeyboardButton("Переглянути список",
                              callback_data='view_list')],
        [InlineKeyboardButton("Додати категорію",
                              callback_data='add_category')],
        [InlineKeyboardButton("Редагувати категорію",
                              callback_data='edit_category')],
        [InlineKeyboardButton("Видалити категорію",
                              callback_data='remove_category')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the main menu
    update.callback_query.message.reply_text(
        "Оберіть дію:", reply_markup=reply_markup)


def view_category(query, context):
    category = query.data.split('_')[1]
    subcategories = shopping_list.get(category, {})

    # Create buttons for subcategories or products
    keyboard = [[InlineKeyboardButton(
        sub, callback_data=f'view_sub_{sub}')] for sub in subcategories]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        f"Категорія: {category}. Оберіть підкатегорію:", reply_markup=reply_markup)


def add_category_prompt(update, context):
    update.callback_query.message.reply_text("Введіть назву нової категорії:")


def edit_category(query, context):
    category = query.data.split('_')[1]
    context.user_data['edit_category'] = category
    query.message.reply_text(
        f"Ви обрали редагування категорії: {category}. Введіть нову назву або залиште як є:")


def remove_category(query, context):
    category = query.data.split('_')[1]
    del shopping_list[category]
    query.message.reply_text(f"Категорію '{category}' видалено.")
