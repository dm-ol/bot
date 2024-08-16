from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context) -> None:
    # Create buttons for navigating through categories
    keyboard = [
        [InlineKeyboardButton("Переглянути список",
                              callback_data='view_list')],
        [InlineKeyboardButton("Додати категорію",
                              callback_data='add_category')],
        [InlineKeyboardButton("Редагувати категорію",
                              callback_data='edit_category')],
        [InlineKeyboardButton("Видалити категорію",
                              callback_data='remove_category')]
    ]

    # Create keyboard markup with the buttons
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the navigation buttons
    update.message.reply_text("Оберіть дію:", reply_markup=reply_markup)
