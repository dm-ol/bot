from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context) -> None:
    # Create a start button to begin interaction
    keyboard = [[InlineKeyboardButton(
        "Почати", callback_data='start_interaction')]]

    # Create keyboard markup with the button
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the start button
    update.message.reply_text(
        "Ласкаво просимо до вашого списку покупок! Натисніть 'Почати', щоб продовжити.", reply_markup=reply_markup)
