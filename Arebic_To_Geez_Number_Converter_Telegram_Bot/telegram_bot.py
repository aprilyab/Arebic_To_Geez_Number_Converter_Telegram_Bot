from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import API
from telegram.ext import MessageHandler, filters
from telegram import Update

# import chessAPI
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(os.getenv("TELEGRAM_API_TOKEN"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    # user_message = update.message.text.split(" ")[1]
    message = "Hello this bot converts Arabic numbers to Geez numbers. Just send me a number from 1 to 100,000"
    await context.bot.send_message(chat_id, message)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message = "Hello this bot converts Arabic numbers to Geez numbers. Just send me a number from 1 to 100,000"
    await context.bot.send_message(chat_id, message)


# This function handles all text messages that aren't commands
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = str(update.message.text)
    chat_id = update.effective_chat.id
    try:
        number = int(user_message)
        if number < 1 or number > 100_001:
            await context.bot.send_message(
                chat_id, "Out of range. Only number from 1 to 100,000"
            )
            return
        message = f"Arabic number {user_message} = Geez number {API.convert_to_geez(int(user_message))}"
        await context.bot.send_message(chat_id, message)
    except Exception as e:
        print(e)
        await context.bot.send_message(chat_id, "Invalid Number")


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.run_polling()
