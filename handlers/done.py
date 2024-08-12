def done(update, context) -> None:
    update.message.reply_text(
        "Додавання товарів завершено. Використайте /list, щоб переглянути список покупок.")
