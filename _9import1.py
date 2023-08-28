from ast import literal_eval

def load_file(file_name, default_return):
    try:
        with open(file_name, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("File does not exist!Creating new file...")
        return default_return
    
def load_file(file_name_account, default_return):
    try:
        with open(file_name_account, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("File does not exist!Creating new file...")
        return default_return

def load_file(file_name_history, default_return):
    try:
        with open(file_name_history, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("File does not exist!Creating new file...")
        return default_return

def save_file(file_name, value):
    with open(file_name, 'w') as file:
        file.write(str(value))

def save_file(file_name_account, value):
    with open(file_name_account, 'w') as file:
        file.write(float(value))

def save_file(file_name_history, value):
    with open(file_name_history, 'w') as file:
        file.write(str(value))

