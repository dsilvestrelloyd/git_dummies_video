
# defining a function to take the parameter sentence
def alternate_char(sentence):

# use .split() to seperate characters within a string with empty spaces as the delimiter
    broken_sentence = sentence.split()

    # defining variables that will be used before the for loops
    lower_or_upper = True
    word = ""
    changed_sentence = []

    # define for loop to iterate through each item in list broken_sentence
    for sub_string in broken_sentence:
    
    # define for loop to iterate through each character in the value of substring
        for letter in sub_string:

            # conditional to check if the character is alphabetic
            if letter.isalpha() == True:
                
                # conditional to check value of lower_or_upper 
                if lower_or_upper == True:

                    # concatenate a lowercase value of letter to variable word 
                    word += letter.lower()

                    # asign false value to lower_or_upper so next value can be uppercase
                    lower_or_upper = False
                
                # else condition is used because if lower_or_upper is not True the only other value it can be is false
                else:
                    
                    # concatenate a uppercase value of letter to variable word 
                    word += letter.upper()

                    # asign false value to lower_or_upper so next value can be lowercase
                    lower_or_upper = True

            # use of else condition to determine the block of code for non-alphabetic characters
            else:

                # no manipulation is necessary the value of letter is concatenated to variable word
                word += letter
        
        # add variable word to list changed_sentence after inner for loop has finished iterating        
        changed_sentence.append(word)

        # resassign variable word to be an empty string value thus it can used for next iterations of inner for loop
        word = ""

    # reassign a changed_sentence to become a string value from the joining of values in prior list changed_sentence
    changed_sentence = " ".join(changed_sentence)

    return changed_sentence


# define function string_validtion with parameter string_values
def string_validation(string_values):

    # use of while True creates infinite loop
    while True:

        # conditional statement that will check if string_values is equal to an empty string
        if string_values == "":

            # use of while True creates infinite loop
            while True:
                # continuously prompt user for answer until an empty string is no longer inputed 
                string_values = input("An error occurred. Please enter your answer again: ")

                if string_values != "":
                    
                    # only breaks inner most while loop when conditional has been met
                    break
                
        # conditional to check if all values in string_values are numeric
        if string_values.isnumeric() == True:

            # use of while True creates infinite loop
            while True:
                # continuously prompt user for until all values are no longer numeric
                string_values = input("An error occurred. Please enter your answer again: ")

                if string_values.isnumeric() == False:
    
                    # only breaks inner most while loop when conditional has been met
                    break

        # once both conditional statements have been met this break will stop the outer while loop breaking the infinte loop     
        break

    # function will return string_values
    return string_values



def invert_alternate_words(for_alteration):
    # listing_alternates will be a list from the spliting of the parameter for_alteration
    listing_alternates = for_alteration.split()

# for loop in iterating through listing_alternates
    for i in range(len(listing_alternates)):
#conditional allows finding of even and odd indexes
        if i % 2 == 0:
            # even indexes are assinged to be lowercase
            listing_alternates[i] = listing_alternates[i].lower()
        else:
            # odd indexes are assigned to be upercase
            listing_alternates[i] = listing_alternates[i].upper()

# use .join()
    listing_alternates = " ".join(listing_alternates)
    # returning value of listing_alternative
    return listing_alternates
    


second_question = "Please enter your phrase or sentence that rhymes: "
first_question = "Please enter the name of a role model of yours: "

# introducing the purpose of the program
print("Welcome, to our inversion of cases program.\
      \n\nThe first section of the program will invert all characters inputted.\
       \n\nTherefore the characters entered output as followed: \nCapital --> Lowercase \t\t  or \t\t Lowercase --> Capital \n\n ")

# store users input to first the question in a variable role_model 
role_model = input(first_question)

# reassign role model the returned value of function string_validition with role an argument
role_model = string_validation(role_model)


# introduce the second section of the program
print("\n\nThe second section of the program will output a phrase or sentence with words alternating in their casing\
      \n\ne.g. \t\t1st word lower, 2nd word, UPPER 3rd word lower, etc...\n")

# store users response to the second question in variable alternating 
second_response = input(second_question)

# assign alternating_words to return value of function string_validation with second_response as the argument
alternating_words = string_validation(second_response)

# print returned value if alternate_char function in a f-string
print(f"\n\n{alternate_char(role_model)}, is an amazing role model.\n\n")

# print the returned value of invert_alternate_words function in an f-string
print(f"The inversion of your phrase/sentence by word is as followed:\
      \n{invert_alternate_words(alternating_words)}")


