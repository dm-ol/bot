from data.shopping_list import shopping_list


def add_category(update, context) -> None:
    try:
        # Get the category name from the command arguments
        category = context.args[0]
        if category in shopping_list:
            update.message.reply_text(f"Категорія '{category}' вже існує.")
        else:
            # Add a new category to the shopping list
            shopping_list[category] = {}
            update.message.reply_text(
                f"Категорія '{category}' успішно додана.")
    except IndexError:
        update.message.reply_text(
            "Будь ласка, вкажіть назву категорії після команди /addcategory.")
