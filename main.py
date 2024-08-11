from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext

# Структура даних для зберігання списку покупок
shopping_list = {
    "Продукти": {
        "Овочі": [],
        "Фрукти": [],
    },
    "Одяг": {
        "Верхній одяг": [],
        "Взуття": [],
    },
    "Електроніка": {
        "Телефони": [],
        "Ноутбуки": [],
    },
    "Іграшки": {
        "М'які іграшки": [],
        "Кубики": [],
    },
    "Для дому": {
        "Меблі": [],
        "Посуд": [],
    },
    "Здоров'я": {
        "Вітаміни": [],
        "Медичні товари": [],
    }
}

# Для зберігання поточного вибору користувача
user_data = {}

# Стартова функція


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(category, callback_data=category)]
        for category in shopping_list.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Оберіть категорію:', reply_markup=reply_markup)

# Функція для обробки вибору категорії


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    data = query.data
    if "_" in data:  # Якщо це підкатегорія
        category, subcategory = data.split("_")
        context.user_data['current_category'] = category
        context.user_data['current_subcategory'] = subcategory
        query.edit_message_text(
            text=f"Додайте товар до підкатегорії {subcategory}. Введіть назву товару або /done, щоб завершити.")
    else:  # Якщо це категорія
        category = data
        subcategories = shopping_list[category].keys()

        keyboard = [
            [InlineKeyboardButton(
                subcategory, callback_data=f"{category}_{subcategory}")]
            for subcategory in subcategories
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            text=f"Оберіть підкатегорію в {category}:", reply_markup=reply_markup)

# Функція для додавання товару


def add_item(update: Update, context: CallbackContext) -> None:
    category = context.user_data.get('current_category')
    subcategory = context.user_data.get('current_subcategory')

    if category and subcategory:
        item = update.message.text
        shopping_list[category][subcategory].append(item)
        update.message.reply_text(f"Товар '{item}' додано до {subcategory}.")

# Функція для завершення додавання товарів


def done(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Додавання товарів завершено. Використайте /list, щоб переглянути список покупок.")

# Функція для перегляду списку покупок


def view_list(update: Update, context: CallbackContext) -> None:
    message = "Ваш список покупок:\n"
    for category, subcategories in shopping_list.items():
        message += f"\n*{category}*:\n"
        for subcategory, items in subcategories.items():
            message += f"  - {subcategory}: {', '.join(items) if items else 'Порожньо'}\n"
    update.message.reply_text(message, parse_mode='Markdown')

# Функція для видалення товару


def remove_item(update: Update, context: CallbackContext) -> None:
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


def main() -> None:
    updater = Updater("YOUR TELEGRAM BOT TOKEN")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('done', done))
    updater.dispatcher.add_handler(CommandHandler('list', view_list))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, add_item))
    updater.dispatcher.add_handler(CommandHandler('remove', remove_item))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
