# copy_module.py
import tkinter as tk

def copy_to_clipboard(password_var, root):
    # Use the built-in Tkinter clipboard
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    return "Password copied to clipboard."
