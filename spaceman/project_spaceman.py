import random

tries_remaining = 7
letters_guessed = ""

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
    # is_word_guessed = True
    for i in range(len(secret_word)):
        if letters_guessed[i] not in secret_word:
            return False
        else: 
            print("You solved the mystery word," + secret_word +"!")
        


        

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
letters_guessed = letters_guessed + guess

#UPDATE
# def update(index, item):
#     checklist[index] = item
def update(index, guess):
    secret_list[index] = guess
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been 
    # guessed correctly so far that are saved in letters_guessed and underscores for 
    # the letters that have not been guessed yet
    secret_list = list(secret_word)
    word_display = "_" * len(secret_word)
    for i in range(len(secret_word)):
        if guess == secret_list[i]:
            update(word_display)
            
            


        



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




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''


    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!\nGuess letters to solve the mystery word to launch Spaceman into space!  If you make more than 7 incorrect guesses, you lose and Spaceman will have to abort his launch.")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    # def user_input(prompt):
    #     #get user input here
    #     user_input = input(prompt)
    #     return user_input

    def guess(prompt):
    #get user input here
        guess = input(prompt)
        return guess

    guess("Please guess a letter:")
    while len(guess) > 1:
        print("You may only guess one letter at a time")
        continue

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    if is_guess_in_word == True:
        print("The letter you guessed appears in the mystery word!")
    if is_guess_in_word == False:
        tries_remaining -= 1
        print("Bummer! The letter you guessed is not in the mystery word. You have {tries_remaining} more tries left.")
        



    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost
    is_word_guessed()







#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
