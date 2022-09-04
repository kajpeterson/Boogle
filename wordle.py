#!/usr/bin/env python
# coding: utf-8

# Let's make Wordle.

# In[ ]:


import sys
import pandas as pd
import random


# In[ ]:


#Random word generator
path = sys.path[0]
filename = '/en_lower_61k_5let.csv'
wordframe = pd.read_csv(path+filename, header = None)
wordlist = list(wordframe[0])
word = wordlist[random.randint(0,len(wordlist))]


# In[ ]:


def display(guess_inputs, guess_outputs, in_set, out_set, untested_set):
    print('\n\n')
    for i in range (0,len(guess_inputs)):
        print(f'{i+1}  {guess_inputs[i]}    {guess_outputs[i]}')
    print(f'\nIn: {in_set}\nOut: {out_set}\nUntested: {untested_set}')


# In[ ]:


#Take guess & word
#Return entry for guess_outputs

def let_check(guess, word, in_set, out_set, untested_set):
    letters = []
    for i in range (0,5):
        if guess[i] == word[i]:
            letters.append(guess[i].upper())
            in_set.add(guess[i])
            try:
                untested_set.remove(guess[i])
            except:
                pass
        elif guess[i] in word:
            letters.append(guess[i])
            in_set.add(guess[i])
            try:
                untested_set.remove(guess[i])
            except:
                pass
        else:
            letters.append('_')
            out_set.add(guess[i])
            try:
                untested_set.remove(guess[i])
            except:
                pass
    guess_output = f'{letters[0]} {letters[1]} {letters[2]} {letters[3]} {letters[4]}'
    return (guess_output, in_set, out_set, untested_set)


# In[134]:


def main():
    print('Welcome to Wordle!\nGuess the word in 6 tries.\nCapital letters are correct, and in the correct position.\nLower case letters are in the word, but not in that position.\nA blank space means that letter is not in the word.\nEnter Q at any time to quit.')
    guess_inputs = []
    guess_outputs = []
    in_set = set()
    out_set = set()
    untested_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    while True:
        guess = str(input("Guess the wordle\n")).lower()
        if guess == 'q':
            print(f'The word was {word}.')
            break
        elif guess in wordlist:
            guess_inputs.append(guess)
            (guess_output, in_set, out_set, untested_set) = let_check(guess, word, in_set, out_set, untested_set)
            guess_outputs.append(guess_output)
            display(guess_inputs, guess_outputs, in_set, out_set, untested_set)
        else:
            print('Nope, try again.\n')

        if guess == word:
            print('\n******************\n* Yay, you win!! *\n******************')
            break
        elif len(guess_inputs) == 6:
            print(f'\nOooh, tough break.\nThe word was {word}.\nBetter luck next time.')
            break


# In[135]:


main()


# In[ ]:




