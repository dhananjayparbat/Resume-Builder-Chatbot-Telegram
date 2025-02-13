from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
import yaml
import sys

TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'

# Variables to store user input
name, job_title, portfolio, github, linkedin, mail, phone = [None] * 7
city, country, summary = [None] * 3
skills = [None] * 4
experiences = [None] * 3
projects = [None] * 3
education = [None] * 2

# Counter to track current question
questions = [
    "name", "job title", "portfolio link", "GitHub link", "LinkedIn link", "mail", "phone number",
    "city", "country", "summary",
    "1st skill", "2nd skill", "3rd skill", "4th skill",
    "experience", "experience duration", "experience details",
    "project name", "project summary", "project skills",
    "degree", "batch year", "certification", "certification duration"
]
current_question = 0

def start(update: Update, context) -> None:
    global current_question
    current_question = 0
    update.message.reply_text(f'Please provide your {questions[current_question]}:')

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
        github = user_input
    elif current_question == 4:
        linkedin = user_input
    elif current_question == 5:
        mail = user_input
    elif current_question == 6:
        phone = user_input
    elif current_question == 7:
        city = user_input
    elif current_question == 8:
        country = user_input
    elif current_question == 9:
        summary = user_input
    elif 9 < current_question < 14:
        skills[current_question - 10] = user_input
    elif 13 < current_question < 17:
        experiences[current_question - 14] = user_input
    elif 16 < current_question < 20:
        projects[current_question - 17] = user_input
    elif 19 < current_question < 23:
        education[current_question - 20] = user_input

    current_question += 1
    if current_question < len(questions):
        update.message.reply_text(f"Please provide your {questions[current_question]}:")
    else:
        create_yaml(update.message)
        sys.exit(0)  # Terminate the program

def create_yaml(message):
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
    updater.idle()

if __name__ == '__main__':
    main()
