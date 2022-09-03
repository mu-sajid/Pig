from colorama import Fore
from keyboard import is_pressed
from random import randint
from time import sleep
import turtle
#

# Functions
def clearConsole():
    ''''Will clear the terminal when called'''
    print('\033[H\033[J')
    return

def winnerScreen(score1, score2):
    ''''Will show results of the game when a winner is determined'''
    
    print('\n' * 10 + "Scroll up to see game events.\n")
    print("Player One Score: " + "\033[34;1m" + f"{score1}" + Fore.RESET)
    print("Player Two Score: " + "\033[33;1m" + f"{score2}" + Fore.RESET)
    if score1 > score2:
        print("\033[34;1m" + "Player One Wins!\n" + Fore.RESET)
        turtle1 = turtle.Turtle()
        turtle1.write("PLAYER ONE WINS!", font =("Arial", 50, "normal"))
    elif score1 < score2:
        print("\033[33;1m" + "Player Two Wins!\n" + Fore.RESET)
        turtle1 = turtle.Turtle()
        turtle1.write("PLAYER TWO WINS!", font =("Arial", 50, "normal"))
    else:
        print("\033[35;1m" + "It's a Draw!\n" + Fore.RESET)
        turtle1 = turtle.Turtle()
        turtle1.write("IT'S A DRAW!", font =("Arial", 50, "normal"))
    
    print("Press 'M' key to return to menu.")
    print("Press 'Q' key to quit.")
    
    while True:
        if is_pressed('m'):
            clearConsole()
            menu()
            break
        elif is_pressed('q'):
            return print("\033[31;m" + "Game has been closed. Thank you for playing!" + Fore.RESET)

def playGame():
    ''''Code and logic for the actual game'''
    isPlayerOne = True
    isPlayerTwo = False
    playerOneTotal = 0
    playerTwoTotal = 0
    pointsThisTurn = 0
    round_count = 0
    my_file = open("game_log.txt", "w")
    print("Beginning game...")
    sleep(2)
    
    while playerOneTotal < 100 and playerTwoTotal < 100:
        round_count += 1
        while isPlayerOne:
            if playerOneTotal+pointsThisTurn < 100:
                print(Fore.BLUE + "Player One" + Fore.RESET + ", would you like to roll or stop? [" + "\033[32;1m" + "'R'" + Fore.RESET + " to roll, " + Fore.GREEN + "'H'" + Fore.RESET + " to hold, " + Fore.RED + "'Q'" + Fore.RESET + " to quit]", end = '')
                playerMove = input().lower()
                if playerMove == 'r':
                    dice = randint(1,6)
                    if dice == 1:
                        pointsThisTurn = 0
                        print(Fore.RED + "Rolled 1! No points gained!" + Fore.RESET)
                        isPlayerOne = False
                        isPlayerTwo = True
                    else:
                        pointsThisTurn += dice
                        if playerTwoTotal+pointsThisTurn < 100:
                            print("Rolled", Fore.BLUE + f"{dice}" + Fore.RESET, "\nPotential score now:", Fore.BLUE + f"{playerOneTotal+pointsThisTurn}" + Fore.RESET)
                        else:
                            break
                elif playerMove == 'h':
                    isPlayerOne = False
                    isPlayerTwo = True
                elif playerMove == 'q':
                    return print(Fore.RED + "Game has been closed. Thank you for playing!" + Fore.RESET)
                else:
                    print(Fore.RED + "Invalid move. Try Again." + Fore.RESET)
            else:
                break
                
        playerOneTotal += pointsThisTurn
        my_file.write("Player 1 earned ")
        my_file.write(str(pointsThisTurn))
        my_file.write(" points. Player 1 total now: ")
        my_file.write(str(playerOneTotal))
        my_file.write("\n")
        pointsThisTurn = 0
        
        print("\033[34;1m" + "Player One Total:",playerOneTotal, Fore.RESET)
        print(Fore.MAGENTA + "Player One round", round_count, "over.\n" + Fore.RESET)
        
        if playerOneTotal >= 100:
            print(Fore.BLUE + "Player One" + Fore.RESET + " has reached a 100 points!")
            print(Fore.YELLOW + "Player Two" + Fore.RESET + ", this is your last chance!")
            isPlayerTwo = True
        
        while isPlayerTwo:
            if playerTwoTotal+pointsThisTurn < 100:
                print(Fore.YELLOW + "Player Two" + Fore.RESET + ", would you like to roll or stop? [" + "\033[32;1m" + "'R'" + Fore.RESET + " to roll, " + Fore.GREEN + "'H'" + Fore.RESET + " to hold, " + Fore.RED + "'Q'" + Fore.RESET + " to quit]", end = '')
                playerMove = input().lower()
                if playerMove == 'r':
                    dice = randint(1,6)
                    if dice == 1:
                        pointsThisTurn = 0
                        print(Fore.RED + "Rolled 1! No points gained!" + Fore.RESET)
                        isPlayerOne = True
                        isPlayerTwo = False
                    else:
                        pointsThisTurn += dice
                        if playerTwoTotal+pointsThisTurn < 100:
                            print("Rolled", Fore.YELLOW + f"{dice}" + Fore.RESET, "\nPotential score now:", Fore.YELLOW + f"{playerTwoTotal+pointsThisTurn}" + Fore.RESET)
                        else:
                            break
                elif playerMove == 'h':
                    if playerOneTotal < 100:
                        isPlayerOne = True
                        isPlayerTwo = False
                    else:
                        isPlayerTwo = False
                elif playerMove == 'q':
                    return print(Fore.RED + "Game has been closed. Thank you for playing!" + Fore.RESET)
                else:
                    print(Fore.RED + "Invalid move. Try Again." + Fore.RESET)
            else:
                break
                
        playerTwoTotal += pointsThisTurn
        
        my_file.write("Player 2 earned ")
        my_file.write(str(pointsThisTurn))
        my_file.write(" points. Player 2 total now: ")
        my_file.write(str(playerTwoTotal))
        my_file.write("\n")
        pointsThisTurn = 0
        print("\033[33;1m" + "Player Two Total:", playerTwoTotal, Fore.RESET)
        print(Fore.MAGENTA + "Player Two round", round_count, "over.\n" + Fore.RESET)
    
    winnerScreen(playerOneTotal, playerTwoTotal)
    my_file.close()

def rules():
    ''''Will display rules to the Pig game'''
    print("\033[36;1m" + "How to play:" + Fore.RESET)
    print("- Player One rolls the dice first. They can keep going until they want to hold.")
    print("- The points earned is the sum of all dice rolls in that round.")
    print("- BUT, if you roll a one, you gain none of the points!")
    print("- After Player One, Player Two will get a chance to do the same.")
    print("- The Goal is to reach 100 points.")
    print("- If Player One reaches 100 first, Player Two will get one last chance to comeback.")
    print("- If Player Two gets a higher score on the final roll then Player Two wins.\n")
    print("Press " + Fore.RED + "'Esc' Key" + Fore.RESET + " to return to main menu.")
    while True:
        if is_pressed('esc'):
            clearConsole()
            menu()
            break
        elif is_pressed('q'):
            return print("\033[31;m" + "Game has been closed. Thank you for playing!" + Fore.RESET)
    return

def menu():
    ''''displays main menu of the game'''
    while True:
        print("Press " + "\033[36;1m" + "'P' Key" + Fore.RESET + " to select" + Fore.CYAN + "'Play Game'" + Fore.RESET)
        print("Press " + Fore.CYAN + "'O' Key" + Fore.RESET + " to select" + Fore.CYAN + "'How to Play'" + Fore.RESET)
        print("Press " + Fore.RED + "'Q' Key" + Fore.RESET + " at any point to " + Fore.RED + "Quit" + Fore.RESET)
        print("#=============================#")
        print("#          " + Fore.GREEN + "Game Menu" + Fore.RESET + "          #")
        print("#=============================#")
        print("#    " + Fore.CYAN + "Play Game---------[P]" + Fore.RESET + "    #")
        print("#    " + Fore.CYAN + "How to Play-------[O]" + Fore.RESET + "    #")
        print("#    " + Fore.RED + "Quit--------------[Q]" + Fore.RESET + "    #")
        print("#=============================#")
        while True:
            if is_pressed('p'):
                clearConsole()
                return playGame()
            elif is_pressed('o'):
                clearConsole()
                return rules()
            elif is_pressed('q'):
                return print(Fore.RED + "Game has been closed. Thank you for playing!" + Fore.RESET)


# Main Code
try:
    print("Welcome to this game of Pig!")
    print("Follow the instructions in order to play.")
    print("Press 'Enter' to advance to main menu.")
    while True:
        if is_pressed('Enter'):
            clearConsole()
            menu()
            break
except:
    print("Error Detected")
#