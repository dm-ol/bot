from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list


def button(update, context) -> None:
    query = update.callback_query
    query.answer()

    data = query.data
    if "_" in data:  # Якщо це підкатегорія
        category, subcategory = data.split("_")
        context.user_data['current_category'] = category
        context.user_data['current_subcategory'] = subcategory
        query.edit_message_text(
            text=f"Додайте товар до підкатегорії {subcategory}. Введіть назву товару або /done, щоб завершити.")
    else:  # Якщо це категорія
        category = data
        subcategories = shopping_list[category].keys()

        keyboard = [
            [InlineKeyboardButton(
                subcategory, callback_data=f"{category}_{subcategory}")]
            for subcategory in subcategories
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text=f"Оберіть підкатегорію в {category}:", reply_markup=reply_markup)
