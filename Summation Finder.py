import time
print("This script finds the summation from one to x") #Intro
x = input("Choose x:") #Prompts user to choose a value for adding
if x.isnumeric():
    x = int(x) #Converts to integer
    pairs = (x/2) # Finds number of pairs
    pairno = (x+1) # Finds sum of pairs
    allno = (pairs*pairno) # Finds sum
    pairsstr = str(pairs)
    print ("Pairs found:  " +pairsstr)
    pairsum = str(pairno)
    print ("Sum of pair:  " +pairsum)
    allnostr = str(allno)
    print ("The answer is " +allnostr)
else:
    print("This script only supports integers")
    time.sleep(2)
    exit()
