#Selection sort, by LemonboyC3
#Sorts data WITHOUT using .sort() (No cheating, you could read the code!)
import random
global unsorted
unsorted = []
global sorteditems
sorteditems = []
itemsinlist="SuperMario" #Make sure that variable isn't numeric
print ("Selection sort") #Prompt the amount of items in list
while not itemsinlist.isnumeric():
 itemsinlist = input("Amount of items in list:")
 if not itemsinlist.isnumeric():
  print("Please input an integer")


x = itemsinlist
y = 0
print("Add items to list. Input random for a random list")
ifrandom = input("Random?")
if(str(ifrandom)=="random"):
 while(y<int(x)):
  unsorted.append(y+1)
  y+=1
 random.shuffle(unsorted)
else:
 while (y < int(x)): #Add items in list
  itemtoadd = input("Item in list:")
 if not itemtoadd.isnumeric():
  print("Please input an integer")
 elif itemtoadd.isnumeric:
  unsorted.append(itemtoadd)
  y += 1


print("Unsorted " + str(unsorted))
unsorted = list(map(int, unsorted)) #Stole *ahem* borrowed off internet, this turns the strings to integers


while(len(unsorted)!=0):# The sort!
 
 thingtomove = 0
 thingtomove = min(unsorted)
 sorteditems.append(thingtomove)
 unsorted.remove(thingtomove)
 print (thingtomove)
 thingtomove = 0

print("Sorted "+ str(sorteditems))

  
