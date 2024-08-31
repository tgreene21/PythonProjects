from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#----------------------------- SEARCH WEBSITE ----------------------------------- #

def find_password():
    searched_result = website_entry.get()

    try:
        with open("data.json", mode="r") as file:
            #Read from the json file
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No file found")
    else:
        try:
            web_info = data[searched_result]
        except KeyError:
            messagebox.showinfo(title="Oops", message = "No details for the website exists")
        else:
            email = web_info["email"]
            password = web_info["password"]
            messagebox.showinfo(title = "Info", message = f"Here is your info: \nEmail: {email} \nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    new_data = {
        website_name: {
            "email": email_name,
            "password": password_name
        }
    }

    if len(website_name) == 0 or len(password_name) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading Old Data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode= "w") as file:
                json.dump(new_data, file, indent = 4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent = 4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 25, pady = 25)

canvas = Canvas(width =200, height= 200, highlightthickness=0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

#Labels
website_label = Label(text = "Website:")
email_label = Label(text = "Email/Username:")
password_label = Label(text = "Password:")

website_label.grid(row = 1, column = 0)
email_label.grid(row = 2, column = 0)
password_label.grid(row = 3, column = 0)

#Textboxes
website_entry = Entry(width = 32)
email_entry = Entry(width = 51)
password_entry = Entry(width = 32)

website_entry.grid(row = 1, column = 1)
email_entry.grid(row = 2, column = 1, columnspan = 2)
password_entry.grid(row = 3, column = 1)



website_entry.focus()
email_entry.insert(0, "your_email_here@gmail.com")

#Buttons
gen_pass_button = Button(text = "Generate Password", command= generate_password)
add_button = Button(width = 43, text = "Add", command = save_password)
search_button = Button(width = 15, text = "Search", command= find_password)

gen_pass_button.grid(row = 3, column = 2)
add_button.grid(row = 4, column = 1, columnspan = 2)
search_button.grid(row =1, column = 2)

window.mainloop()