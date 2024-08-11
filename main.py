from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

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

    category = query.data
    subcategories = shopping_list[category].keys()

    keyboard = [
        [InlineKeyboardButton(subcategory, callback_data=f"{category}_{subcategory}")]
        for subcategory in subcategories
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=f"Оберіть підкатегорію в {category}:", reply_markup=reply_markup)

def main() -> None:
    updater = Updater("YOUR TELEGRAM BOT TOKEN")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

