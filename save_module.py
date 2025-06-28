# save_module.py

def save_to_file(user_name, password):
    file_name = f"{user_name}_password.txt"
    with open(file_name, 'w') as file:
        file.write(password)
    return f"Password saved to {file_name}"

