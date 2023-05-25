from flask import Flask, request

app = Flask(__name__)


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    Dispatcher
    
)
from handlers import (
    start,
    prayer,
    back,
)
TOKEN = f'6097820347:AAFk8qxkkUSqSVsuUlBTDEjdzMiWTWpA5HU'

@app.route('/home')
def home():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def webhook():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(prayer, pattern="👍"))
    dp.add_handler(CallbackQueryHandler(back, pattern="⬅️Orqaga"))

    update = update.Update.de_json(request.get_json(force=True))

    dp.process_update(update)

    return 'OK'
