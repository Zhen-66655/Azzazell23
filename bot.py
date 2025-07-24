from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, ContextTypes, filters
)

TOKEN = "8252579113:AAF_9zQEFe_W9lSH2KjHdFL4zu1MQK4xYY0"

# Fungsi saat /start diketik
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot siap digunakan.")

# Fungsi menangani semua pesan biasa
async def echo_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_user.username or update.effective_user.first_name
    message = update.message.text

    print(f"📩 Pesan dari {username} (chat_id: {chat_id}): {message}")
    await update.message.reply_text(f"Hai {username}, chat ID kamu: {chat_id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Tangani perintah /start
    app.add_handler(CommandHandler("start", start))

    # Tangani semua pesan biasa
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_all))

    print("🤖 Bot aktif, menunggu pesan...")
    app.run_polling()
