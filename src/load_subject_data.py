# Open json file and load data
import json
import os
from PIL import Image

class Person():
	def __init__(self, id : int, date_of_birth : str, firstname: str, lastname: str, picture_path : str, ekg_tests):
		self.id = id
		self.date_of_birth = date_of_birth
		self.firstname = firstname
		self.lastname = lastname
		self.picture_path = picture_path
		self.ekg_tests = ekg_tests

	def get_fullname(self):
		return self.lastname + " " + self.firstname


def load_subject_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

	# User Data Dictionary in Personen in ein Array speichern
    person_list = []
    for person_dict in data:
        current_person = Person(person_dict["id"], 
					person_dict["date_of_birth"], 
					person_dict["firstname"], 
					person_dict["lastname"], 
					person_dict["picture_path"], 
					person_dict["ekg_tests"])
        person_list.append(current_person)
    
    return person_list

def get_subject_names(person_list):
    subject_names = []
    for person in person_list:
        subject_names.append(person.firstname + " " + person.lastname)

    return subject_names

def get_subject_image(person_list, current_subject):
    for person in person_list:
        if person.firstname + " " + person.lastname == current_subject:
            image_path = person.picture_path
    image = Image.open(image_path)
    return image


if __name__ == "__main__":
    # Define FILE_PATH
    FILE_PATH = "data/person_db.json"
    user_data = load_subject_data(FILE_PATH)
    print(user_data)
    print(user_data[1].firstname)
    #name_list = get_subject_names(FILE_PATH)
    #print(name_list)

    # Test if class works
    person_1 = Person(1, "22.01.2000", "John", "Doe", "data/pictures/jd.png", [])
    print(person_1.firstname)
    print(person_1.get_fullname())
    



