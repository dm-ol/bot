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

    # Register handlers for different commands and messages
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start polling for updates
    updater.start_polling()

    # Block until you press Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
