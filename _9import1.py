from ast import literal_eval

def load_file(file_name, default_return):
    try:
        with open(file_name, 'r') as file:
            return literal_eval(file.read())
    except FileNotFoundError:
        print("File does not exist!Creating new file...")
        return default_return
    
def save_file(file_name, value):
    with open(file_name, 'w') as file:
        file.write(str(value))


