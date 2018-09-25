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

print("Tutorial: Here's what you can do. Type in: ")
print("[R] to save the name to My List.")
print("[L] to save the name in Trash List.")
print("[M] to see your current My List.")
print("[T] to see your current Trash List.")
print("[E] to exit.")

user_name = input("What is your name?: ")
print("Hi " + user_name + "!")
gender_input = input("Which name list do you want to see, female, male or all?: ")

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
    print("Here's your current My List!")
    print("My List", my_list)

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
    print("Here's your current My List!")
    print("My List", my_list)

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
    print("Here's your current My List!")
    print("My List", my_list)

#Export list to CSV
with open('user_name.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(my_list)