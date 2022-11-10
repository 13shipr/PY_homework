# bot commands modul

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def com_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/Hello\n/Help\n')