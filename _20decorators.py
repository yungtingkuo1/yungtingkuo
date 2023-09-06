class Manager:
    def __init__(self):
        self.actions = {}
    
    def assign(self, name):
        def inner_function(func):
            self.function[name] = func

        return inner_function
        
    def execute(self, name, *args, **kwargs):
        return self.function[name](self,*args, *kwargs)
            
manager = Manager ()


@manager.assign("accounting")
def accounting():
    print("Welcome to our accounting system!")

while True:
    action = input("What action to do [sale, purchase or balance]")
    if action == "sale":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = float(input("Enter the product quantity: "))

        manager.execute(product_name, price, quantity)
        print(f"Sale: {product_name, price, quantity}")

    elif action == "purchase":
        product_name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = float(input("Enter the product quantity: "))
            
        manager.execute(product_name, price, quantity)
        print(f"Purchase: {product_name, price, quantity}")

    elif action == "balance":
        amount = float(input("Enter the amount to add (+) or subtract (-): "))
        
        manager.execute(amount)
        print(f"balance: {amount}")
    
    else:
        print("Exiting...")
        break




