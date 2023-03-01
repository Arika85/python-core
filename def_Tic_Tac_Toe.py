import numpy as np
import random


dash = []
for i in range(0,10):
    i = '_'
    dash.append(i)

def table():
    print("\t   Tic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| 1 || 2 || 3 ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| 4 || 5 || 6 ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| 7 || 8 || 9 ||")
    print("\t~~~~~~~~~~~~~~~~~")

    print("\n\t   Tic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {dash[1]} || {dash[2]} || {dash[3]} ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {dash[4]} || {dash[5]} || {dash[6]} ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {dash[7]} || {dash[8]} || {dash[9]} ||")
    print("\t~~~~~~~~~~~~~~~~~")


flag = True
while flag:
    table()
    X = int(input("\nX: Where would you like to place your piece (1-9): "))
    if dash[X] == "_":
        dash[X] = "X"
    table()
     
    if "X" == dash[1] and "X" == dash[2] and "X" == dash[3]:
        table()
        print("Player 1 wins")
        break
    elif "X" == dash[4] and "X" == dash[5] and "X" == dash[6]:
        print("Player 1 wins")
        table()
        break
    elif "X" == dash[7] and "X" == dash[8] and "X" == dash[9]:
        table()
        print("Player 1 wins")
        break
    elif "X" == dash[1] and "X" == dash[5] and "X" == dash[9]:
        table()
        print("Player 1 wins")
        break
    elif "X" == dash[3] and "X" == dash[5] and "X" == dash[6]:
        table()
        print("Player 1 wins")
        break
    elif "X" == dash[2] and "X" == dash[5] and "X" == dash[7]:
        table()
        print("Player 1 wins")
        break
    elif "X" == dash[3] and "X" == dash[5] and "X" == dash[7]:
        table()
        print("Player 1 wins")
        break
    else:
        print("This is not a spot on the board.  Try again!")
    table()
    
    O = int(input("O: Where would you like to place your piece (1-9): "))
    if dash[O] == "_":
        dash[O] = "O"
    table()

    if "O" == dash[1] and "O" == dash[2] and "O" == dash[3]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[4] and "O" == dash[5] and "O" == dash[6]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[7] and "O" == dash[8] and "O" == dash[9]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[1] and "O" == dash[5] and "O" == dash[9]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[3] and "O" == dash[5] and "O" == dash[6]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[2] and "O" == dash[5] and "O" == dash[7]:
        table()
        print("Player 2 wins")
        break
    elif "O" == dash[3] and "O" == dash[5] and "O" == dash[7]:
        table()
        print("Player 2 wins")
        break
    else:
        print("This is not a spot on the board.  Try again!")

