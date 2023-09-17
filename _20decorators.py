import _9import1

class Manager:
    def __init__(self):
        self.actions = {}
    
    def load_data(self):
        self.file_name = input("Please provide a name of a file(include extension, i.e. .txt)")
        self.file_name_account = input("Please provide a name of a file(include extension, i.e. .txt)")
        self.file_name_history = input("Please provide a name of a file(include extension, i.e. .txt)")

        self.inventory = _9import1.load_file(self.file_name, {})
        self.account = _9import1.load_file(self.file_name_account, 0)
        self.history = _9import1.load_file(self.file_name_history, [])
    
    def save_data(self):
        _9import1.save_file(self.file_name, self.inventory)
        _9import1.save_file(self.file_name_account, self.account)
        _9import1.save_file(self.file_name_history, self.history)

  
    def assign(self, name):
        def inner_function(func):
            self.actions[name] = func

        return inner_function
        
    def execute(self, name, *args, **kwargs):
        return self.actions[name](self,*args, *kwargs)
            
manager = Manager ()
manager.load_data()


@manager.assign("accounting")
def accounting(manager):
    print("Welcome to our accounting system!")

@manager.assign("sale")
def sale(manager):
    product_name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = float(input("Enter the product quantity: "))
    if manager.inventory.get(product_name, 0) < quantity:
        print(f"Not enought itmes: {product_name}")
        return
            
    manager.history.append([product_name,price, quantity]) 
    manager.inventory[product_name] -= quantity
    manager.account += quantity * price

@manager.assign("purchase")
def purchase(manager):
    product_name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    quantity = float(input("Enter the product quantity: "))
        
    if manager.account >= quantity * price:
        manager.history.append([product_name,price, quantity]) 
        manager.inventory[product_name] -= quantity
        manager.account += quantity * price
    else:
        print(f"Insufficient funds. Purchase cannot be completed.")

@manager.assign("balance")
def balance(manager):
    amount = float(input("Enter the amount to add (+) or subtract (-): "))
    if manager.amount + manager.account >= 0:
        manager.account += amount
    else:
        print("Error! account can not be negative!")

@manager.assign("review")
def review(manager):
    review = []
    print("Provide from and to values")
    from_value = int(input("From:"))
    to_value = int(input("To:"))
    new_review = manager.history[from_value:to_value]
    print(new_review)


while True:
    action = input("What action to do [sale, purchase or balance]")
    if action == "sale":
        manager.execute("sale")
    elif action == "purchase":        
        manager.execute("purchase")
    elif action == "balance":
        manager.execute("balance")
    else:
        print("Exiting...")
        manager.save_data()
        break
