import tkinter as tk
from tkinter import ttk

class UsernameModule:
    def __init__(self, root, on_username_submit):
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.name_var = tk.StringVar()
        self.name_label = ttk.Label(self.frame, text="Enter your name:")
        self.name_entry = ttk.Entry(self.frame, textvariable=self.name_var)
        
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def get_username(self):
        return self.name_var.get()

