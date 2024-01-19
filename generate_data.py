from PIL import Image
import pytesseract
from googletrans import Translator
import os

import json
from datetime import datetime

result = []
translations = []
data = {}

def get_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    text = text.replace('\n', ' ').replace('_', '').replace('’', '').replace('‘', '')
    return text

def translate_text():
    translator = Translator()
    for index, value in enumerate(result):
        translation = translator.translate(value, dest='es')
        print(f'Translation --> {translation.text}')
        data[index + 1] = {
            "english": value,
            "spanish": translation.text
        }
        translations.append(translation.text)

folder_name = "images"

def read_images():
    # get list of images names
    files = os.listdir(f'./{folder_name}')
    for file_name in files:
        if(file_name.endswith(".png") or file_name.endswith(".jpeg") or file_name.endswith(".jpg")):
            text = get_text_from_image(f'./{folder_name}/{file_name}')
            print(text)
            result.append(text)

def create_data_file():
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

def print_time(execOn):
    current_time = datetime.now()
    human_readable_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Execution {execOn} at:", human_readable_time)

try:
    print_time("started")
    read_images()
    translate_text()
    create_data_file()
    print_time("end")
except:
    print("el horrorr")
    print_time("end with error")