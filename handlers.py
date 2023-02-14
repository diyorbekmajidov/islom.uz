from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    Dispatcher
)
import requests
import islom


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    inlinekeyborad = InlineKeyboardMarkup([
        [InlineKeyboardButton("Qoraqalpog'iston", callback_data = "👍 Karakalpakstan")],
        [InlineKeyboardButton('Toshkent', callback_data = "👍:Tashkent"), InlineKeyboardButton("Surxondaryo", callback_data = "👍:Surkhandarya")],
        [InlineKeyboardButton("Andijon", callback_data = '👍:Andijan'), InlineKeyboardButton("Farg'ona", callback_data = "👍:Ferghana")],
        [InlineKeyboardButton("Namangan", callback_data = "👍:Namangan"), InlineKeyboardButton("Sirdaryo", callback_data = "👍:Syr Darya")],
        [InlineKeyboardButton("Smarqand", callback_data = "👍:Samarkand"), InlineKeyboardButton("Qashqadaryo", callback_data = "👍:Kashkadarya")],
        [InlineKeyboardButton("Buxoro", callback_data="👍:Bukhra"), InlineKeyboardButton("Xorazim", callback_data = "👍:Khorazim")],
        [InlineKeyboardButton("Navoiy", callback_data = "👍:Navoi"), InlineKeyboardButton("Jizzax", callback_data = "👍:Jizzakh")],
    ])

    text = f"Assalomu alaykum {first_name} IslomNur botimizga hush kilibsiz\n Namoz vaqtlarini bilish uchun viloyatni tanlang"
    update.message.reply_text(text,reply_markup=inlinekeyborad)

def prayer(update:Update, context:CallbackContext):
    query = update.callback_query
    bot = context.bot
    data = query.data
    city=data.split(":")[1]
    islom.prayer(city)
    bot.send_photo(chat_id=query.message.chat_id, photo=open('image1.png', 'rb'))
    # query.edit_message_text(text=text,parse_mode=ParseMode.HTML)