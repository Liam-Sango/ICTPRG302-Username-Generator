import secrets
import string

#Reads names from an input file
def read_input_file(file_path):
    name_list = []

    with open(file_path) as input_file:
        for file_line in input_file:
            count = file_line.count(" ")
            if count >= 2:
                break
            else:
                name_list.append(file_line.strip())  # strip() to remove trailing newline
    
    return name_list


#Splits a list of full names into two indivdual lists of names.
def split_full_names(full_names):
    first_names = []
    surnames = []
    for name in full_names:
        names_parts = name.split(" ", 1)
        first_names.append(names_parts[0].capitalize())
        surnames.append(names_parts[1].lower())
    return first_names, surnames

#Takes a list of names, and returns a list containing their initials
def generate_initials(first_names):
    initials = []
    for name in first_names:
        initials.append(name[0].upper())
    return initials

#Generates random numbers
def random_number_generator(Length):
    digits = string.digits
    random_number = ""
    for x in range(Length):
        random_number += secrets.choice(digits)
    return random_number

#Generates usernames
def generate_usernames (Full_Names):
    first_names = []
    surnames = []
    initials = []
    usernames = []

    first_names, surnames = split_full_names(Full_Names)
    initials = generate_initials(first_names)

    for i in range(len(Full_Names)):
        usernames.append(f"{initials[i]}{surnames[i]}{random_number_generator(4)}")

    return usernames

##writes our usernames to a file
def write_name_output_file(file_path, username_list):
    newline = "\n"
    with open(file_path, "w") as file:
        file.write("##USERNAMES## \n")

    with open (file_path, "a") as input_file:
        for x in range(len(username_list)):
            input_file.write (f"{username_list[x]}{newline}")

run_cond = True

while run_cond == True:

    print("Enter the full path to your list of names")
    input_filepath = input()
    print("Now enter the full path to your output file (or create one)")
    output_filepath = input()

    fullnames = read_input_file(input_filepath)
    usernames = generate_usernames(fullnames)
    write_name_output_file (output_filepath, usernames)

    print("Sucess, Would you like to create more usernames? (Y or N)")
    run_choice = input()

    if run_choice == "Y":
        continue
    elif run_choice == "N":
        print("Alright, Exiting...")
        break
    else:
        print("You entered an invalid choice, Exiting...")
        break




