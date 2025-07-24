# Password Generator and Strength Evaluator

## Overview
This project is a user-friendly Password Generator and Strength Evaluator with a graphical user interface (GUI) built using Python's Tkinter library. It allows users to generate secure passwords based on customizable criteria, assess their strength, and receive suggestions for improvement. Additional features include copying passwords to the clipboard and saving them to a file.

## Features
- **Customizable Password Generation:**
  - Choose password length
  - Optionally include uppercase letters, digits, and special characters
- **Password Strength Assessment:**
  - Evaluates the strength of the generated password
  - Provides a score and improvement suggestions
- **User-Friendly GUI:**
  - Simple and intuitive interface using Tkinter
  - Personalized greeting with your name
- **Extra Functions:**
  - Copy generated password to clipboard
  - Save password to a file named `<your_name>_password.txt`
  - Clear generated data and suggestions
 
## Video

https://github.com/user-attachments/assets/5d8cef3f-e4c6-4c9d-9619-309581bfc50d



## Requirements
- Python 3.x
- Tkinter (usually included with standard Python installations)

## How to Run
1. **Clone or Download the Repository**
2. **Install Python 3.x** if not already installed.
3. **Run the GUI Application:**
   ```bash
   python pgmwithGUI.py
   ```
   This will launch the Password Generator GUI.

## Usage
1. Enter your name in the provided field.
2. Specify the desired password length.
3. Select options to include uppercase letters, digits, and/or special characters.
4. Click **Generate Password** to create a password.
5. View the generated password, its strength, and suggestions for improvement.
6. Use the **Copy to Clipboard** button to copy the password.
7. Use the **Save to File** button to save the password to a file.
8. Use the **Clear Generated** button to reset the fields.

## File Structure
- `pgmwithGUI.py` - Main GUI application
- `password_generator.py` - Password generation logic
- `strength_assessment.py` - Password strength evaluation
- `improvement_suggestions.py` - Suggestions for improving password strength
- `username_input_module.py` - Handles username input in the GUI
- `save_module.py` - Handles saving passwords to a file
- `clear_module.py` - Clears generated data in the GUI
- `copy_module.py` - Handles copying passwords to clipboard

## License
This project is for educational and personal use. 
