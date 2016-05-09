nice = 0
mean = 0

def main():
    start()

def start():
    print "Hello and welcome to nice or mean!"
    name = raw_input ("What's your name? : ")
    print "Hi and welcome, "+name+"!"
    print "In this game, you will be greeted by several different people. You can treat them nicely or you can be mean."
    print "At the end of the game your fate will be determined by how you act."

    choice = raw_input("Do you want to play? y/n ")

    if choice =="y":
        print "Great! Use 'm' for mean and 'n' for nice!"
        begin()

    if choice =="n":
        print "Okay, byeeeeeeee"

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job - you win! Everyone loves you and you live in a palace!"
        choice = raw_input ("Do you want to play again? y/n ")

        if choice =="y":
            print "Okay let's go!"
            nice = 0
            begin()

        if choice =="n":
            print "Okay, byeeeeeee"
            exit()

    if mean > 2:
        print "Too bad - game over! You now live in a van down by the river with no friends!"

        choice = raw_input("Do you want to play again? y/n ")

        if choice =="y":
            print "Okay let's go!"
            mean = 0
            begin()

        if choice =="n":
            print "Okay, byeeeeee"
            exit()

        elif choice != "y"+"n":
            print "Please enter y or n, you big butthead!"

            if choice =="y":
                begin()
            if choice =="n":
                print "byeeee bitch!"
                exit()

            if choice != "y"+"n":
                choice = raw_input("Do you really want to play again? y/n ")

    pick = raw_input("Someone approaches you to talk. Will you be nice or mean? n/m ")

    if pick =="n":
        print "They smile, wave and walk away."
        nice = nice+1
        print "You currently have " +str(nice) + " nice."
        begin()


    if pick =="m":
        print "They frown, glare at you, and storm off."
        mean = mean+1
        print "You currently have " +str(mean) + " mean."
        begin()


start()
