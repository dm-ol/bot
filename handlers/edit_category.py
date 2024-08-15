from data.shopping_list import shopping_list


def edit_category(update, context) -> None:
    try:
        # Extract old and new category names from the command arguments
        old_category, new_category = context.args[0], context.args[1]
        if old_category in shopping_list:
            # Rename the category
            shopping_list[new_category] = shopping_list.pop(old_category)
            update.message.reply_text(
                f"Категорію '{old_category}' перейменовано на '{new_category}'.")
        else:
            update.message.reply_text(
                f"Категорія '{old_category}' не знайдена.")
    except (IndexError, ValueError):
        update.message.reply_text(
            "Будь ласка, вкажіть стару і нову назву категорії у форматі: /editcategory <стара> <нова>.")
