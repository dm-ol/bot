from data.shopping_list import shopping_list


def view_list(update, context) -> None:
    # Generate a formatted message of the entire shopping list
    message = "Ваш список покупок:\n"
    for category, subcategories in shopping_list.items():
        message += f"\n*{category}*:\n"
        for subcategory, items in subcategories.items():
            message += f"  - {subcategory}: {', '.join(items) if items else 'Порожньо'}\n"
    update.message.reply_text(message, parse_mode='Markdown')
