list = [ ]

while True:
    question_add = input("Inform what you want to add to the list, press 1 to stop!")
    if question_add == "1":
        break
    list.append(question_add)

print(list)