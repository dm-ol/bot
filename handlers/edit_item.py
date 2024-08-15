from data.shopping_list import shopping_list


def edit_item(update, context) -> None:
    try:
        # Extract category, subcategory, old item name, and new item name
        category, subcategory, old_item, new_item = context.args[
            0], context.args[1], context.args[2], context.args[3]
        if category in shopping_list and subcategory in shopping_list[category] and old_item in shopping_list[category][subcategory]:
            # Rename the item
            index = shopping_list[category][subcategory].index(old_item)
            shopping_list[category][subcategory][index] = new_item
            update.message.reply_text(
                f"Товар '{old_item}' у підкатегорії '{subcategory}' перейменовано на '{new_item}'.")
        else:
            update.message.reply_text(
                f"Товар '{old_item}' або підкатегорія '{subcategory}' у категорії '{category}' не знайдено.")
    except (IndexError, ValueError):
        update.message.reply_text(
            "Будь ласка, вкажіть категорію, підкатегорію, стару і нову назву товару у форматі: /edititem <категорія> <підкатегорія> <старий товар> <новий товар>.")
