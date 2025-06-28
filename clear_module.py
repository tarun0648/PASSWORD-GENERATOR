# clear_module.py

def clear_generated_vars(variables):
    for var in variables:
        var.set("")
    return "Generated password and suggestions cleared."

