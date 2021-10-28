#HANGMAN GAME! ...but now it's Flower Petals.

#import word list and random functions
from nltk.corpus import words # get the word list
import random #need the randint function
word_list = words.words()

#draws a flower
def draw(strikes):
    print("\n\n\n")
    if strikes == 0:
        print("\n    / \\\n  <  O  >\n    \ /\n     |\n    ~|~\n     |\n     |")
    if strikes == 1:
        print("\n    / \\\n  <  O  >\n    \ /\n     |\n     |~\n     |\n~    |")
    if strikes == 2:
        print("\n    / \\\n  <  O  >\n    \ /\n     |\n     | \n     |\n~    |    ~")
    if strikes == 3:
        print("\n    / \\\n  <  O  >\n     | \n     |\n     | \n     |\n~\/  |    ~")
    if strikes == 4:
        print("\n    / \\\n  <  O   \n     | \n     |\n     | \n     |\n~\/  |   >~")
    if strikes == 5:
        print("\n       \n  <  O   \n     | \n     |\n     | \n     |\n~\/  | /\>~")
    if strikes == 6:
        print("\n       \n     O   \n     | \n     |\n     | \n     |\n~\/< | /\>~")
    print("\n")

#generates a random English word of a minimum length
def randomword():        
    gen = 1
    minlength = 6
    while gen == 1:    
        n = random.randint(1,len(word_list))
        if (len(word_list[n])) < minlength: #Filters out short words, cause that's too easy.
            continue #gets a new word if it was too short
        word = word_list[n]
        gen = 0
    return word

#Thsi is where most of it happens.
def blanks():
    word = randomword()    #gets random word
    word = word.lower()    #makes it lower case so case doesn't matter
    length = len(word)
    X = ['_ ']*length       #generates the blanks the player sees
    print(draw(0))
    print(*X,sep='')
    play = "y"    #starts while loop
    wrong = 0     #a wrong guess will change this to 1
    badguess = []
    print("Quit at any time by typing 'Quit'.")
    while play == "y":
    #restarts the loop if they've already guessed this letter.
        repeatright = 0
        repeatwrong = 0
        guess = input("\nGuess a letter: ")
        for i in range (0,length):
            if X[i] == guess:
                repeatright = 1               
        for i in range (0,len(badguess)):
            if badguess[i] == guess:
                repeatwrong = 1
        if repeatright == 1:
            print("You already guessed that.")
            continue
        if repeatwrong == 1:
            print("It was wrong then, it's still wrong now.")
            continue
    #otherwise, if it's a new letter, checks to see if it's right.
        goodguess = 0
        guess = guess.lower()           #makes both upper and lower case guesses okay (random word is always lowercase)
        if guess == "quit" or guess =="exit" or guess == "end" or guess == "solve":             #this way I don't have to ask to play every time. User just has to remember "quit" to quit.
            print("I guess they gave up!")
            print(word)
            break
        for i in range (0,length):
            if word[i] == guess:        
                X[i] = guess
                goodguess = 1
        if goodguess == 0:
            wrong = wrong + 1
            badguess.append(guess)
        
        strikes = len(badguess)
        draw(strikes)    
        print(*X,sep='')        #shows correct guesses + remaining blanks. Makes more legible by concatenating a string with the elements of X. 
        print ("\nBad guesses: ", badguess)
        if strikes > 5:
            print("\nBoo, that sucks, you lose.")
            print(word)
            break
        if X.count('_ ') == 0:
            print("\nOMG YAY you win!")
            break    


#just the outer while loop. Probably could have included in blanks() and renamed that main.
def main():
    play = input("Would you like to play Flower Petals? (y/n): ")
    while play == "y":
        blanks()
        play = input("\nPlay again? (y/n): ") #y restarts while loop, anything else exits it
    
        
    print("\nBye, Felicia!") 
main()