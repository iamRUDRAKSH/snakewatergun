#SNAKE WATER GUN GAME
import random
name = input("Enter your name : ")
print("Press 's' for snake, 'w' for water and 'g' for gun\n")
print("Person to score 5 points first wins")
cscore = 0
pscore = 0
print("LETS START!!\n")
cinputs = ['s', 'w', 'g']
while(pscore != 5 and cscore != 5):
    pip = input("Enter your choice : ")
    cip = random.choice(cinputs)
    if cip == 's':
        if pip == 'w' or pip == 'W':
            print("Computer chose snake and you chose water\n")
            print("You lose")
            cscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 'g' or pip == 'G':
            print("Computer chose snake and you chose gun\n")
            print("You win")
            pscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 's' or pip == 'S':
            print("Computer chose snake and you chose snake\n")
            print("It's a tie")
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        else:
            print("Invalid input")
    elif cip == 'w':
        if pip == 'w' or pip == 'W':
            print("Computer chose water and you chose water\n")
            print("It's a tie")
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 'g' or pip == 'G':
            print("Computer chose water and you chose gun\n")
            print("You lose")
            cscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 's' or pip == 'S':
            print("Computer chose water and you chose snake\n")
            print("You win")
            pscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        else:
            print("Invalid input")
    elif cip == 'g':
        if pip == 'w' or pip == 'W':
            print("Computer chose gun and you chose water\n")
            print("You win")
            pscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 'g' or pip == 'G':
            print("Computer chose gun and you chose gun\n")
            print("It's a tie")
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        elif pip == 's' or pip == 'S':
            print("Computer chose gun and you chose snake\n")
            print("You lose")
            cscore += 1
            print(f"Your score = {pscore}  computer score = {cscore}\n")
        else:
            print("Invalid input")

if(pscore == 5):
    print("Congratulations!! You win!!\n\n")
elif(cscore == 5):
    print("Sorry!! You lose!!\n")
    print("Better luck next time\n")

print("End of the game!!\n\n")    

            


                
            


