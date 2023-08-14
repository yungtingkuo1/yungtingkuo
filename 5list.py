print("Availalbe commands: \n")
print("balance")
print("sale")
print("purchase")
print("account")
print("list")
print("warehouse") 
print("review")
print("end - end program. \n") 

account = []
inventory = []
list = []


while True:
    command = input("please enster a command:")

    if command =="balance":
            amount = float(input("Enter the amount to add (+) or subtract (-): "))
            if amount >= 0:
                account.append(amount)
            else:
                if abs(amount) <= account.balance:
                    account.append(amount)
        #an amount to add or subtract from the account.
    elif command =="sale":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        list.append(product_name,price, quantity)      
        print("Your current sale are:", end=" ")
        for product_name,price, quantity in list:
            print(product_name,price, quantity + ",", end="")  
        #update the account and warehouse accordingly. update ammount[], inventory[] 
    elif command =="purchase":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        if product is None:
                product = (product_name, price, quantity)
                inventory.add_product(product)
        print("Your current purchase are:", end=" ")
        for product_name,price, quantity in inventory:
            print(product_name,price, quantity + ",", end="")
        # update the account and warehouse accordingly. the account balance is not negative after purchase
    elif command =="account":
            print(f"Account balance: {account.balance}")
    elif command == "list":
        for event in list:
            print(event)   
        #total inventory in the warehouse along with product prices and quantities. 
    elif command == "warehouse":  
        product_name = input("Enter the product name: ")  
        product = inventory.get_product(product_name)
        for item, quantity in inventory:
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
         # Prompt for a product name and display its status in the warehouse.
    elif command == "review":
        review = []
        print("Provide from and to values")
        from_value = int(input("From:"))
        to_value = int(input("To:"))
        new_review = review[from_value:to_value]
        print(new_review)
        #Prompt for two indices 'from' and 'to', and display all recorded operations within that range.
        #If ‘from’ and ‘to’ are empty, display all recorder operations. 
    elif command =="end":
        print("End program.")
        break
    else: 
        print("Availalbe commands: \n")
        print("balance")
        print("sale")
        print("purchase")
        print("account")
        print("list")
        print("warehouse") 
        print("review")
        print("end - end program. \n") 
            


