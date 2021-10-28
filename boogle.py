#cd /Users/kajpeterson/Boggle

import itertools
import random
import operator
import time
import sys
import pandas as pd

#====================================================================================
#DEFINE FUNCTIONS

def rolldice():
    positions = []
    for i in range(1,17):
        positions.append(i)
    random.shuffle(positions)
    return(positions)

def letters_func(word):
    letters = []
    skip = 0
    for char in word:
        if skip == 1:
            skip = 0
            continue
        if skip == 0:
            if char == "Q":
                letters.append('QU')
                skip = 1
            else:
                letters.append(char)
    return letters

def spellcheck(word, letters):
    path = sys.path[0]
    csv_path = f'{path}/en_lower_61k.csv'
    #csv_path = '/Users/kajpeterson/Boggle/en_diy_lower.csv' alternatively, hardcode the path if you don't want to use sys.
    valid1 = 0
    if len(letters) < 3:
        print(f'{word} is invalid. Must be at least 3 letters.')
    else:
        df = pd.read_csv(csv_path)
        if word.lower() in df.values:
            valid1 = 1
        else:
            print(f"{word} is not in the dictionary.")
    return valid1

def chains_func(letters, dice):
    word_pos_list = []
    valid3 = 1
    for l in letters:
        letter_pos_list = []
        found = 0
        for d in range (0,len(dice)):
            #print(f'checking d{1}')
            if dice[d].get('letter') == l:
                letter_pos_list.append(dice[d].get('pos'))
                found = 1
                #print("letter found!")
        if found == 0:
            print(f"{letters} is invalid because one or more letters do not appear on the board.")
            valid3 = 0
            break
        word_pos_list.append(letter_pos_list)
    #print(word_pos_list)    
    return list(itertools.product(*word_pos_list)), valid3 

def validate(chains,dice):     
    #print("\n validating")
    default_pos = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    valid_pos = default_pos
    valid2 = 0
    for chain in chains:
        if valid2 == 1:
            break
        for i in range (0,len(chain)):
            if chain.count(chain[i]) > 1:
                #print(f'{chain} is invalid because it contains duplicates')
                valid_pos = default_pos
                break
            if chain[i] in valid_pos:
                if i == len(chain) - 1:
                    #print(f'{chain} is a valid chain')
                    valid_pos = default_pos
                    valid2 = 1
                else:
                    for d in range (0,len(dice)):
                        if chain[i] == dice[d].get('pos'):
                            valid_pos = dice[d].get('adj')
            else:
                #print(f'{chain} is invalid')
                valid_pos = default_pos
                break
    return valid2

def show_board(dice):
    board_unsorted = []
    for d in range (0,len(dice)):
        space = []
        space.append(dice[d].get('pos'))
        if len(dice[d].get('letter')) == 1:
            letter_padded = dice[d].get('letter') + ' '
        else:
            letter_padded = dice[d].get('letter')
        space.append(letter_padded)
        board_unsorted.append(space)
    board_sorted = sorted(board_unsorted, key = operator.itemgetter(0))
    print(f'\n___________\n{board_sorted[0][1]} {board_sorted[1][1]} {board_sorted[2][1]} {board_sorted[3][1]}\n{board_sorted[4][1]} {board_sorted[5][1]} {board_sorted[6][1]} {board_sorted[7][1]}\n{board_sorted[8][1]} {board_sorted[9][1]} {board_sorted[10][1]} {board_sorted[11][1]}\n{board_sorted[12][1]} {board_sorted[13][1]} {board_sorted[14][1]} {board_sorted[15][1]}\n-----------\n')

def  create_board():
    die1 = ('R', 'I', 'F', 'O', 'B', 'X')
    die2 = ('I', 'F', 'E', 'H', 'E', 'Y')
    die3 = ('D', 'E', 'N', 'O', 'W', 'S')
    die4 = ('U', 'T', 'O', 'K', 'N', 'D')
    die5 = ('L', 'U', 'P', 'E', 'T', 'S')
    die6 = ('A', 'C', 'I', 'T', 'O', 'A')
    die7 = ('Y', 'L', 'G', 'K', 'U', 'E')
    die8 = ('QU', 'B', 'M', 'J', 'O', 'A')
    die9 = ('H', 'M', 'S', 'R', 'A', 'O')
    die10 = ('E', 'H', 'I', 'S', 'P', 'N')
    die11 = ('B', 'A', 'L', 'I', 'Y', 'T')
    die12 = ('E', 'Z', 'A', 'V', 'N', 'D')
    die13 = ('R', 'A', 'L', 'E', 'S', 'C')
    die14 = ('U', 'W', 'I', 'L', 'R', 'G')
    die15 = ('P', 'A', 'C', 'E', 'M', 'D')
    die16 = ('V', 'E', 'T', 'I', 'G', 'N')

    adj_list = [(2,5,6), (1,3,5,6,7), (2,4,6,7,8), (3,7,8), (1,2,6,9,10), (1,2,3,5,7,9,10,11), (2,3,4,6,8,10,11,12), (3,4,7,11,12), (5,6,10,13,14), (5,6,7,9,11,13,14,15), (6,7,8,10,12,14,15,16), (7,8,11,15,16), (9,10,14), (9,10,11,13,15), (10,11,12,14,16), (11,12,15)]
    positions = rolldice()

    d1 = {'pos': positions[0], 'letter': die1[random.randint(0,5)], 'adj': adj_list[positions[0]-1]}
    d2 = {'pos': positions[1], 'letter': die2[random.randint(0,5)], 'adj': adj_list[positions[1]-1]}
    d3 = {'pos': positions[2], 'letter': die3[random.randint(0,5)], 'adj': adj_list[positions[2]-1]}
    d4 = {'pos': positions[3], 'letter': die4[random.randint(0,5)], 'adj': adj_list[positions[3]-1]}
    d5 = {'pos': positions[4], 'letter': die5[random.randint(0,5)], 'adj': adj_list[positions[4]-1]}
    d6 = {'pos': positions[5], 'letter': die6[random.randint(0,5)], 'adj': adj_list[positions[5]-1]}
    d7 = {'pos': positions[6], 'letter': die7[random.randint(0,5)], 'adj': adj_list[positions[6]-1]}
    d8 = {'pos': positions[7], 'letter': die8[random.randint(0,5)], 'adj': adj_list[positions[7]-1]}
    d9 = {'pos': positions[8], 'letter': die9[random.randint(0,5)], 'adj': adj_list[positions[8]-1]}
    d10 = {'pos': positions[9], 'letter': die10[random.randint(0,5)], 'adj': adj_list[positions[9]-1]}
    d11 = {'pos': positions[10], 'letter': die11[random.randint(0,5)], 'adj': adj_list[positions[10]-1]}
    d12 = {'pos': positions[11], 'letter': die12[random.randint(0,5)], 'adj': adj_list[positions[11]-1]}
    d13 = {'pos': positions[12], 'letter': die13[random.randint(0,5)], 'adj': adj_list[positions[12]-1]}
    d14 = {'pos': positions[13], 'letter': die14[random.randint(0,5)], 'adj': adj_list[positions[13]-1]}
    d15 = {'pos': positions[14], 'letter': die15[random.randint(0,5)], 'adj': adj_list[positions[14]-1]}
    d16 = {'pos': positions[15], 'letter': die16[random.randint(0,5)], 'adj': adj_list[positions[15]-1]}

    dice = (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16)

    return dice

def play(player, dice, bank1, bank2, time_limit, quit):
    time_up = 0
    bank = []
    while True:
        if quit == 1:
            break
        if time_up == 1:
            break
        word = input(f"Okay, Player {player}. You have {time_limit/60} minutes. Hit ENTER to begin.").upper()
        if word == '':
            tic = time.time()
            while True:
                if quit == 1:
                    break
                if player == 1:
                    bank = bank1
                elif player == 2:
                    bank = bank2
                show_board(dice)
                print(bank)
                word = input("Enter a word on the board:\n").upper()
                toc = time.time()
                if toc-tic > time_limit:
                    time_up = 1
                    break
                elif word == "Q":
                    print("Goodbye!")
                    quit = 1
                    break
                elif word in bank:
                    print(f'you already guessed {word}.')
                else:
                    letters = (letters_func(word))
                    valid1 = spellcheck(word, letters)
                    if valid1 == 1:
                        (chains, valid3) = chains_func(letters, dice)
                        valid2 = 0
                        if valid3 == 1:
                            valid2 = (validate(chains, dice))
                        if valid2 == 1:
                            print(f'{word} is a valid word')
                            bank.append(word)
                        else:
                            print(f'{word} is NOT a valid word')
        elif word == "Q":
            print("Goodbye!")
            quit = 1
            break
        else:
            print("No, just hit ENTER.")
    return (bank, quit)

def scoring(bank1, bank2, score1, score2, round):
    score_dict = {3:1,4:1,5:2,6:3,7:5,8:11}
    score_list = []
    for guess in bank1:
        if guess in bank2:
            score_list.append(0)
        elif len(guess) > 8:
            score_list.append(score_dict[8])
        else:
            score_list.append(score_dict[len(guess)])
    print("________________________________")
    print(f"Player 1's score for round {round}:")
    for i in range (0,len(bank1)):
            print(f"{bank1[i]} - {score_list[i]}")
    print(f"Round {round} Total: {sum(score_list)}")
    score1 = score1 + sum(score_list)
    print(f"Player1 Total: {score1}")
    print("--------------------------------")

    score_list = []
    for guess in bank2:
        if guess in bank1:
            score_list.append(0)
        elif len(guess) > 8:
            score_list.append(score_dict[8])
        else:
            score_list.append(score_dict[len(guess)])
    print("________________________________")
    print(f"Player 2's score for round {round}:")
    for i in range (0,len(bank2)):
            print(f"{bank2[i]} - {score_list[i]}")
    print(f"Round {round} Total: {sum(score_list)}")
    score2 = score2 + sum(score_list)
    print(f"Player2 Total: {score2}")
    print("--------------------------------")
    return(score1, score2)

#====================================================================================
#MASTER FUNCTION
def main():
    print("\n\n=======================\n* Welcome to Boogle!! *\n=======================\n(Boggle is trademarked.)\n")
    print("Common words among players eliminated\nNo. of Letters | Points per Word\n       3       |        1\n       4       |        1\n       5       |        2\n       6       |        3\n       7       |        5\n       8+      |        11\n")
    print("For the 2-player version, take turns.\nThe screen will clear in between players so player 2 doesn't see player 1's words.")
    quit = 0
    score1 = 0
    score2 = 0
    round = 1
    while True:
        if quit == 1:
            break
        else:
            word = input("MAIN MENU\nPlease make a selection:\n    1 = 1 Player\n    2 = 2 Players\n    Q = Quit\n").upper()
            if word == "Q":
                print("Goodbye!")
                quit = 1
                break
            elif word == "1":
                if word == "Q":
                    print("Goodbye!")
                    quit = 1
                    break
                else:
                    while True:
                        if quit == 1:
                            break
                        players = word
                        bank1 = []
                        bank2 = []
                        time_limit = 180 #seconds
                        dice = create_board()
                        player = 1
                        print(f"~~~~~~~~\nROUND {round}!\n~~~~~~~~")
                        (bank1, quit) = play(player, dice, bank1, bank2, time_limit, quit)
                        if quit == 1:
                            break    
                        print(f"Time's up, Player 1! Here are your words:\n{bank1}\n")
                        (score1, score2) = scoring(bank1, bank2, score1, score2, round)
                        while True:
                            if quit == 1:
                                break
                            word = input("Play again? (Y/N)").upper()
                            if word == "N":
                                if score1 > score2:
                                    winner = 1
                                elif score2 > score1:
                                    winner = 2
                                else:
                                    winner = 0
                                if winner > 0:
                                    print(f"\n/\***************************/\ \n\/ Player {winner} wins!!! Yaaay!!! \/ \n/\***************************/\ \n")
                                else:
                                    print("It's a tie!!!")
                                quit = 1
                                break
                            elif word == "Q":
                                print("Goodbye!")
                                quit = 1
                                break
                            elif word == "Y":
                                round = round + 1
                                break
                            else:
                                print("selection not valid")
            elif word == "2":
                if word == "Q":
                    print("Goodbye!")
                    quit = 1
                    break
                else:
                    while True:
                        if quit == 1:
                            break
                        players = word
                        bank1 = []
                        bank2 = []
                        time_limit = 180 #seconds
                        dice = create_board()
                        player = 1
                        print(f"~~~~~~~~\nROUND {round}!\n~~~~~~~~")
                        (bank1, quit) = play(player, dice, bank1, bank2, time_limit, quit)
                        if quit == 1:
                            break    
                        print(f"Time's up, Player 1! Here are your words:\n{bank1}\n")     
                        while True:
                            if quit == 1:
                                break
                            word = input("Okay, Player 1. Hit ENTER and pass to Player 2.").upper()
                            if word == "Q":
                                print("Goodbye!")
                                quit = 1     
                                break
                            elif word == "":
                                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                                player = 2
                                (bank2, quit) = play(player, dice, bank1, bank2, time_limit, quit)
                                if quit == 1:
                                    break
                                print(f"Time's up, Player 2! Here are your words:\n{bank2}\n")
                                break
                            else:
                                print("Selection not valid.")
                        (score1, score2) = scoring(bank1, bank2, score1, score2, round)
                        while True:
                            if quit == 1:
                                break
                            word = input("Play again? (Y/N)").upper()
                            if word == "N":
                                if score1 > score2:
                                    winner = 1
                                elif score2 > score1:
                                    winner = 2
                                else:
                                    winner = 0
                                if winner > 0:
                                    print(f"\n/\***************************/\ \n\/ Player {winner} wins!!! Yaaay!!! \/\n/\***************************/\ \n")
                                else:
                                    print(f"\n/\************************/\ \n\/ It's a tie!!! Yaaay!!! \/\n/\************************/\ \n")
                                quit = 1
                                break
                            elif word == "Q":
                                print("Goodbye!")
                                quit = 1
                                break
                            elif word == "Y":
                                round = round + 1
                                break
                            else:
                                print("selection not valid")
            else:
                print("Selection not valid.")

main()
