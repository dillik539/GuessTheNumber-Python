import random
keepGoing = "y"
while(keepGoing == "y" or keepGoing =="Y"):
    number = random.randint(0,10)
    guessNo = int(input("Enter your guess: "))
    if(number == guessNo):
      print("Congratulations! Your guess is correct.")
      break
    if(guessNo>number):
        print("Your guess is high. Try again.")
    else:
        print("Your guess is low. Try again.")
    keepGoing = input("Do you want to continue the game? press y for yes.")
