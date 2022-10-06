import random

Usrcoins = 10



def usrName():
    x=input("What is your name?")
    return(x)

def greeting(y): 
    print("Welcome to 20!") 
    print(y)
    return (y)
greeting(usrName())

def randInt():
    return random.randint(1 , 10)
print(randInt())
   

   
############# Hit or Stand ###########
compTotal = 0
choice = "y"
usrTotal = 0
while (choice == "y" ):
    x = randInt()
    usrTotal = x + usrTotal
    if (usrTotal > 20):   # change score limit here #
        print("you loose")
        break
        

    choice = input("You have " +str(usrTotal)+ " points. Would you like to hit? Please only type y or n.")

    while (choice != "y" and choice != "n"):
        choice = input("You did not type y or n. You have " +str(usrTotal)+ " points. Would you like to hit? Please only type y or n.")


    ############# computer numbers ###########

    x = randInt()
    compTotal = x + compTotal
    print(compTotal)
    if (compTotal > 20):    # change score limit here for the computer #
        print("you win")
        break






 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 # COMPBUST =  True