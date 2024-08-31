
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

######################################################################################################################

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {}

for (index, row) in nato_df.iterrows():
    nato_dict[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    name = input("What is your name?").upper()

    try:
        returned_list = [nato_dict[c] for c in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(returned_list)

generate_phonetic()


