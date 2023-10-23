# Importing necessary libraries for password generation and GUI creation
import random
import string
import tkinter as tk

# Function to generate and display a random password of user-specified length
def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    result_label.config(text=f"Generated Password: {password}")

# Initializing the Tkinter window
window = tk.Tk()

# Setting the title of the window to "Password-Generator"
window.title("Password-Generator")

# Creating a label for the password-length in the window
length_label = tk.Label(window, text="Password-Length:",font=('Consolas',14,'bold'))
length_label.pack(pady=(20,0))
length_entry = tk.Entry(window)
length_entry.pack(pady=(0,20))

# Create button for generating-password!
generate_button = tk.Button(window, text="Generate-Password", command=generate_password,bg='blue', fg='black', font=('Consolas', 14, 'bold'), bd=5)
generate_button.pack(pady=(0,10))

# Creating and packing a label in the window to display the result
result_label = tk.Label(window, font=("Consolas", 14), wraplength=300)
result_label.pack()

# Run the application
window.mainloop()
