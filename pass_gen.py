import string
import random

if __name__ == "__main__" :

    # getting lists of alphabets, digits and punctuations from string module
    alphabets = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    
    # adding all these characters to one list
    list_of_characters = []
    list_of_characters.extend(alphabets)
    list_of_characters.extend(digits)
    list_of_characters.extend(punctuations)

    # shuffling the list_of_characters using the random module
    random.shuffle(list_of_characters)

    password_length = int(input("Enter the length of the password to be generated: \n"))
    password = ""
    i = 0
    while(i<password_length):
        password += list_of_characters[i]
        i=i+1

    print("Generated password is: " + password)