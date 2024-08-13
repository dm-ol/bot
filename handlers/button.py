from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from data.shopping_list import shopping_list


def button(update, context) -> None:
    query = update.callback_query
    query.answer()

    data = query.data
    if "_" in data:  # If it's a subcategory
        category, subcategory = data.split("_")
        context.user_data['current_category'] = category
        context.user_data['current_subcategory'] = subcategory
        query.edit_message_text(
            text=f"Add an item to the {subcategory} subcategory. Enter the item name or use /done to finish.")
    else:  # If it's a category
        category = data
        subcategories = shopping_list[category].keys()

        # Create buttons for subcategories
        keyboard = [
            [InlineKeyboardButton(
                subcategory, callback_data=f"{category}_{subcategory}")]
            for subcategory in subcategories
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text=f"Please select a subcategory in {category}:", reply_markup=reply_markup)
