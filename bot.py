from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler
    
)
from handlers import (
    start,
    prayer,
    back,
)
TOKEN = f'6097820347:AAFk8qxkkUSqSVsuUlBTDEjdzMiWTWpA5HU'
updater = Updater(TOKEN)
updater.bot.set_webhook('')

def main() -> None:
    """
    Run the bot.
    """
    # Create the Updater and pass it your bot's token.

    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(prayer, pattern="👍"))
    dp.add_handler(CallbackQueryHandler(back, pattern="⬅️Orqaga"))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()