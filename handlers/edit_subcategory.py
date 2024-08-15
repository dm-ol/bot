from data.shopping_list import shopping_list


def edit_subcategory(update, context) -> None:
    try:
        # Extract category, old subcategory name, and new subcategory name
        category, old_subcategory, new_subcategory = context.args[
            0], context.args[1], context.args[2]
        if category in shopping_list and old_subcategory in shopping_list[category]:
            # Rename the subcategory
            shopping_list[category][new_subcategory] = shopping_list[category].pop(
                old_subcategory)
            update.message.reply_text(
                f"Підкатегорію '{old_subcategory}' у категорії '{category}' перейменовано на '{new_subcategory}'.")
        else:
            update.message.reply_text(
                f"Підкатегорія '{old_subcategory}' або категорія '{category}' не знайдена.")
    except (IndexError, ValueError):
        update.message.reply_text(
            "Будь ласка, вкажіть категорію, стару і нову назву підкатегорії у форматі: /editsubcategory <категорія> <стара> <нова>.")
