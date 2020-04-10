import os #for clearing the screen
import argparse #for command line arguments
import csv #for reading from csv file with episode titles
import random
import string

os.system("clear") #clear screen

#check if this letter is in the word
def check(letter, mistakes):
    #check for all occurrences of the letter
    good = 0
    for i in range(len(word)):
        if letter == word[i]:
            guess[i] = letter
            good += 1
    #if the letter has not occurred in the word
    if good == 0:
        mistakes += 1
        print("\nSorry! You're wrong.")
        wrongletters.append(letter)
        return mistakes
    #if the letter has occurred somewhere in the word
    else:
        print("\nNice one!")
        return mistakes

#set command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--a", default = 2, type = int)
args = parser.parse_args()
a = args.a

#input word
if a == 1:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to Episode Hangman!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Guess the episode title!\n")
    #load data from Scraped.csv and randomly pick an episode title (row)
    with open("EpisodeList.csv") as f:
        reader = csv.reader(f)
        chosen_word = random.choice(list(reader))[0]
    chosen_word = chosen_word.lower()

else:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to 2-player Hangman!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    #player 1 inputs a word
    chosen_word = input("Player 1, enter your chosen word/sentence : ")

    #clear the screen before player 2 sees!
    os.system("clear")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to 2-player Hangman!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Player 2, guess the word/sentence!\n")

#convert string to list
word = [x for x in chosen_word]
punctuation = [' ', ",", '?', '!', '(', ')', '-', ':', ';', '&']

#the guess so far
guess = []
for i in range(0, len(word)):
    #if word[i] == ' ' or word[i] == "," or word[i] == '?' or word[i] == '!' or word[i] == '(' or word[i] == ')' or word[i] == '-' or word[i] == ':' or word[i] == ';' or word[i] == '&' or word[i].isnumeric() == True:
    if word[i] in punctuation:
        guess.append(word[i])
    else:
        guess.append('_')

#the wrong letters guessed so far
wrongletters = []

print("You're allowed 10 mistakes.\n")

#print the blanks
print(*guess, sep=' ')

mistakes = 0
#give the user 10 mistakes when guessing the letters in the word
while mistakes < 10:

    #input the guessed letter
    letter = input("\nGuess a letter: ")
    
    #check if more than one letter
    if len(letter) > 1:
        print("\nOne letter at a time, please!")
    elif letter.isnumeric() == True or letter in punctuation:
        print("\nOnly guess letters!")
    #check if that letter is in the word
    elif letter in wrongletters:
        print("\nYou've already guessed that!")
    else:
        mistakes = check(letter, mistakes)
    print("Mistakes =", mistakes, wrongletters)

    print("\n")
    print(*guess, sep=' ')

    #if the word has been completely guessed
    if guess == word:
        print("\nWell done! \nYou've guessed it.\n")
        break
    if mistakes == 10:
        print("\nOops, you've made 10 mistakes.\nThe answer was...", chosen_word, "\nGAME OVER.\n")


