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

print("チュートリアル：こんなことができるよ！")
print("[R] = 名前をマイリストに入れる")
print("[L] = 名前をゴミ箱に入れる")
print("[M] = マイリストを見る")
print("[T] = ゴミ箱を見る")
print("[E] = 終了")

user_name = input("あなたの名前は？")
print("こんにちは、" + user_name + "さん!")
gender_input = input("赤ちゃんの性別を選んでください。女の子、男の子、両方: ")

if gender_input == "女の子":
    for f in female_list:
        r = random.choice(female_list)
        print("名前：", " ".join(r[1:3]))
        selection_input = input("どうする？")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("マイリスト", my_list)
        if selection_input == "T":
            print("ゴミ箱", trash_list)
        if selection_input == "E":
            print("またね！")
            print("マイリスト：", my_list)
            break
    print("またね！")
    print("マイリスト", my_list)
    print("ゴミ箱", trash_list)

if gender_input == "男の子":
    for f in male_list:
        r = random.choice(male_list)
        print("名前：", " ".join(r[1:3]))
        selection_input = input("どうする？")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("マイリスト", my_list)
        if selection_input == "T":
            print("ゴミ箱", trash_list)
        if selection_input == "E":
            print("またね！")
            print("マイリスト", my_list)
            break
    print("またね！")
    print("マイリスト", my_list)
    print("ゴミ箱", trash_list)

if gender_input == "両方":
    for f in all_list:
        r = random.choice(all_list)
        print("名前：", " ".join(r[1:3]))
        selection_input = input("どうする？")
        if selection_input == "R":
            my_list.append(r)
        if selection_input == "L":
            trash_list.append(r)
        if selection_input == "M":
            print("マイリスト", my_list)
        if selection_input == "T":
            print("ゴミ箱", trash_list)
        if selection_input == "E":
            print("またね！")
            print("マイリスト", my_list)
            break
    print("またね！")
    print("マイリスト", my_list)
    print("ゴミ箱", trash_list)

#Export list to CSV
filename = str(user_name + ".csv")
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(my_list)