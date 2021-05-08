from dictionary import *
import os
from classes import *
from time import sleep

def clean(): #This function is useful to clean the screan
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def text_presentation(text): #This function presents the text in a animated way
    presented_text = ""
    for i in text:
        presented_text += i
        print(presented_text)
        sleep(0.05)
        clean()

def menu():
    clean()
    print("\tWellcome to the Morse Code Machine\n\n")
    choice = input("1 Codify\n2 Decodify\n3 Instructions\n4 Quit\nChoose a option: ")

    if choice == "1":
        codify_page()
    elif choice == "2":
        decodify_page()
    elif choice == "3":
        instructions_page()
    elif choice == "4":
        exit()

def codify_page():
    clean()
    morse_text = ""
    print("\tCodify your text\n")
    text = input("Insert your text down below:\n")
    for letter in text:
        letter_to_be_codified = Letter(letter)
        morse_text += letter_to_be_codified.corresponding_morse+" "
        del letter_to_be_codified
    print("Codified text: ", morse_text.capitalize())
    while True:
        restart = input("Would you like to try again? Insert \"yes\" to restart or \"no\" to quit: ")

        if restart.lower() == "yes":
            codify_page()
        elif restart.lower() == "no":
            menu()
        else:
            input("Invalid option. Try again.")


def decodify_page():
    text = []
    morse_char = []
    while True:
        clean()
        print("Helping table:\n")
    
        for x, y in decodify_dictionary.items():
            print(f"{x} = {y}")
        print("\nYou've inserted: ", "".join(morse_char))
        print("Translation: ", "".join(text))
        choice = input("\n\nEnter your morse code using the menu down below:\n\n1 Enter \".\" (dot)\n2 Enter \"-\" (dash)\n 3 End character \n4 End word\n5Erase last element \n6 Erase last translated letter\n7 Quit\nEnter your option: ")

        if choice == "1":
            morse_char.append(".")
        elif choice == "2":
            morse_char.append("-")
        elif choice == "3":
            charac = Morse("".join(morse_char))
            text.append(charac.corresponding_leeter)
            if text[-1] == None:  #This condition checks if the user's input is valid
               text.pop()
               morse_char = []
            else:
                morse_char = []
        elif choice == "4":
            text.append(" ")

        elif choice == "5":
            try:
                morse_char = []
            except:
                pass
        elif choice == "6":
            try:
                text.pop()
            except:
                pass
        elif choice == "7":
            exit()

        else:
            input("Invalid option. Try again.")

        

def instructions_page():
    instructions_text = "First of all, you need to choose the mode which you'd like to use. You can either enter 1 to codify from alphabet to morse code, or enter 2 to do the other way around. In the first mode, you just need to write the whole text at once, and the program will codify it all as soon as you hit enter. When decodifying, you need to insert each character one by one, by entering the option to each case."
    text_presentation(instructions_text)
    print(instructions_text)
    input("\nHit enter to return to the main menu ")
    menu()