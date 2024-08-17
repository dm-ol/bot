from telegram import Update
from telegram.ext import CallbackContext
from data.shopping_list import shopping_list


def add_item_prompt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Введіть назву продукту:")


def add_item(update: Update, context: CallbackContext) -> None:
    item_name = update.message.text
    context.user_data['item_name'] = item_name
    update.message.reply_text(
        f"Ви додали продукт '{item_name}'. Введіть кількість:")


def set_item_quantity(update: Update, context: CallbackContext) -> None:
    quantity = int(update.message.text)
    item_name = context.user_data['item_name']
    category = context.user_data.get('category')
    subcategory = context.user_data.get('subcategory')

    # Add the item with the specified quantity
    for item in shopping_list[category][subcategory]:
        if item['name'] == item_name:
            item['quantity'] = quantity
            break
    else:
        shopping_list[category][subcategory].append(
            {'name': item_name, 'quantity': quantity})

    update.message.reply_text(
        f"Продукт '{item_name}' у кількості {quantity} додано до списку.")
