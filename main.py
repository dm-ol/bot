from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from handlers.start import start
from handlers.button import button
from handlers.add_item import add_item
from handlers.done import done
from handlers.view_list import view_list
from handlers.remove_item import remove_item


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
