from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
import yaml
import sys
import time

TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'
updater = Updater(TOKEN)

# Variables to store user input
name, job_title, portfolio, github, linkedin, mail, phone = [None] * 7
city, country, summary ,skills= [None] * 4
experiences = [None] * 3
projects = [None] * 3
education = [None] * 2

# Counter to track current question
questions = [
    "name", "job title", "portfolio link", "GitHub link", "LinkedIn link", "mail", "phone number",
    "city", "country", "summary",
    "1st skill","experience", "experience duration", "experience details",
    "project name", "project summary", "project skills",
    "degree", "batch year", "certification", "certification duration"
]
current_question = 0

def start(update: Update, context) -> None:
    global current_question
    current_question = 0
    update.message.reply_text(f'Please provide your {questions[current_question]}:')

'''def stop(update, context):
    update.message.reply_text("Bot is stopping.")
    updater.stop()  # Terminates the bot
    exit(0)'''     

def collect_resume_info(update: Update, context) -> None:
    global current_question, name, job_title, portfolio, github, linkedin, mail, phone
    global city, country, summary, skills, experiences, projects, education

    user_input = update.message.text

    if current_question == 0:
        name = user_input
    elif current_question == 1:
        job_title = user_input
    elif current_question == 2:
        portfolio = user_input
    elif current_question == 3:
        github=user_input
    elif current_question == 4:
        linkedin=user_input
    elif current_question == 5:
        mail=user_input
    elif current_question == 6:
        phone=user_input
    elif current_question == 7:
        city=user_input
    elif current_question == 8:
        country=user_input
    elif current_question == 9:
        summary=user_input
    elif current_question == 10:
        skills=user_input    
    elif current_question == 11:
        experiences[0]=user_input    
    elif current_question == 12:
        experiences[1]=user_input
    elif current_question == 13:
        experiences[2]=user_input    
    elif current_question == 14:
        projects[0]=user_input    
    elif current_question == 15:
        projects[1]=user_input    
    elif current_question == 16:
        projects[2]=user_input    
    elif current_question == 17:
        education[0] = user_input
    elif current_question == 18:
        education[1] = user_input

    current_question += 1
    if current_question < len(questions):
        update.message.reply_text(f"Please provide your {questions[current_question]}:")
    else:
        create_yaml(update.message)

def create_yaml(message):
    # Process the collected data and create the YAML file
    data = {
        "full name": name,
        "job title": job_title,
        "links": {
            "Portfolio": portfolio,
            "GitHub": github,
            "LinkedIn": linkedin,
            mail: f"mailto:{mail}",
            f"+91{phone}": f"tel:+91{phone}"
        },
        "not_links": [f"{city} | {country}"],
        "summary": summary,
        "skills": skills,
        "experience": {
            experiences[0]: [experiences[1], experiences[2]]
        },
        "projects": {
            projects[0]: [projects[1], projects[2]]
        },
        "education": {
            education[0]: [education[1]]
        }
    }

    formatted_yaml = yaml.dump(data, default_flow_style=False)
    with open('output.yaml', 'w') as file:
        file.write(formatted_yaml)

    message.reply_text("Your resume information has been saved in output.yaml")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, collect_resume_info))

    updater.start_polling()
    start_time = time.time()
    duration = 30  # 10 minutes in seconds

    while time.time() - start_time < duration:
        time.sleep(1)  # Check every 1 second

    updater.stop()  # Stop the bot after the specified duration
    exit(0)

if __name__ == '__main__':
    main()
