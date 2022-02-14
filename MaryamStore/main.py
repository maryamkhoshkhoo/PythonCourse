from pyfiglet import Figlet
import qrcode

address = 'database.txt'

def show_menu():
    print("1-Add product")
    print("2-Edit Product")
    print("3-Delete Poduct")
    print("4-Search")
    print("5-Show List")
    print("6-Buy")
    print("7-exit") 
    print("8-save")
    print("9-qrcode")


def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])



def load():
    print("Loading...")
    myfile = open("database.txt", "r")
    data = myfile.read()
    print(data)
    products_list= data.split("\n") 


    for i in range(len(products_list)):
        product_info = products_list[i].split(",")
        mydict = {}
        mydict["id"] = product_info[0]
        mydict["name"] = product_info[1]
        mydict["price"] = product_info[2]
        mydict["count"] = product_info[3] 
        PRODUCTS.append(mydict)
    print("Welcome")


PRODUCTS = []
load()

f = Figlet(font="standard")
print(f.renderText("Maryam Store"))


def add_product():
    id = int(input("Please enter id:"))
    name = input("Please enter name:")
    price = float(input("Please enter price:"))
    count = int(input("Please enter count:"))
    PRODUCTS.append({"id": id, "name": name, "price": price, "count":count})
    print("New product added!")


def search():
    user_product = input("Please enter id or name:")
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]["name"] == user_product or PRODUCTS[i]["id"]== user_product:
            print(PRODUCTS[i]) 
            break
        else:
            print("Not Found! Sorry!")


def delete_product():
    code = input("You can delete product by their code:")
    del PRODUCTS[code]
    print("Done!")
   

def edit_product():
    name = input("Enter name of product that you want to edit:")
    for i in range(len(PRODUCTS)):
        if name == PRODUCTS[i]["name"]:
            PRODUCTS[i]["name"] = input("new name:")
            PRODUCTS[i]["price"] = input("new price:")
            PRODUCTS[i]["count"] = input("new count:")
            break
        else:
            print("Not exists")


def save():
    database_file = open(address, "w")
    for i in range(len(PRODUCTS)):
        save_dict = PRODUCTS[i]
        id = save_dict["id"]
        name = save_dict["name"]
        price = save_dict["price"]
        count = save_dict["count"]
        database_file.write(id,name,price,count)

    database_file.close()
    print("Your changes saved") 


def show_qrcode():
    productqr=input("Enter the id of the product:")
    for i in range(len(PRODUCTS)):
        if productqr == PRODUCTS[i]["id"]:
            myqr = qrcode.make(PRODUCTS[i])
            myqr.save(f"qrcode{i}.png")
            print("qrcode created")
            break



show_menu() 

choice = int(input("Please select a number:")) 

if choice == 1:
    add_product()

elif choice == 2:
    edit_product()

elif choice == 3:
    delete_product()

elif choice == 4:
    search()

elif choice == 5:
    show_list() 

elif choice == 6:
    pass

elif choice == 7:
    pass

elif choice == 8:
    save() 

elif choice == 8:
    show_qrcode()    