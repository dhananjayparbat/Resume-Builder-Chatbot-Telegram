from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'

# Variable to store the received message
received_message = ""

# Command handler to start the bot
def start(update: Update, context) -> None:
    update.message.reply_text('Bot is running. Send me a message.')

# Message handler to capture text messages
def echo(update: Update, context) -> None:
    global received_message
    received_message = update.message.text
    update.message.reply_text(f'Message received: {received_message}')

def main() -> None:
    # Create the Updater and pass it the bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handler
    dp.add_handler(CommandHandler("start", start))

    # Register the message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
