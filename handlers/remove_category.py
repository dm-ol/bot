from data.shopping_list import shopping_list


def remove_category(update, context) -> None:
    try:
        category = context.args[0]
        if category in shopping_list:
            del shopping_list[category]
            update.message.reply_text(
                f"Категорію '{category}' успішно видалено.")
        else:
            update.message.reply_text(f"Категорія '{category}' не знайдена.")
    except IndexError:
        update.message.reply_text(
            "Будь ласка, вкажіть назву категорії після команди /removecategory.")
