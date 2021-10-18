import random

play = "Yes"

def Game(c, p):
    if(c == p):
        return None
    if(c == 'g'):
        if(p == 's'):
            return False
        if(p == 'w'):
            return True
    if(c == 'w'):
        if(p == 'g'):
            return False
        if(p == 's'):
            return True
    if(c == 's'):
        if(p == 'w'):
            return False
        if(p == 'g'):
            return True
         
name = input("Enter your name : ")
round = int(input(("Enter how many rounds you want to play with Computer : ")))    
draw = won = lost = 0  
for item in range(round):
    print("\n*********************************************\n")
    print("Computer is Choosing...")
    i = random.randint(1, 3)
    print("Computer has Choosen!")
    if (i == 1):
        comp = "s"
    if (i == 2):
        comp = "w"
    if (i == 3):
        comp = "g"
    player = input("Your turn to Choose :\n1.For Choosing Snake - Press 's'\n2.For Choosing Water - Press 'w'\n3.For Choosing Gun   - Press 'g'\n")
    result = Game(comp,player)
    print(f"You have Choosed '{player}' and Computer had Choosen '{comp}'")
    if result == None:
        print("The Game was Draw as you both had choosen the same.\n")
        draw += 1
    if result == True:
        print("You Won!\n")
        won += 1
    if result == False:
        print("You Lost!\n")
        lost += 1
    
with open("result.txt", "a") as f:
    f.write(f"{name.upper()} played {round} matches and result is : \nWon = {won}\nLost = {lost}\nDraw = {draw}\n\n\t*********\n\n")


