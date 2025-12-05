
#for the random number generator 
import random

print("This is Rock Paper Scissors!")
print("I will generate a choice then you can choose yours")
print("If you beat me you get a Cookie!\n")
print("Here are the choices:"
      "1 = rock" \
      "2 = paper" \
      "3 = scissors")
print("I've chosen, now it's your turn!")

# COUNTERS
winCount = 0
lossCount = 0
roundCount = 1

# WHILE CONDITION CONTROLLER
exit = False
while exit == False:
    compC = random.randint(1, 3)

    print("Round " + str(roundCount))

    strCheck = False
    while strCheck == False:
        userC = input("Choose!: ")
        if not userC.isdigit():
         print("Guess must be a integer")
         continue 
    
        userC = int(userC)
        if userC >= 1 and userC <= 3:
           break 
        else:
           print("Choice must be between 1, 2 or 3")
           continue
            
    # 1 wins against 3      
    # 2 wins against 1
    # 3 wins against 2

    # TIE CASE
    if userC == compC:
       print("It's a tie!")

    # WIN CASES
    if userC == 1 and compC == 3:
       print("You won!")
       winCount += 1
       roundCount += 1

    if userC == 2 and compC == 1:
       print("You won!")
       winCount += 1
       roundCount += 1

    if userC == 3 and compC == 2:
       print("You won!")
       winCount += 1
       roundCount += 1
    
    # EVERYTHING ELSE IS A LOSS
    else:
       print("You lost gang HAHA!")
       lossCount += 1
       roundCount += 1
    
    
    # ASKING TO LEAVE
    leave = input("Would you like to leave? Yes/No: ")
    if leave == "Yes" or leave == "y" or leave == "yes":
        exit = True
    if leave == "No" or leave == "n" or leave == "no":
        continue
    if exit == True:
        break 