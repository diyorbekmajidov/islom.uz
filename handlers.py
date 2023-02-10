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


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    inlinekeyborad = InlineKeyboardMarkup([
        [InlineKeyboardButton("Qoraqalpog'iston", callback_data = "Karakalpakstan")],
        [InlineKeyboardButton('Toshkent', callback_data = "Tashkent"), InlineKeyboardButton("Surxondaryo", callback_data = "Surkhandarya")],
        [InlineKeyboardButton("Andijon", callback_data = 'Andijan'), InlineKeyboardButton("Farg'ona", callback_data = "Ferghana")],
        [InlineKeyboardButton("Namangan", callback_data = "Namangan"), InlineKeyboardButton("Sirdaryo", callback_data = "Syr Darya")],
        [InlineKeyboardButton("Smarqand", callback_data = "Smarkand"), InlineKeyboardButton("Qashqadaryo", callback_data = "Kashkadarya")],
        [InlineKeyboardButton("Buxoro", callback_data="Bukhra"), InlineKeyboardButton("Xorazim", callback_data = "Khorazim")],
        [InlineKeyboardButton("Navoiy", callback_data = "Navoi"), InlineKeyboardButton("Jizzax", callback_data = "Jizzakh")],
    ])

    text = f"Assalomu alaykum {first_name} IslomNur botimizga hush kilibsiz \n Namoz vaqtlarini bilish uchun viloyatni tanlang"
    update.message.reply_text(text,reply_markup=inlinekeyborad)

def prayer(update:Update, contexr:CallbackContext):
    query = update.callback_query
    city = query.data
    url = "https://aladhan.p.rapidapi.com/timingsByCity"

    querystring = {"country":"Uzbekistan","city":f'{city}'}

    headers = {
        "X-RapidAPI-Key": "985cef3375msh3d3b11fac985565p1acdc4jsnbb0709f31f0b",
        "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response['data']['timings']
    fajr = data["Fajr"]
    sunrise = data["Sunrise"]
    dhuhr = data["Dhuhr"]
    asr = data["Asr"]
    sunset = data["Sunset"]
    maghrib = data["Maghrib"]
    isha = data["Isha"]
    imsak = data["Imsak"]
    midnight = data["Midnight"]
    firstthird = data["Firstthird"]
    lastthird = data["Lastthird"]
