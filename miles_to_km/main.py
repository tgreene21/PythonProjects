from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height=300)
window.config(padx = 20, pady = 20)

def convert():
    miles = my_text.get()
    km = float(miles) * 1.609
    result_label.config(text = round(km))

# 3 labels

miles_label = Label(text = "Miles")
is_equal_to_label = Label(text = "is equal to")
result_label = Label(text = "0")
km_label = Label(text = "Km")

miles_label.grid(row = 0, column = 2)
is_equal_to_label.grid(row = 1, column = 0)
result_label.grid(row = 1, column = 1)
km_label.grid(row = 1, column = 2)


# 1 text box

my_text = Entry()
my_text.grid(row = 0, column = 1)

# 1 button

calculate_button = Button(text = "Calculate", command = convert)
calculate_button.grid(row = 2, column = 1)

window.mainloop()