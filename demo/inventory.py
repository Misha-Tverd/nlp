import os
import json


with open("goods.json", "r") as f:
    if os.path.getsize("goods.json") > 0:
        goods = json.load(f)
        print(goods)

list_item = """ 
    1. Add goods.
    2. Increase quantity.
    3. Decrease quantity.
    4. Show entire inventory"""     



def add_goods():
    input_goods = {}
    input_goods = {input("Add new goods: ")}
    print(type(input_goods))
    with open("goods.json", "r+") as f:
        f = json.load(f)
        f.append(input_goods)
        print(f"New goods added")
        menu = 5
    return menu 


menu = int(input(f"Select a menu item using the number key. {list_item}\nSelect a menu item: "))
while True:
    
    if menu == 1:
        add_goods()
    elif menu == 2:
        increase_quantity()
    elif menu == 3:
        decrease_quantity()
    elif menu == 4:
        show_entire_inventory()
    elif menu == 5:
        break
    else:
        print("choose correct number: ")
        menu  = int(input("Select a menu item: "))
