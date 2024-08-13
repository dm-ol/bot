from data.shopping_list import shopping_list


def add_category(update, context) -> None:
    try:
        category = context.args[0]
        if category in shopping_list:
            update.message.reply_text(f"Категорія '{category}' вже існує.")
        else:
            shopping_list[category] = {}
            update.message.reply_text(
                f"Категорія '{category}' успішно додана.")
    except IndexError:
        update.message.reply_text(
            "Будь ласка, вкажіть назву категорії після команди /addcategory.")
