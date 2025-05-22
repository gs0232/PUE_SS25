# Open json file and load data
import json
import os
from PIL import Image

# Example usage
FILE_PATH = "data/person_db.json"  # Replace with your actual file path

def load_subject_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def get_subject_names(data):
    # user_data[0]['firstnames']
    subject_name = []
    for person in data:
        subject_name.append(person['firstname'] + " " + person['lastname'])

    return subject_name

def get_subject_image(current_subject):
    for person in load_subject_data(FILE_PATH):
        if person['firstname'] + " " + person['lastname'] == current_subject:
            image_path = person['picture_path']
    image = Image.open(image_path)
    return image


if __name__ == "__main__":
    user_data = load_subject_data(FILE_PATH)
    name_list = get_subject_names(user_data)
    print(name_list)
    



