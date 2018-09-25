import csv
import random

all_list = []
female_list = []
male_list = []
my_list = []
trash_list = []

with open ('namelist_db.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        all_list.append(row)
        if row[0] == "female":
            female_list.append(row)
        if row[0] == "male":
            male_list.append(row)   

print("Directions: Type in the following letters.")
print("[R] to save the name to My List.")
print("[L] to save the name in Trash List.")
print("[M] to see your current My List.")
print("[T] to see your current Trash List.")
print("[E] to exit.")

gender_input = input("Select gender female / male / all ?: ")

if gender_input == "female":
    for f in female_list:
        r = random.choice(female_list)
        print("Name: ", " ".join(r[1:3]))
        selection_input = input("Type in a letter: ")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("My List", my_list)
        if selection_input == "T":
            print("Trash List", trash_list)
        if selection_input == "E":
            print("Here's your current My List!")
            print("My List", my_list)
            break

if gender_input == "male":
    for f in male_list:
        r = random.choice(male_list)
        print("Name: ", " ".join(r[1:3]))
        selection_input = input("Type in a letter: ")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("My List", my_list)
        if selection_input == "T":
            print("Trash List", trash_list)
        if selection_input == "E":
            print("Here's your current My List!")
            print("My List", my_list)
            break

if gender_input == "all":
    for f in all_list:
        r = random.choice(all_list)
        print("Name: ", " ".join(r[1:3]))
        selection_input = input("Type in a letter: ")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("My List", my_list)
        if selection_input == "T":
            print("Trash List", trash_list)
        if selection_input == "E":
            print("Here's your current My List!")
            print("My List", my_list)
            break