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
    elif query.data.startswith('view_sub_'):
        view_subcategory(query, context)
    elif query.data.startswith('add_item_'):
        add_item_prompt(query, context)
    elif query.data.startswith('remove_item_'):
        remove_item_prompt(query, context)
    elif query.data.startswith('edit_item_'):
        edit_item_prompt(query, context)
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
        sub, callback_data=f'view_sub_{category}_{sub}')] for sub in subcategories]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        f"Категорія: {category}. Оберіть підкатегорію:", reply_markup=reply_markup)


def view_subcategory(query, context):
    category, subcategory = query.data.split('_')[2], query.data.split('_')[3]
    items = shopping_list.get(category, {}).get(subcategory, [])

    # Create buttons for items within the subcategory
    keyboard = [[InlineKeyboardButton(
        f"{item['name']} (кількість: {item['quantity']})", callback_data=f'edit_item_{category}_{subcategory}_{item["name"]}')
    ] for item in items]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text(
        f"Підкатегорія: {subcategory}. Оберіть продукт для редагування:", reply_markup=reply_markup)


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


def add_item_prompt(query, context):
    # Prompt the user to enter a new item in the selected subcategory
    category, subcategory = query.data.split('_')[2], query.data.split('_')[3]
    context.user_data['add_item_category'] = category
    context.user_data['add_item_subcategory'] = subcategory
    query.message.reply_text(
        f"Введіть назву продукту для додавання в '{subcategory}':")


def remove_item_prompt(query, context):
    # Prompt the user to select an item to remove
    category, subcategory, item = query.data.split('_')[2], query.data.split('_')[
        3], query.data.split('_')[4]
    shopping_list[category][subcategory].remove(item)
    query.message.reply_text(f"Продукт '{item}' видалено з '{subcategory}'.")


def edit_item_prompt(query, context):
    # Prompt the user to edit an item or its quantity
    category, subcategory, item_name = query.data.split(
        '_')[2], query.data.split('_')[3], query.data.split('_')[4]
    context.user_data['edit_item_category'] = category
    context.user_data['edit_item_subcategory'] = subcategory
    context.user_data['edit_item_name'] = item_name
    query.message.reply_text(
        f"Введіть нову кількість для '{item_name}' в підкатегорії '{subcategory}':")
