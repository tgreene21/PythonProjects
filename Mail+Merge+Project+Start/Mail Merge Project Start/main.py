#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Get the list of names
with open("Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

#Remove Empty Line Characters
for i in range(0, len(name_list) - 1):
    name_list[i] = name_list[i].strip()

#Grab the sample letter
with open("Input/Letters/starting_letter.txt") as file:
    contents = file.read()

#For each name in the list, generate a file with their name instead of [name]
for name in name_list:
    with open(f"Output/ReadyToSend/letter_to_{name}", mode = "w") as file:
        new_contents = contents
        x = new_contents.replace("[name]", name)
        file.write(x)