Usrcoins = 10

def usrName():
    x=input("What is your name")
    return(x)

def greeting(y): 
    print("Welcome to 20!") 
    print(y)
    return (y)
greeting(usrName())

############# Hit or Stand ###########
function usrGame() {

    var choice = "y"
    var usrTotal = 0
    while (choice == "y" ) {
        var x = randInt()
        usrTotal = x + usrTotal
        if (usrTotal > 20) {    /* change score limit here*/
            break
        }

        choice = prompt(`You have ${usrTotal} points. Would you like to hit? Please only type y or n.`)

        while (choice != "y" && choice != "n"){
            choice = prompt(`You did not type y or n. You have ${usrTotal} points. Would you like to hit? Please only type y or n.`)
        }
    }

    return usrTotal

}
