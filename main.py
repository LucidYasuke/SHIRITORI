import random
from words import dictionary_words, usable_quote
import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

"""
The class is here two specify a players name, used words, points, and mistake
It changes as the game changes and it is helpful for accessing information without creating multiple variable
"""


class Player:
    def __init__(self, name, used_words, points, mistakes):
        self.name = name
        self.used_words = used_words
        self.points = points
        self.mistakes = mistakes


all_used_words = []
used_words_one = []
used_words_two = []

""" 
Using a import time module and a for loop, create an unsymmetrical time interval so that the code isn't constant wait time
"""


def wait(num):
    change = num * .125
    for i in range(random.randint(2,6)):
        change * 2
    time.sleep(change)


def prelude_game(num):
    # PLAYER ORGANIZE
    """
    Using the class created above, we asses player one and two names, give them each a unique

    """
    print(f"{Fore.RED}{Style.BRIGHT}Big Brain Word Chain{Style.RESET_ALL}")
    wait(num)

    print(f"Shiritori [Shee-ree-toh-ree] is a japanese word chain game that involves kana")
    wait(num)
    print(f"This game takes inspiration from Shiritori but using english words and letters")
    wait(num)
    print(f"This is a two player game, the first person to play will be selected at random")
    wait(num)
    print(f"The next player will use the last letter of your word as the beginning letter for their word")
    wait(num)
    print(f"If you make two mistakes during your turn, the other person will get a chance to steal your point\n")
    wait(num)

    global player_one
    player_one = input("Your Name Player 1?: ")
    global one
    one = Player(player_one, used_words_one, 0, 0)
    wait(1)

    global player_two
    player_two = input("Your Name Player 2?: ")
    global two
    two = Player(player_two, used_words_two, 0, 0)
    time.sleep(1)

    print(f"\nPlayer 1: {Fore.MAGENTA}{one.name}!")
    time.sleep(.5)
    print(f"Player 2: {Fore.YELLOW}{two.name}!\n")
    time.sleep(1)

    """
    This sets the game point of the Game
    """
    while True:
        global final_point
        final_point = input(
            f"How many points do you want to be max points\n {Fore.BLUE}7{Fore.RESET} Points / {Fore.BLUE}15{Fore.RESET} Points / {Fore.BLUE}21{Fore.RESET} Points \nMax Points:  ")
        if final_point == "7":
            final_point = 7
            print(f"Game Final Point is {final_point}\n")
            break
        elif final_point == "15":
            final_point = 15
            print(f"Game Final Point is {final_point}\n")
            break
        elif final_point == "21":
            final_point = 21
            print(f"Game Final Point is {final_point}\n")
            break
        else:
            print(f"\n")
            continue

    """
    This sets the players into a list so that it is easier for more to randomize
    The turn is mainly for later on in the code for an if/else statement, but it also tells who goes first
    """
    global players
    players = [one, two]
    global turn
    turn = random.choice(players)

    if turn == one:
        print(f"{Fore.MAGENTA}{turn.name}{Fore.RESET} goes first!\n")
    elif turn == two:
        print(f"{Fore.YELLOW}{turn.name}{Fore.RESET} goes first!\n")

    # New_letter
    """
    This is an important step and in the prelude because it is only happens once
    In another python file, there is a list with all 26 letter in lowercase
    A random letter for the first word in the word chain is given
    The quotes is a random choice from a quotes list in another section that is used  
    """
    global new_letter
    new_letter = random.choice(dictionary_words.letters)
    print(random.choice(usable_quote.quotes))
    time.sleep(1)
    print(f"\nLETTER: {Fore.RED}{new_letter}")
    time.sleep(1)

    print(
        f'\nTo quit enter "-1"! To see all words used enter "-2"! To see all words used by current player enter "-3"\n')


# Core
"""
Shiritori [shee-ree-toh-ree] is a japanese word chain game that uses the last kana to create a new word and repeats
This is an English version using the last letter of a word
"""


def shiritori():
    global new_letter
    global turn
    global given_word
    """
    Turn is randomized at the beginning of the game so this first if-elif checks if the turn is player one or player two turn
    The code for both versions are similar besides minor tweaks to change values to the specified player
    """
    if turn == one:
        while True:
            """
            As long as the player does not have 2 mistakes they can try and add a new word to the chain
            When the player has 2 mistakes, the else statement resets their value to 0 and switches the turn to the other player for them to play
            """
            if one.mistakes < 2:
                """
                The given word is an input by the user, using f-strings to make the ode cleaner, the player name is said and is asked for a word that starts with the new_letter
                1. If the given word == '-1', that is a be
                """
                given_word = input(
                    f"{Fore.MAGENTA}{turn.name}{Fore.RESET} give us a word that starts with {Fore.RED}{new_letter}: ")
                if given_word == '-1':
                    quit()

                elif given_word == '-2':
                    print(f"\n{all_used_words}")
                    continue

                elif given_word == '-3':
                    print(f"\n{one.used_words}")
                    continue

                elif given_word.lower().startswith(new_letter):
                    if given_word.lower() not in all_used_words:  # if the word given by the player is not used, the code proceeds
                        if given_word.lower() not in dictionary_words.words:  # If the word was not in used words but is also not in dictionary words the code will add a mistake to player and continue the loop
                            print(f"69000 words and yet your word is not in our dictionary!\n")
                            one.mistakes += 1
                            continue

                        else:  # If the player hit all the right criteria, they will gain a point, the words will be added to their words and all words, and the last letter of the word will be take for the next word in the word chain
                            all_used_words.append(given_word.lower())
                            one.used_words.append(given_word.lower())
                            one.points += 1
                            print(f"{given_word}\n")

                            """
                            The word is turned into a list, and the the last letter is take, [-1], 
                            and then joined back into new_letter for the next person, the turn is the chanegd
                            """
                            string_word = list(given_word.lower())
                            letter = string_word[-1]
                            new_letter = ("").join(letter)
                            turn = two
                            break

                    else:  # A mistake is given if the word has been used
                        print(f"Word has already been used!\n")
                        one.mistakes += 1
                        continue

                elif not given_word.lower().startswith(
                        new_letter):  # If the given_word has not hit the first criteria, starting with the new_letter, a mistake is gicen and loop continued
                    print(f"Word does not start with {Fore.RESET}{new_letter}\n")
                    one.mistakes += 1
                    continue
            else:
                one.mistakes = 0
                turn = two
                break

    elif turn == two:
        while True:
            """
            As long as the player does not have 2 mistakes they can try and add a new word to the chain
            When the player has 2 mistakes, the else statement resets their value to 0 and switches the turn to the other player for them to play
            """
            if two.mistakes < 2:
                given_word = input(
                    f"{Fore.YELLOW}{turn.name}{Fore.RESET} give us a word that starts with {Fore.RED}{new_letter}: ")
                if given_word == '-1':
                    quit()

                elif given_word == '-2':
                    print(f"\n{all_used_words}")
                    continue

                elif given_word == '-3':
                    print(f"\n{two.used_words}")
                    continue

                elif given_word.lower().startswith(new_letter):
                    if given_word.lower() not in all_used_words:  # if the word given by the player is not used, the code proceeds
                        if given_word.lower() not in dictionary_words.words:  # If the word was not in used words but is also not in dictionary words the code will add a mistake to player and continue the loop
                            print(f"69000 words and yet your word is not in our dictionary!\n")
                            two.mistakes += 1
                            continue

                        else:  # If the player hit all the right criteria, they will gain a point, the words will be added to their words and all words, and the last letter of the word will be take for the next word in the word chain
                            all_used_words.append(given_word.lower())
                            two.used_words.append(given_word.lower())
                            two.points += 1
                            print(f"{given_word}\n")

                            """
                            The word is turned into a list, and the the last letter is take, [-1], 
                            and then joined back into new_letter for the next person, the turn is the chanegd
                            """
                            string_word = list(given_word.lower())
                            letter = string_word[-1]
                            new_letter = ("").join(letter)
                            turn = one
                            break

                    else:  # A mistake is given if the word has been used
                        print(f"Word has already been used!\n")
                        two.mistakes += 1
                        continue

                elif not given_word.lower().startswith(
                        new_letter):  # If the given_word has not hit the first criteria, starting with the new_letter, a mistake is gicen and loop continued
                    print(f"Word does not start with {Fore.RED}{new_letter}\n")
                    two.mistakes += 1
                    continue
            else:
                two.mistakes = 0
                turn = one
                break


def run_shiritori(num):
    prelude_game(num)
    while (one.points < final_point and two.points < final_point) or given_word == "-1":
        shiritori()

    print(f"\n{Fore.MAGENTA}{one.name}{Fore.RESET} has {Fore.BLUE}{one.points}{Fore.RESET} points!")
    print(f"\n{Fore.YELLOW}{two.name}{Fore.RESET} has {Fore.BLUE}{two.points}{Fore.RESET} points!\n")

    print(f"All words used: {all_used_words}\n")
    print(f"All words used by {Fore.MAGENTA}{one.name}{Fore.RESET} {one.used_words}\n")
    print(f"All words used by {Fore.YELLOW}{two.name}{Fore.RESET} {two.used_words}\n")

    if one.points > two.points:
        print(f"{Fore.MAGENTA}{one.name}{Fore.RESET} WINS!")
    elif one.points < two.points:
        print(f"{Fore.YELLOW}{two.name}{Fore.RESET} WINS!")


run_shiritori(1)
