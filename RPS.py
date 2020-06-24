from random import choice
while True:
    print("Winning Rules of the Rock paper scissor game as follows:\nRock vs paper->paper wins\nRock vs scissor->Rock wins\npaper vs scissor->scissor wins")
    print("Enter you choice\n1.Rock\n2.Paper\n3.Scissor")
    user=input("Users turn")
    print("Now is computer turn")
    computer=choice(["Rock","Paper","Scissor"])
    print("Computer's choice is",computer)
    if user=="1":
        userchoice="Rock"
    elif user=="2":
        userchoice="Paper"
    elif user=="3":
        userchoice="Scissor"
    print(userchoice,"vs",computer)
    if userchoice==computer:
        print("draw, please try again")
        continue
    elif userchoice=="Rock":
        if computer=="Paper":
            print("Paper win --> computer win")
        else:
            print("Rock win --> user win")
    elif userchoice=="Paper":
        if computer=="Scissor":
            print("Scissor win --> computer win")
        else:
            print("Paper win --> user win")
    elif userchoice=="Scissor":
        if computer=="Rock":
            print("Rock win --> computer win")
        else:
            print("Scissor win --> user win")
    else:
        print("please try again")
    again=input("Try again? Y/N")
    if again =="N":
        break