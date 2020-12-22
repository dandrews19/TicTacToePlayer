# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Fall 2020
# Assignment 8
# Description:
# This program uses functions to  simulate a two player game of Tic Tac
# Toe. The program will allow the two players to place an “x” or an “o” somewhere on
# the board and determine when someone wins or when a stalemate is reached.

import TicTacToeHelper


# prints a nice board
def printPrettyBoard(boardList):


    print("")
    print(boardList[0] + "| " + boardList[1] + "| " + boardList[2])
    print("---------")
    print(boardList[3] + "| " + boardList[4] + "| " + boardList[5])
    print("---------")
    print(boardList[6] + "| " + boardList[7] + "| " + boardList[8])
    print("")



# checks if players spot request is in range and it is not taken
def isValidMove(boardList, spot):

    if (0 <= spot <= 8) and (boardList[spot] != "x " and boardList[spot] != "o "):
        return True
    else:
        return False


# replaces selected spot with the player letter
def updateBoard(boardList, spot, playerLetter):

    boardList[spot] = playerLetter

# runs game with x as the start
def playGame1():
    boardList = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    winner1 = "n"
    move_counter = 0
    winner2 = "n"
# runs game until there is a winner
    while winner2 == "n" and winner1 == "n":
        printPrettyBoard(boardList)
        spot = input("Player x, pick a spot: ")
        while spot.isdigit() == False:
            spot = input("Player x, pick a spot: ")
        playerLetter = "x "
        valid = isValidMove(boardList, int(spot))
        while valid == False:
            print("Invalid move, please try again.")
            spot = input("Player x, pick a spot: ")
            valid = isValidMove(boardList, int(spot))
        if valid == True:
            updateBoard(boardList, int(spot), playerLetter)
        move_counter += 1
        winner1 = TicTacToeHelper.checkForWinner(boardList, move_counter)
        if winner1 == "n":
            printPrettyBoard(boardList)
            spot = input("Player o, pick a spot: ")
            while spot.isdigit() == False:
                spot = input("Player o, pick a spot: ")
            playerLetter = "o "
            valid = isValidMove(boardList, int(spot))
            while valid == False:
                print("Invalid move, please try again.")
                spot = input("Player o, pick a spot: ")
                valid = isValidMove(boardList, int(spot))
            if valid == True:
                updateBoard(boardList, int(spot), playerLetter)
            move_counter += 1
            winner2 = TicTacToeHelper.checkForWinner(boardList, move_counter)
    printPrettyBoard(boardList)
    # prints results
    print("Game Over!")
    if winner1 == "x ":
        print("Player x is the winner!")
    if winner2 == "o ":
        print("Player o is the winner!")
    if winner1 == "s" or winner2 == "s":
        print("Stalemate reached!")



# runs the game with o as the start
def playGame2():
    boardList = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 "]
    winner1 = "n"
    move_counter = 0
    winner2 = "n"
    # runs the game until there is a winner, switching between x and o for moves
    while winner2 == "n" and winner1 == "n":
        printPrettyBoard(boardList)
        spot = input("Player o, pick a spot: ")
        while spot.isdigit() == False:
            spot = input("Player o, pick a spot: ")
        playerLetter = "o "
        valid = isValidMove(boardList, int(spot))
        while valid == False:
            print("Invalid move, please try again.")
            spot = input("Player o, pick a spot: ")
            valid = isValidMove(boardList, int(spot))
        if valid == True:
            updateBoard(boardList, int(spot), playerLetter)
        move_counter += 1
        winner1 = TicTacToeHelper.checkForWinner(boardList, move_counter)
        if winner1 == "n":
            printPrettyBoard(boardList)
            spot = input("Player x, pick a spot: ")
            while spot.isdigit() == False:
                spot = input("Player x, pick a spot: ")
            playerLetter = "x "
            valid = isValidMove(boardList, int(spot))
            while valid == False:
                print("Invalid move, please try again.")
                spot = input("Player x, pick a spot: ")
                valid = isValidMove(boardList, int(spot))
            if valid == True:
                updateBoard(boardList, int(spot), playerLetter)
            move_counter += 1
            winner2 = TicTacToeHelper.checkForWinner(boardList, move_counter)
    printPrettyBoard(boardList)
    # states outcome of game
    print("Game Over!")
    if winner1 == "o ":
        print("Player o is the winner!")
    if winner2 == "x ":
        print("Player x is the winner!")
    if winner1 == "s" or winner2 == "s":
        print("Stalemate reached!")


# continues the game while player wants to play, and asks user which symbol they want to start with
def main():
    print("Welcome to Tic Tac Toe!")
    game = "Y"
    while game == "Y" or game == "y":
        start = input("Choose which player you want to start (x or o): ")
        while start != "x" and start != "X" and start != "o" and start != "O":
            start = input("Choose which player you want to start (x or o): ")
        if start == "x" or start == "X":
            playGame1()
        elif start == "o" or start == "O":
            playGame2()
        game = input("Would you like to play another round? (y/n): ")
        while game != "Y" and game != "y" and game != "n" and game != "N":
            game = input("Would you like to play another round? (y/n): ")
    print("Goodbye!")




main()