from tkinter import *
import random

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TIMER = 3000 #3 Seconds
flashcard_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    flashcard_dict = original_data.to_dict(orient = "records")
else:
    flashcard_dict = data.to_dict(orient="records")
finally:
    current_word = random.choice(flashcard_dict)

# ------------------------------------ Create New Flash Cards ---------------------------#

def create_flashcard():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    current_word = random.choice(flashcard_dict)
    canvas.itemconfig(title_text,text = "French", fill = "black")
    canvas.itemconfig(word_text, text = current_word["French"], fill = "black")
    flip_timer = window.after(TIMER, func=flip)


# -------------------------------------- Flip the card ----------------------------------#

def flip():
    global current_word
    canvas.itemconfig(canvas_image, image = card_back_img)
    canvas.itemconfig(title_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, text = current_word["English"], fill = "white")


# ------------------------------------ Words to Learn/Save Progress -------------------------#

def is_known():
    global current_word, flashcard_dict
    flashcard_dict.remove(current_word)

    data = pandas.DataFrame(flashcard_dict)
    data.to_csv("data/words_to_learn.csv", index = False)


    create_flashcard()


# ----------------------------------------- UI SETUP -------------------------------------#

window = Tk()
window.title("Flashcards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(TIMER, func=flip)

canvas = Canvas(width =800, height= 526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file= "images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text = "Title", fill = "black", font = (FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text = "Word", fill = "black", font = (FONT_NAME, 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)


#Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command= create_flashcard)
wrong_button.grid(row = 1, column = 0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command = is_known)
right_button.grid(row = 1, column = 1)


create_flashcard()


window.mainloop()

