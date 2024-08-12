from data.shopping_list import shopping_list


def remove_item(update, context) -> None:
    category = context.user_data.get('current_category')
    subcategory = context.user_data.get('current_subcategory')

    if category and subcategory:
        item = update.message.text
        if item in shopping_list[category][subcategory]:
            shopping_list[category][subcategory].remove(item)
            update.message.reply_text(
                f"Товар '{item}' видалено з {subcategory}.")
        else:
            update.message.reply_text(
                f"Товар '{item}' не знайдено у {subcategory}.")
