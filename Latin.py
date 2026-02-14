
# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 3

def word_to_pig(word): # defines function word_to_pig with argument word
    if word[0].isupper(): # conditions if the first letter is uppercase    
        word = word.lower() # converts all uppercase letters to lowercase
        if word[0] in 'aeiou': # conditions if the first uppercase letter in word is a vowel
            word = word + 'yay' # adds yay to voweled word
            word = word.replace(word[0], word[0].upper(), 1) # capitalizes first letter one time
            return word # returns final word in pig latin
        
        else: # conditions for first uppercase letters that are consonants
            for letter in word: # creates a for loop for letters in word
                if letter not in 'aeiou': # conditions if letter is a consonant
                    word = word.strip(letter) # removes letter from the beginning of the word
                    word = word + letter # adds removed letter to the end of the word
                else: # breaks for loop when a vowel is identified
                    break
        
            word = word + 'ay' # adds 'ay' to the end of the modified word from the for loop
            word = word.replace(word[0], word[0].upper(), 1) # capitalizes beginning letter one time
            return word # returns final word in pig latin
            
    else: # conditions word when first letter is not uppercase
        if word[0] in 'aeiou': # identifies if the first lowercase letter is a vowel
            word = word + 'yay' # adds yay to voweled words
            return word # returns final word in pig latin
        
        else: # conditions for first lowercase letters that are consonants
            for letter in word: # creates a for loop for letters in word
                if letter not in 'aeiou': # conditions if letter is a consonant
                    word = word.strip(letter) # removes letter from the beginning of the word
                    word = word + letter # adds letter to the end of the word
                else: # breaks for loop when vowel is identified
                    break
        
            word = word + 'ay' # adds 'ay' to the end of the modified word
            return word # returns final word in pig latin

word = input('Please enter a word: ') # grabs input from the user as word

print(word_to_pig(word)) # prints word in pig latin

def name_to_pig(first_name, last_name): # defines name_to_pig function with arguments first_name and last_name
    f = word_to_pig(first_name) # creates variable f for first_name in Pig Latin using word_to_pig function
    l = word_to_pig(last_name) # creates variable l for last_name in Pig Latin using word_to_pig function
    n = f + ' '+ l  # puts the values of f and l in pig latin together with a space in between
    return n # returns first_name in Pig Latin and last_name in Pig Latin

name = input('Please enter first name and last name with a space in between: ') # grabs input from the user for first and last name
name = name.split() # splits the user string name into list based on space

while len(name) != 2: # asks user to enter input again if less than 2 words or more than 2 words are recognized in first and last name
    name = input('Please enter first name and last name with a space in between: ') # grabs input from the user again for first and last name
    name = name.split() # splits the user string name into list based on space

first_name = name[0] # assigns first_name with first listed string in name.split()
last_name = name[1] # assigns last_name with second listed string in name.split()

print(name_to_pig(first_name, last_name)) # prints name in Pig Latin


    



