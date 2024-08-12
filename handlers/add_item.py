from data.shopping_list import shopping_list


def add_item(update, context) -> None:
    category = context.user_data.get('current_category')
    subcategory = context.user_data.get('current_subcategory')

    if category and subcategory:
        item = update.message.text
        shopping_list[category][subcategory].append(item)
        update.message.reply_text(f"Товар '{item}' додано до {subcategory}.")
