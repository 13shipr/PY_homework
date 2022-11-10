# import logging
from config import TOKEN
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", com_help))

print('server ok')
app.run_polling()
