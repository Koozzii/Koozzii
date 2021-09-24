

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
from math import *

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    wordLen = len(secretWord)
    for e in secretWord:
        if e in lettersGuessed:
            wordLen -= 1
            if wordLen == 0:
                return True
        else:
            return False
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    wordList = []
    theWord = ''
    count = 0
    for x in secretWord:
        wordList.append(x)
    for y in wordList:
        if y in lettersGuessed:
            count += 1
        else:
            wordList[count] = '_ '
            count += 1
    for z in wordList:
        theWord = theWord + z
    return theWord
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

alphabet = string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    alphabet = string.ascii_lowercase
    alphabetList = []
    word = ''
    for x in alphabet:
        alphabetList.append(x)
    for y in lettersGuessed:
        if y in alphabetList:
            alphabetList.remove(y)
            
    for z in alphabetList:
        word = word + z
    return word
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
      '''
    print("Welcome to the game, Hangman!")
    lettersGuessed = []
    numberOfGuesses = 8
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    while numberOfGuesses != 0 and False == (isWordGuessed(secretWord, lettersGuessed)):
        print("You have " + str(numberOfGuesses) + " left.")
        print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
        inputGuess = str(input("Please guess a letter: "))
        guess = inputGuess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
            numberOfGuesses -= 1
            lettersGuessed.append(guess)
    if numberOfGuesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
    else:
            print("Congratulations, you won!")
    '''  
    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
