products = []
def read_file():
    f = open("database.txt", "r")
    for line in f:
        result = line.split(", ")
        my_dictionary = {"id": result[0], "name": result[1], "price": result[2], "amount": result[3]}
        products.append(my_dictionary)
        print(result)

def show_menu():
    print("1- Add")
    print("2- remove")
    print("3- search")
    print("4- edit")
    print("5- show list")
    print("6- Buy")
    print("7- exit")

def add():
    id = input("id: ")
    name = input("name: ")
    price = input("price: ")
    amount = input("amount: ")
    new_dic = {"id":id, "name":name, "price":price, "amount":amount}
    products.append(new_dic)
    print(products)

def remove():
    key = input("Enter the ID or the name of the item: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            products.remove(key)
            break
    else:
        print("Not found")

def search():
    key = input("Enter your key: ")
    for product in products:
        if product["id"] == key or product["name"] == key:
            print(product)
            break
    else:
        print("Not found")

def edit():
    read_file()
    key = int(input("Enter the ID of the item: "))
    for product in products:
        if product ["id"] == key:
            field = int(input("""Please enter the number of the field you want to edit: 
            1- Name
            2- Price
            3- Count"""))
            if field == 1:
                namech = input("please enter the new name: ")
                product["name"] = namech
                print("changes successfully made.")
                break
            if field == 2:
                pricech = input("please enter the new price: ")
                products["price"] = pricech
                print("changes successfully made.")
                break
            if field == 3:
                countch = input("please enter the new count: ")
                products["count"] = countch
                print("changes successfully made.")
                break
        else:
            print("Not found")

def showlist():
    print("id\tname\tprice\tamount")
    for product in products:
        print(product["id"],"\t", product["name"],"\t",  product["price"],"\t",  product["amount"])

def buy():
    shop = []
    while True:
        ID = input("Please enter the product ID: ")
        if not ID in products:
            print("ID not found.")
            exit()
        if ID in products:
            amount = int(input("Enter the amount of the item: "))
            shop.append(ID*amount)


def save_to_database():
    save = input("Would you like to save the changes?(yes/no): ")
    if save == "yes":
        open("database.txt", "w")
        print(products)
    if save == "no":
        exit()
    

read_file()
while True:
    show_menu()
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        add() 
    elif user_choice == 2:
        remove()
    elif user_choice == 3:
        search()
    elif user_choice == 4:
        edit()
    elif user_choice == 5:
        showlist()
    elif user_choice == 6:
        buy()
    elif user_choice == 7:
        save_to_database()
        exit(0)
    else:
        print("Please select a number: ")