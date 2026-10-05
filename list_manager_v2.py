item_list = [ ]

while True:
    add_list = input("What do you want to add to the list? press 1 if theres nothing else to add: ")
    
    if add_list == "1":
        first_question = input("Press 2 to show the position of every item, 1 for a position of a item, press 0 for no item: ")
        
        if first_question == "2":
            position_number_two = -1
            
            for items in item_list:
                position_number_two += 1
                print(f"{items} is in the position {position_number_two} in the list!")
            
            break
        
        if first_question == "1":
            try:
                second_question = input("Inform the item and i will inform its position in the list!: ")
                position_number_one = item_list.index(second_question)
            
                print(f"{second_question} is in the position {position_number_one} in the list!")
            except ValueError:
                print("This Item is not in the list!")
            break

        if first_question == "0":
            for items in item_list:
                print(items)
            
            print("Those are the Items added to the list!")
            break
    
    item_list.append(add_list)
