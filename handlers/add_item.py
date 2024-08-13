from data.shopping_list import shopping_list


def add_item(update, context) -> None:
    # Retrieve the current category and subcategory from the user data
    category = context.user_data.get('current_category')
    subcategory = context.user_data.get('current_subcategory')

    if category and subcategory:
        # Get the item name from the user's message
        item = update.message.text
        # Add the item to the corresponding subcategory list
        shopping_list[category][subcategory].append(item)
        update.message.reply_text(
            f"Товар '{item}' додано до підкатегорії {subcategory}.")
