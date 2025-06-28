import random
import string
import tkinter as tk
from tkinter import ttk
from password_generator import *
from improvement_suggestions import *
from strength_assessment import *
from username_input_module import UsernameModule
from save_module import save_to_file
from clear_module import clear_generated_vars
from copy_module import copy_to_clipboard
 

def generate_and_display_password():
    user_name = username_module.get_username()

    length = int(length_var.get())
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    password = generate_password(user_name,length, include_uppercase, include_digits, include_special_chars)
    password_var.set(f"Generated Password: {password}")

    strength = check_strength(password)
    strength_var.set(f"Password Strength: {strength}/3\n\nSuggestions:  - ")

    if strength < 4:
        suggestions = suggest_improvements(password, strength)
        suggestions_var.set("\n".join(suggestions))
    else:
        suggestions_var.set("")

    greeting_var.set(f"Hello, {user_name}!")

def save_to_file_wrapper():
    message_var.set(save_to_file(name_var.get(), password_var.get()))

# Function to clear the generated password and suggestions
def clear_generated_wrapper():
    message_var.set(clear_generated_vars([password_var, suggestions_var, name_var, length_var ,strength_var,greeting_var, message_var]))

def copy_to_clipboard_wrapper():
    result = copy_to_clipboard(password_var, root)
    message_var.set(result)

# GUI setup
root = tk.Tk()
root.title("Password Generator and Strength Evaluator")

# Variables

name_var = tk.StringVar()
length_var = tk.StringVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()
password_var = tk.StringVar()
strength_var = tk.StringVar()
suggestions_var = tk.StringVar()
greeting_var = tk.StringVar()
message_var = tk.StringVar()

username_module = UsernameModule(root, generate_and_display_password)

# Widgets
length_label = ttk.Label(root, text="Enter the desired length of the password:")
length_entry = ttk.Entry(root, textvariable=length_var)
uppercase_check = ttk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
digits_check = ttk.Checkbutton(root, text="Include digits", variable=digits_var)
special_chars_check = ttk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
generate_button = ttk.Button(root, text="Generate Password", command=generate_and_display_password)
password_label = ttk.Label(root, textvariable=password_var)
strength_label = ttk.Label(root, textvariable=strength_var)
suggestions_label = ttk.Label(root, textvariable=suggestions_var)
greeting_label = ttk.Label(root, textvariable=greeting_var)
copy_label = ttk.Label(root, text="  EXTRA FUNCTIONS :- ")
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard_wrapper)
save_button = ttk.Button(root, text="Save to File", command=save_to_file_wrapper)
clear_button = ttk.Button(root, text="Clear Generated", command=clear_generated_wrapper)
message_label = ttk.Label(root, textvariable=message_var)

# Layout
length_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
length_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
uppercase_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")
digits_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")
special_chars_check.grid(row=4, column=0, padx=10, pady=5, sticky="w")
generate_button.grid(row=5, column=0, columnspan=2, pady=10)
password_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="w")
strength_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5, sticky="w")
suggestions_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="w")
greeting_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")
copy_button.grid(row=6, column=0, columnspan=2)
save_button.grid(row=6, column=1, columnspan=1)
clear_button.grid(row=6, column=2, columnspan=3)
message_label.grid(row=13, column=0, pady=5)
copy_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")


root.mainloop()
