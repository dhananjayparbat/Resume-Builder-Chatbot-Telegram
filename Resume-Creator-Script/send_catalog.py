import os
from telegram import Bot

# Replace 'YOUR_API_TOKEN' with your bot's API token
bot = Bot('5883900901:AAHCdl8eKx8as1aCxDbNdMYEVI9fBbYLJy8')

# Replace 'CHAT_ID' with the chat ID where you want to send the files
chat_id = '5943365437'

# Replace 'DIRECTORY_PATH' with the path to the directory containing .pdf files
directory_path = '/home/reaper/Resume-Creator-Script/template_catalog'

# List files in the directory
files = os.listdir(directory_path)

# Filter files with .pdf extension and upload
for file in files:
    if file.endswith('.pdf'):
        file_path = os.path.join(directory_path, file)
        with open(file_path, 'rb') as pdf_file:
            bot.send_document(chat_id=chat_id, document=pdf_file)
