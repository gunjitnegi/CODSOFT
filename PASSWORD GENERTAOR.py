import random
import string
import tkinter as tk

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            password_label.config(text="Password length should be at least 6.")
            return
        
        # Define the character sets for the password
        all_characters = string.ascii_letters + string.digits + string.punctuation

        # Randomly generate the password
        password = ''.join(random.choice(all_characters) for _ in range(length))

        password_label.config(text=f"Generated Password: {password}")

    except ValueError:
        password_label.config(text="Please enter a valid number for the length.")

# Set up the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("600x400")  # Increased window size to 600x400
app.resizable(False, False)  # Disable resizing
app.configure(bg="#E0E0E0")

# Title label
title_label = tk.Label(app, text="Password Generator", font=("Arial", 18, "bold"), bg="#E0E0E0", fg="#333333")
title_label.pack(pady=30)

# Length input label and entry
length_label = tk.Label(app, text="Enter password length:", font=("Arial", 12), bg="#E0E0E0", fg="#333333")
length_label.pack(pady=10)

entry_length = tk.Entry(app, font=("Arial", 14), width=15)
entry_length.pack(pady=5)

# Generate password button
generate_button = tk.Button(app, text="Generate Password", font=("Arial", 14), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=20)

# Display generated password
password_label = tk.Label(app, text="Generated Password: ", font=("Arial", 14), bg="#E0E0E0", fg="#333333")
password_label.pack(pady=20)

# Run the application
app.mainloop()
