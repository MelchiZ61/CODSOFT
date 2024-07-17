# A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a
# password generator application using Python, allowing users to specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

from tkinter import *
from tkinter import messagebox
from random import randint

#------------------------------------------
#------------------------------------------
def passgen():
    pw_entry.delete(0, END)
    try:
        pw_length = int(my_entry.get())
        if pw_length <= 0:
            disp_error = "Please enter a valid length"
            my_entry.delete(0, END)
            messagebox.showerror("Error", disp_error)
        else:
            my_password = ''
            for x in range(pw_length):
                my_password += chr(randint(33, 126))

            pw_entry.insert(0, my_password)
    except ValueError:
        disp_error = "Please enter a valid length"
        my_entry.delete(0, END)
        messagebox.showerror("Error", disp_error)

#------------------------------------------
#------------------------------------------
def copier():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Info", "Password Copied to Clipboard")

#------------------------------------------
#------------------------------------------
def clearing():
    my_entry.delete(0, END)
    pw_entry.delete(0, END)

#------------------------------------------
#------------------------------------------
root = Tk()
root.title("Task 3: Password Generator Program")
root.geometry("800x370")
root.configure(background='#16CADC')

# LabelFrame for password size
lf = LabelFrame(root, text="Enter Password Size", font=("Times New Roman", 16), background='#d9d9d9', padx=20, pady=20)
lf.pack(pady=20)

# Entry for password size
my_entry = Entry(lf, font=("Helvetica", 24), width=20)
my_entry.pack(pady=10)

pw_frame = Frame(root)
pw_frame.pack(pady=20)

pw_scrollbar = Scrollbar(pw_frame, orient=HORIZONTAL)
pw_scrollbar.pack(side=BOTTOM, fill=X)

pw_entry = Entry(pw_frame, font=("Helvetica", 24), width=39, xscrollcommand=pw_scrollbar.set)
pw_entry.pack(side=LEFT)

pw_scrollbar.config(command=pw_entry.xview)

# Frame for buttons
my_frame = Frame(root, background='#f0f0f0')
my_frame.pack(pady=20)

# Generate Password button
my_button = Button(my_frame, text="Generate Password", font=("Helvetica", 14), command=passgen, background='#4caf50', fg='white', padx=10, pady=5)
my_button.grid(row=0, column=0, padx=10)

# Copy Password button
clip_button = Button(my_frame, text="Copy Password", font=("Helvetica", 14), command=copier, background='#2196f3', fg='white', padx=10, pady=5)
clip_button.grid(row=0, column=1, padx=10)

# Clear Field button
clear_field = Button(my_frame, text="Clear Field", font=("Helvetica", 14), command=clearing, background='#f44336', fg='white', padx=10, pady=5)
clear_field.grid(row=0, column=2, padx=10)

root.mainloop()
#------------------------------------------
#------------------------------------------