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
from islom import prayer


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    inlinekeyborad = InlineKeyboardMarkup([
        [InlineKeyboardButton("Qoraqalpog'iston", callback_data = "👍 Karakalpakstan")],
        [InlineKeyboardButton('Toshkent', callback_data = "👍 Tashkent"), InlineKeyboardButton("Surxondaryo", callback_data = "👍_Surkhandarya")],
        [InlineKeyboardButton("Andijon", callback_data = '👍 Andijan'), InlineKeyboardButton("Farg'ona", callback_data = "👍_Ferghana")],
        [InlineKeyboardButton("Namangan", callback_data = "👍_Namangan"), InlineKeyboardButton("Sirdaryo", callback_data = "👍_Syr Darya")],
        [InlineKeyboardButton("Smarqand", callback_data = "👍 Smarkand"), InlineKeyboardButton("Qashqadaryo", callback_data = "👍_Kashkadarya")],
        [InlineKeyboardButton("Buxoro", callback_data="👍_Bukhra"), InlineKeyboardButton("Xorazim", callback_data = "👍_Khorazim")],
        [InlineKeyboardButton("Navoiy", callback_data = "👍_Navoi"), InlineKeyboardButton("Jizzax", callback_data = "👍_Jizzakh")],
    ])

    text = f"Assalomu alaykum {first_name} IslomNur botimizga hush kilibsiz\n Namoz vaqtlarini bilish uchun viloyatni tanlang"
    update.message.reply_text(text,reply_markup=inlinekeyborad)

def prayer(update:Update, contexr:CallbackContext):
    query = update.callback_query
    city = query.data
    print(city.split(" ")[-1])
    print(prayer(city.split(" ")[-1]))
    # text = f'bomdot:{fajr}'
    # query.edit_message_text(text=text,parse_mode=ParseMode.HTML)