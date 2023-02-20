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
        [InlineKeyboardButton("Qoraqalpog'iston", callback_data = "👍:Нукус")],
        [InlineKeyboardButton('Toshkent', callback_data = "👍:Тошкент"), InlineKeyboardButton("Surxondaryo", callback_data = "👍:Термиз")],
        [InlineKeyboardButton("Andijon", callback_data = '👍:Андижон'), InlineKeyboardButton("Farg'ona", callback_data = "👍:Фарғона")],
        [InlineKeyboardButton("Namangan", callback_data = "👍:Наманган"), InlineKeyboardButton("Sirdaryo", callback_data = "👍:Гулистон")],
        [InlineKeyboardButton("Samarqand", callback_data = "👍:Самарқанд"), InlineKeyboardButton("Qashqadaryo", callback_data = "👍:Қарши")],
        [InlineKeyboardButton("Buxoro", callback_data="👍:Бухоро"), InlineKeyboardButton("Xorazim", callback_data = "👍:Хива")],
        [InlineKeyboardButton("Navoiy", callback_data = "👍:Навоий"), InlineKeyboardButton("Jizzax", callback_data = "👍:Жиззах")],
    ])

    text = f"Assalomu alaykum {first_name} IslomNur botimizga hush kilibsiz\n Namoz vaqtlarini bilish uchun viloyatni tanlang"
    update.message.reply_text(text,reply_markup=inlinekeyborad)

def prayer(update:Update, context:CallbackContext):
    query = update.callback_query
    bot = context.bot
    data = query.data
    city=data.split(":")[1]
    islom.parser_url(city)
    bot.send_photo(chat_id=query.message.chat_id, photo=open('ima1.png', 'rb'))
    # query.edit_message_text(text=text,parse_mode=ParseMode.HTML)