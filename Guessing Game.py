import random #Imports random thing for randomness
answer = (random.randint(1,100))
print("This script is a number guessing game")
print("Guess the number!")
guess = 100000 #May look stupid, but this is to absolutely make sure guess!=answer. 
guesses = 0

while(int(guess)!=answer):
   guess = input("Pick a number from 1 to 100:")
   if guess.isnumeric():
    guesses+=1
    if(int(guess)>answer):
     print("Too high!")

    elif(int(guess)<answer):
     print("Too low!")

    elif(int(guess)==answer):
     print("Well done!")
     print("You won using "+ str(guesses)+" guesses")
   else:
    print("This script only supports integers")
    guess = 100000








    
