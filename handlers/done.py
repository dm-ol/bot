def done(update, context) -> None:
    # Notify the user that item adding is finished
    update.message.reply_text(
        "Додавання товарів завершено. Використайте /list, щоб переглянути список покупок.")
