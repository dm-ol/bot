import getpass
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers.start import start
from handlers.button import button
from handlers.add_item import add_item
from handlers.done import done
from handlers.view_list import view_list
from handlers.remove_item import remove_item
from handlers.add_category import add_category
from handlers.remove_category import remove_category
from handlers.edit_category import edit_category
from handlers.edit_subcategory import edit_subcategory
from handlers.edit_item import edit_item


def main() -> None:
    # Prompt the user to enter their Telegram bot token
    token = getpass.getpass("Введіть токен вашого Telegram бота: ")

    # Create the Updater and pass it your bot's token
    updater = Updater(token)

    # Register handlers for the start command and button interactions
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Register handlers for various bot functionalities
    updater.dispatcher.add_handler(CommandHandler('add_item', add_item))
    updater.dispatcher.add_handler(CommandHandler('done', done))
    updater.dispatcher.add_handler(CommandHandler('view_list', view_list))
    updater.dispatcher.add_handler(CommandHandler('remove_item', remove_item))
    updater.dispatcher.add_handler(
        CommandHandler('add_category', add_category))
    updater.dispatcher.add_handler(
        CommandHandler('remove_category', remove_category))
    updater.dispatcher.add_handler(
        CommandHandler('edit_category', edit_category))
    updater.dispatcher.add_handler(CommandHandler(
        'edit_subcategory', edit_subcategory))
    updater.dispatcher.add_handler(CommandHandler('edit_item', edit_item))

    # Start polling for updates
    updater.start_polling()

    # Block until you press Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
