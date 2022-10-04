
import random


letters_guessed = []



def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            # maybe do an or statement to check for duplicate letters?
            return False
        else: 
            return True
        


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the 
    secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, 
        the string should contain the letter at the correct position.  For letters in the word that the 
        user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been 
    # guessed correctly so far that are saved in letters_guessed and underscores for 
    # the letters that have not been guessed yet

    word_display = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            word_display = word_display[:i] + secret_word[i] + word_display[i+1:]

#   This is what I have so far, I am stuck on how to get it to check for duplicate letters
# sometimes when there is a duplicate letter, it says the puzzle is solved when it is not



   
    print(' '.join(word_display))
    print("Letters you have guessed: ", letters_guessed)




def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    if guess in secret_word:
        return True
    else:
        return False

# ----------------------------
# find how many times a letter occurs in the word

# --------------------------------


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!\nGuess letters to solve the mystery word to launch Spaceman into space!  If you make more than 7 incorrect guesses, you lose and Spaceman will have to abort his launch.")
    

        #TODO: Ask the player to guess one letter per round and check that it is only one letter
    

    tries_remaining = 7
    while True:
        

        guess = input("Please guess a letter:")
        # if len(guess) > 1:
        #     print("You may only guess one letter at a time")
    
        letters_guessed.append(guess)
            

        #TODO: Check if the guessed letter is in the secret or not and give the player feedback

        if is_guess_in_word(guess, secret_word) == True:
            print("The letter you guessed appears in the mystery word!")
        if is_guess_in_word(guess, secret_word) == False:
            tries_remaining -= 1
            print("Bummer! The letter you guessed is not in the mystery word. You are allowed " + str(tries_remaining) + " more incorrect tries.")
            

        #TODO: show the guessed word so far
        get_guessed_word(secret_word, letters_guessed)
        #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("You solved the mystery word," + secret_word +"!")

        if tries_remaining == 0:
            print("You failed to launch Spaceman :_(\nThe mystery word was: " + secret_word)
            break
            

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

def test():
    # add test code here
    secret_word = load_word()
    spaceman(secret_word)
    
# test()