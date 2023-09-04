import _9import1

file_name = input("Please provide a name of a file(include extension, i.e. .txt)")
file_name_account = input("Please provide a name of a file(include extension, i.e. .txt)")
file_name_history = input("Please provide a name of a file(include extension, i.e. .txt)")

inventory = _9import1.load_file(file_name, {})
account = _9import1.load_file(file_name_account, 0)
history = _9import1.load_file(file_name_history, [])

commend = ""

print("Availalbe commands: \n")
print("balance")
print("sale")
print("purchase")
print("account")
print("list")
print("warehouse") 
print("review")
print("end - end program. \n") 

while True:
    command = input("please enster a command:")

    if command =="balance":
            amount = float(input("Enter the amount to add (+) or subtract (-): "))
            if amount + account >= 0:
                account += amount
            else:
                print("Error! account can not be negative!")
                continue
        #an amount to add or subtract from the account.
    elif command =="sale":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = float(input("Enter the product quantity: "))
        if inventory.get(product_name, 0) < quantity:
                print(f"Not enought itmes: {product_name}")
                continue
        
        history.append([product_name,price, quantity]) 

        inventory[product_name] -= quantity
        account += quantity * price

        #update the account and warehouse accordingly. 
    elif command =="purchase":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = float(input("Enter the product quantity: "))
        
        if account >= quantity * price:
            history.append([product_name,price, quantity]) 
            inventory[product_name] -= quantity
            account += quantity * price
        else:
            print(f"Insufficient funds. Purchase cannot be completed.")
        # update the account and warehouse accordingly. the account balance is not negative after purchase
    elif command =="account":
            print(f"Account balance: {account}")
    elif command == "list":
        for event in history:
            print(event)   
        #total inventory in the warehouse along with product prices and quantities. 
    elif command == "warehouse":  
        product_name = input("Enter the product name: ")  
        product_quantity = inventory.get(product_name)
        for item, quantity in inventory:
            print(f"Product: {product_name}, Quantity: {product_quantity}")
         # Prompt for a product name and display its status in the warehouse.
    elif command == "review":
        review = []
        print("Provide from and to values")
        from_value = int(input("From:"))
        to_value = int(input("To:"))
        new_review = history[from_value:to_value]
        print(new_review)
        #Prompt for two indices 'from' and 'to', and display all recorded operations within that range.
        #If ‘from’ and ‘to’ are empty, display all recorder operations. 
    elif command =="end":
        print("End program.")
        _9import1.save_file(file_name, inventory)
        _9import1.save_file(file_name_account, account)
        _9import1.save_file(file_name_history, history)
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
            
