from data.shopping_list import shopping_list


def remove_item(update, context) -> None:
    # Retrieve the current category and subcategory from the user data
    category = context.user_data.get('current_category')
    subcategory = context.user_data.get('current_subcategory')

    if category and subcategory:
        # Get the item name from the user's message
        item = update.message.text
        if item in shopping_list[category][subcategory]:
            # Remove the item from the subcategory list
            shopping_list[category][subcategory].remove(item)
            update.message.reply_text(
                f"Товар '{item}' видалено з підкатегорії {subcategory}.")
        else:
            update.message.reply_text(
                f"Товар '{item}' не знайдено в підкатегорії {subcategory}.")
