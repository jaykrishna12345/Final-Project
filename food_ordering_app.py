import re
import json
class Restaurant:

    def __init__(self, name):
        self.rest_name = name
        self.food = {}
        self.food_ID = len(self.food) + 1
        self.user_details = {}
        self.ordered_item = []



# Admin_Part
    def add_food_item(self):
        try:
            name = input("Enter the food name : ")
            quantity = float(input("Enter the quantity : "))
            price = float(input("Enter the price : "))
            discount = float(input("Enter the discount : "))
            stock = float(input("Enter the available stock : "))
            food_item = {"Name": name, "Quantity": quantity, "Price": price, "Discount": discount, "Stock": stock}
            self.food_ID = len(self.food) + 1
            self.food[self.food_ID] = food_item
            print("\n<<<<<< Food Item added successfully >>>>>>\n")
            print("Newly Added items :", self.food, "\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")

    def edit_food_item(self):
        try:
            
            x = int(input("Enter the Food ID you want to update : \n"))
            
            if x in self.food.keys():
                print("\n1) Update Food Name")
                print("2) Update Quanity")
                print("3) Update Price")
                print("4) Update Discount")
                print("5) Update Stock\n")
                
                y = input("Enter Your Choice(Enter the number only) : ")
                
                if y == "1":
                    self.food[x]["Name"] = input("Updated Food name : ")
                    print("\n<<<<<< Successfully Updated Food Name >>>>>>\n")
                elif y == "2":
                    self.food[x]["Quantity"] = float(input("Updated Quantity is : "))
                    print("\n<<<<<< Successfully Updated The Quantity >>>>>>\n")
                elif y == "3":
                    self.food[x]["Price"] = float(input("Updated Price is : "))
                    print("\n<<<<<< Successfully Updated The Price >>>>>>\n")
                elif y == "4":
                    self.food[x]["Discount"] = float(input("Updated Discount is : "))
                    print("\n<<<<<< successfully Updated Discount Amount >>>>>>\n")
                elif y == "5":
                    self.food[x]["Stock"] = float(input("Updated Stock is : "))
                    print("\n<<<<<< Successfully Updated The Stock >>>>>>\n")
                else:
                    print("\n!! Sorry Invalid Choice !!\n")
            
            else:
                print("\n!! Incorrect Food ID !!\n")
                print("\n!! Please Try Again !!\n")
        
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")

    def view_food_item(self):
        print("List of Food Items : \n")
        if len(self.food) != 0:
            for i in self.food:
                print(f"Food Id : {i}")
                for j in self.food[i]:
                    print(j, ":", self.food[i][j])
                print()
        else:
            print("!! Sorry No Food Items is Added !!\n")

    def delete_food_item(self):
        try:
            
            x = int(input("Enter the Food ID : "))
            if x in self.food.keys():
                del self.food[x]
                print("\n!! Food item deleted successfully !!\n")
                print("Updated Food List : \n",self.food)
            else:
                print("\n!! Incorrect Food ID !!\n ")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n")

# User_Part

    def user_register(self):
        try:
            while True:
                
                print("<<< Please eneter Email Id like this 'abc@gmail.com' >>>")
                email = input("Enter your email id : ")
                print("<<< Password should contain atleast 1 capital,1 small,1 special char, & atleast 8-16 char long >>>")
                password = input("Enter your password : ")
                
                res1 = re.findall("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",password)
                if res1:
                    print("Strong password")
                else:
                    print("Password is too weak")
                    break
                user_name = input("Enter your full name : ")
                phone_no = int(input("Enter your 10 digit phone number : "))

                address = input("Enter your address : ")
                self.user_details = {"User Name": user_name, "Phone No.": phone_no, "Email ID": email,
                                     "Password": password, "Address": address}
                print("\n<<<<<< Your Account is Created Successfully >>>>>>\n")
                print(f"Welcome TO {self.rest_name} Restaurant\n")
                print("User Details : ")
                for i in self.user_details:
                    print(i, ":", self.user_details[i])
                break

        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ")

    def user_login(self):
        try:
            while True:
                print(f"<_<_< Welcome TO {self.rest_name} Restaurant >_>_>\n")
                email = input("Enter Your Email ID : ")
                pas = input("Enter Your Password : ")
                if len(self.user_details) != 0:
                    if email == self.user_details["Email ID"] and pas == self.user_details["Password"]:
                        print("\n<<<<<< Login successfully >>>>>>")
                        
                        
                        while True:
                            print(f"\n_-_-_-_-_-__Hello__-_-_-_-_-_")
                            print("\nEnter the Below Options")
                            print("\n1) Place New Order")
                            print("2) Check Order History")
                            print("3) Update Your Profile Details")
                            print("4) Exit\n")
                            z = input("Please Input your Choice : ")
                            if z == "1":
                                self.place_order()
                            elif z == "2":
                                self.ordered_history()
                            elif z == "3":
                                self.update_details()
                            elif z == "4":
                                break
                            else:
                                print("invalid Number")
                    else:
                        print("\n!! Incorrect Email or Password!!\n")
                else:
                    print("\n! There is no Account with this Email ID !\n\n!! Please Create Your Account First!!\n")
                    break
                break
        except Exception as e:
            print("\n!! Something went wrong please try again !!")

    def place_order(self):
        try:
            if len(self.food) != 0:
                menu = []
                for items in self.food:
                    menu.append([self.food[items]["Name"], self.food[items]["Quantity"], self.food[items]["Price"]])
                for i in menu:
                    print(i)
                while True:
                    print("\nEnter 1 to Place the Order")
                    print("\nEnter 2 to Exit\n")
                    x = input()
                    if x == "1":
                        print("Enter the Food number You want to ordered separated by comma")
                        y = input().split(",")
                        for i in y:
                            z = int(i)
                            if z <= len(menu):
                                self.ordered_item.append(menu[z - 1])
                            else:
                                print("We Don't have this Food Item : ", z)
                        print("List of food item you selected : \n")
                        for j in self.ordered_item:
                            print(j)
                    elif x == "2":
                        break
                    else:
                        print("!! Invalid Number !!\n")
            else:
                print("\n!! Sorry! No Food Items are available Now !!\n")

        except Exception as e:
            print("\n!! Something went wrong try again !!")

    def ordered_history(self):
        print("\nList of Previous ordered : ")
        for i in self.ordered_item:
            print(i)

    def update_details(self):
        try:
            while True:
                print("<<<<<< Select Below Options to Update Your Profile Details >>>>>>\n")
                print("\n1) Name")
                print("2) Phone number")
                print("3) Email ID")
                print("4) Password")
                print("5) Address")
                print("6) Exit\n")

                x = input("Please Input your Choice : ")
                if x == "1":
                    self.user_details["User Name"] = input("Enter your updated full name : ")
                    print("\n<<<<<< Name Updated Successfully >>>>>>\n")
                elif x == "2":
                    self.user_details["Phone No."] = int(input("Enter your updated 10 digit phone number : "))
                    print("\n<<<<<< Phone No. Updated Successfully >>>>>>\n")
                elif x == "3":
                    self.user_details["Email_ID"] = input("Enter your updated email id : ")
                    print("\n<<<<<< Email Updated Successfully >>>>>>")

                elif x == "4":
                    self.user_details["Password"] = input("Enter your updated password : ")
                    print("\n!<<<<<< Password Updated Successfully >>>>>>\n")

                elif x == "5":
                    self.user_details["Address"] = input("Enter your updated address with area PIN code ")
                    print("\n<<<<<< Address Updated Successfully >>>>>>\n")

                elif x == "6":
                    break
                else:
                    print("\n!! Invalid Number Entered !!\n")

                if x in ["1", "2", "3", '4', "5"]:
                    for i in self.user_details:
                        print(i, ":", self.user_details[i])
                else:
                    print("\n!! Please Enter correct Input !!\n")
        except Exception as e:
            print("\n!! Something went wrong please try again !!\n ")

 
# Main_Part

def main():
    try:
        obj = Restaurant("The Viper's Kitchen")
        print("\n||||/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||||\n")
        print(f">>>>>>>>>>>>  Welcome To {obj.rest_name}  <<<<<<<<<<<<<\n")
        print("               ** The Real Taste is Here **               \n")
        print("||||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/||||")

        while True:
            print("\n1) Admin")
            print("2) User")
            print("3) Exit\n")
            x = input("Please Input your Choice : ")
            if x == "1":
                # obj.check_admin()
                read = open("admin.json","r")
                data = json.load(read)
                print("^^^^ For Admin ID and Password Please refer to the 'admin.json' file ^^^^")
                name = input("Enter Admin name : ")
                password = input("Enter Admin Password : ")
        
                if name == data["name"] and password == data["password"]:
                    print("\n<<<<<< Loged in Succesfully >>>>>>")

                    while True:
                        print("\n1) Add New Food Items")
                        print("2) Edit Food Items")
                        print("3) View Food Items")
                        print("4) Delete Food Items")
                        print("5) Exit\n")
                        y = input("Please Input your Choice : ")
                        if y == "1":
                            obj.add_food_item()
                        elif y == "2":
                            obj.edit_food_item()
                        elif y == "3":
                            obj.view_food_item()
                        elif y == "4":
                            obj.delete_food_item()
                        elif y == "5":
                            break
                        else:
                            print("Invalid Number")
            elif x == "2":
                while True:
                    print("\nEnter the Below Options")
                    print("\n1) Register")
                    print("2) Login")
                    print("3) Exit\n")
                    y = input("Please Input your Choice : ")
                    if y == "1":
                        obj.user_register()
                    elif y == "2":
                        obj.user_login()
                    elif y == "3":
                        break
                    else:
                        print("\nInvalid Number ")
            elif x == "3":
                print("\n||||/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||||")
                print("\n        >>>>>>>>>>>>>>>>  Thank You  <<<<<<<<<<<<<<<<<")
                print("        >>>>>>>>>>>>  Please Visit Again  <<<<<<<<<<<<\n")
                print("||||/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||||\n")
                break
            else:
                print("Invalid Number")
    except Exception as e:
        print("something went wrong please give input carefully")

# Calling_Main_Function

if __name__ == '__main__':
    main() 