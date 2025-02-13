from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
import yaml
import sys

TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'

user_inputs = {}

def start(update: Update, context) -> None:
    update.message.reply_text('Welcome! Please provide the following information for your resume:\n'
                              '1. Name')

def collect_resume_info(update: Update, context) -> None:
    global user_inputs

    user_input = update.message.text

    if len(user_inputs) < 23:  # Modify this based on the total number of inputs expected
        user_inputs[len(user_inputs)] = user_input
        update.message.reply_text(f"{len(user_inputs) + 1}. Please provide the next information.")
        
        if len(user_inputs) == 23:  # Modify this based on the total number of inputs expected
            create_yaml(update.message)
    else:
        update.message.reply_text("Thank you! Information collected for your resume.")
        create_yaml(update.message)
        sys.exit(0)

def create_yaml(message):
    yaml_template = """
    full name: {0}
    job title: {1}
    primary color: 008080
links:
  - Portfolio: {2}
  - GitHub: {3}
  - LinkedIn: {4}
  - {5}: mailto:{5}
  - "+91{6}": tel:+91{6}


not_links:
  - {7} | {8}



summary: |
  {9}
  
skills:
  - {10}
  - {11}
  - {12}
  - {13}

experience:
  - {14}:
    - {15}
    - |
      - {16}

      Highlighted skills: {17}
  
projects:
  - {18}:
      - |
        {19}

        Highlighted skills: {20}

education:
  - {21}:
      - "{22}"

  - {23}:
      - "{24}"
    """

    formatted_yaml = yaml_template.format(*user_inputs.values())
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
