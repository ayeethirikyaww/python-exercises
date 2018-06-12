from sys import exit

def home():
    print("You go back to home.")
    print("What are you ride?")
    choice=input("> ")
    if "horse" in choice:
        dead("I ride horse")
    elif "Cow" in choice:
        dead("I ride Cow")
    else:
        print("I walk")
        exit(0)

def candy_room():
    print("There are many candies here.")
    print("This candies are dangerous.")
    print("So,you don't eat.If ate you don't free")
    print("eat or not eat?")
    noeat_candy=False

    while True:
        choice=input("> ")
        if choice=="eat candy":
            dead("You don't free from witch")
        elif choice=="not eat candy":
            print("You free and go to door")
            print("You go back home")
            noeat_candy=True
            home()
        else:
            print("I got no idea what that means.")

def witch_home():
    print("Here you see the great evil witch")
    print("She, it whatever stares at you.")
    print("Do you flee you life or eat your body?")

    choice=input("> ")
    if "flee" in choice:
        start_flee()
    elif "body" in choice:
        dead("Well that was tasty!")
    else:
        witch_home()


def dead(why):
    print(why,"Good job!")
    exit(0)

def start_flee():
    print("You are in witch home")
    print("There is a door that through candy room")
    print("If you through candy room ,you press 'Yes' and if you don't through you prees 'No'")
    choice=input("< ")
    if choice=="Yes":
        candy_room()
    elif choice=="No":
        witch_home()
    else:
        dead("You don't free from witch's home until you die.")


start_flee()

