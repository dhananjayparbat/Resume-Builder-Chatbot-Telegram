from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import Update
import yaml
import sys

TOKEN = '5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8'

user_inputs = [None] * 24  # List to store user inputs

def start(update: Update, context) -> None:
    update.message.reply_text('Welcome! Please provide the following information for your resume:\n'
                              '1. Name')

def collect_resume_info(update: Update, context) -> None:
    global user_inputs

    user_input = update.message.text

    if None in user_inputs:
        index = user_inputs.index(None)
        user_inputs[index] = user_input
        next_index = user_inputs.index(None)

        if next_index != -1:
            update.message.reply_text(f"{next_index + 1}. Please provide the next information.")
        else:
            create_yaml(update.message)
            sys.exit(0)  # Terminate the program
    else:
        update.message.reply_text("Thank you! Information collected for your resume.")
        create_yaml(update.message)
        sys.exit(0)  # Terminate the program

def create_yaml(message):
    yaml_template = """
    full name: {0}
    job title: {1}
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

    formatted_yaml = yaml_template.format(*user_inputs)
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
