from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from handlers.start import start
from handlers.button import button
from handlers.add_item import add_item
from handlers.done import done
from handlers.view_list import view_list
from handlers.remove_item import remove_item
from handlers.add_category import add_category
from handlers.remove_category import remove_category


def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR TELEGRAM BOT TOKEN")

    # Register handlers for different commands and messages
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('done', done))
    updater.dispatcher.add_handler(CommandHandler('list', view_list))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, add_item))
    updater.dispatcher.add_handler(CommandHandler('remove', remove_item))

    # Handlers for adding and removing categories
    updater.dispatcher.add_handler(CommandHandler('addcategory', add_category))
    updater.dispatcher.add_handler(
        CommandHandler('removecategory', remove_category))

    # Start polling for updates
    updater.start_polling()

    # Block until you press Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
