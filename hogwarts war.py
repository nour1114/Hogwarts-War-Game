import time
import random
#randnom func
houses=["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]
random=random.choice(houses)
if random=="Gryffindor":
    print("The Hat has chosen you to be a Gryffindor because you have the qualities of courage, chivalry, and daring.")
elif random=="Slytherin":
    print("The Hat has chosen you to be a Slytherin because you are cunning, resourceful, and ambitious.")
elif random=="Hufflepuff":
    print("The Hat chose you to be in Hufflepuff because you have the qualities of friendship, love, hard work, cooperation, and loyalty.")
elif random=="Ravenclaw":
    print("The Hat chose you to be in Ravenclaw because you have the qualities of intelligence, cunning and quick wit.")
#main func
from time import sleep
def print_pause(text):
    print(text)
    sleep(2)
#intro funcs  
def intro():
    print_pause("You hear explosions all around you, lights up the sky despite the onset of night, screams!")
    print_pause("You are now in the Hogwarts War!")
    print_pause("and today Hogwarts is witnessing its war with the Black Lord Voldemort and his followers, the Death Eaters.")
    print_pause("As a Hogwarts student, you cannot use the three forbidden spells of Crucio to torture, Imperio to control, and Avadacadafra to kill, otherwise your fate will be sealed Azkban.")
    print_pause("You have in your hand a magic wand made of elm wood with a dragon's heart inside and 9.5 inches long.")
    print_pause("You don't have much time.")
    print_pause("Beware!!!")
    print_pause("there is a Death Eater approaching you and wants to attack you!!!")
    print_pause("There are three spells and one of them can defend yourself.")
    user_choice=input("Enter 1 if you choose Rectrosembra to tickle, or enter 2 if you choose Experiamus to strip, or enter 3 Fullerae to heal.")
    #starting decisions
    choice_1="The Death Eater managed to dodge your spell and hit you with Avadacadvara!"
    choice_2="You managed to strip the Death Eater of his wand and now it's your turn to cast the attack spell!"
    choice_3="If you choose this spell, I'll tell you I'm sorry you don't belong at Hogwarts, you better go sell potatoes, I'm joking with you. Try again."
    while user_choice not in ["1","2","3"]:
        user_choice=input("enter 1,2,3:")
    #first decision
    if user_choice == "1":
        print(choice_1)
        #The decision to restart the game or not
        user_choice=input("whould you like to play again?,(y/n)") 
        choice_y="Hogwarts is your home, let's go back to play again " 
        choice_n="Hogwarts is your home. Come back anytime. We will always be waiting for you. See you later"
        while user_choice not in ["y","n"]:
            user_choice=input("enter y,n:")
        if user_choice =="y":
                print (choice_y)
                intro()
        while user_choice =="n":
                print(choice_n)
                break
    #second decision
    elif user_choice =="2":
        print(choice_2)
        print_pause("Now you must choose one spell out of three spells to attack the Death Eater and eliminate it without going to Azkban")
        #Decisions to end the game
        user_choice =input("Enter 1 if you choose Expecto Patronum to protect against Dementors, enter 2 if you choose Crucio to torture, or enter 3 if you choose Sectocembra to chop the enemy.") 
        choice_1="You summoned your Patrunam, but that didn't help, and the Death Eater managed to pick up his wand again and finish you off with Avadakadavra!!!.Try again"
        choice_2="You have successfully taken down the Death Eater, but welcome to Azkaban, you will spend the rest of your life there.Try again"
        choice_3="Congratulations You did a great job defending Hogwarts You successfully took down the Death Eater without soiling your hand with unforgivable spells Go back and fight"
        while user_choice not in ["1","2","3"]:
            user_choice=input("enter 1,2,3:")
        #The first decision
        if user_choice=="1":
            print(choice_1)
            #The decision to restart the game or not
            user_choice=input("whould you like to play again?,(y/n)") 
            choice_y="Hogwarts is your home, let's go back to play again " 
            choice_n="Hogwarts is your home. Come back anytime. We will always be waiting for you. See you later"
            while user_choice not in ["y","n"]:
                user_choice=input("enter y,n:")
            if user_choice =="y":
                print (choice_y)
                intro()
            while user_choice =="n":
                print(choice_n) 
                break
        #Second decision
        elif user_choice=="2":
            print(choice_2)
            #The decision to restart the game or not
            user_choice=input("whould you like to play again?,(y/n)") 
            choice_y="Hogwarts is your home, let's go back to play again " 
            choice_n="Hogwarts is your home. Come back anytime. We will always be waiting for you. See you later"
            while user_choice not in ["y","n"]:
                user_choice=input("enter y,n:")
            if user_choice =="y":
                print (choice_y)
                intro()
            while user_choice =="n":
                print(choice_n) 
                break
            #Third decision
        elif user_choice =="3":
            print(choice_3)
            #The decision to restart the game or not
            user_choice=input("whould you like to go back and fight?,(y/n)")
            choice_y="Hogwarts is your home, let's go back to play again " 
            choice_n="Hogwarts is your home. Come back anytime. We will always be waiting for you. See you later"
            if user_choice =="y":
                print (choice_y)
                intro()
            while user_choice =="n":
                print(choice_n)
                break
     #Third decision        
    elif user_choice =="3":
        print(choice_3)
        #The decision to restart the game or not
        user_choice=input("whould you like to play again?,(y/n)") 
        choice_y="Hogwarts is your home, let's go back to play again " 
        choice_n="Hogwarts is your home. Come back anytime. We will always be waiting for you. See you later"
        while user_choice not in ["y","n"]:
            user_choice=input("enter y,n:")
        if user_choice =="y":
            print (choice_y)
            intro()
        while user_choice =="n":
            print(choice_n)
            break
if __name__ == "__main__":
    intro()