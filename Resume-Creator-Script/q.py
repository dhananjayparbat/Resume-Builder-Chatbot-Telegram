from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update

TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'

# Variables to store user information
resume_info = {
    "name": None,
    "job_title": None,
    "portfolio_link": None,
    "github_link": None,
    "linkedin_link": None,
    "mail": None,
    "phone_no": None,
    "city": None,
    "country": None,
    "summary": None,
    "skills": [None, None, None, None],
    "experience": [None, None, None]  # [experience1, duration1, work1]
}

# Counter to keep track of information collection
info_index = 0

def start(update: Update, context) -> None:
    update.message.reply_text('Welcome! Please provide the following information for your resume:\n'
                              '1. Name')

def collect_resume_info(update: Update, context) -> None:
    global info_index
    global resume_info

    # Get the user's message
    user_input = update.message.text

    # Update resume information based on the user's input
    if info_index < len(resume_info):
        resume_info[list(resume_info.keys())[info_index]] = user_input
        info_index += 1

    # Get the next piece of information to collect or end the process
    if info_index < len(resume_info):
        update.message.reply_text(f"Next, please provide your {list(resume_info.keys())[info_index]}")
    else:
        update.message.reply_text("Thank you! Information collected for your resume.")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, collect_resume_info))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
