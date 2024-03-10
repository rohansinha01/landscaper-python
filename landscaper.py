# Character Attributes
mower = {
    "money": 0,
    "tool": 0,
    "winner": False
}



# Tools Available
tools = [
    {"name": "teeth", "price": 0,"profit": 1},
    {"name": "scissors", "price": 5,"profit": 5},
    {"name": "push lawnmower", "price": 25,"profit": 50},
    {"name": "battery powered lawnmower", "price": 250,"profit": 100},
    {"name": "team of starving students", "price": 500,"profit": 250},
]

# Functions

def actions(): 

    result = input("do you want [m]ow, [u]pgrade, or [q]uit? ")

    if(result == "m"):
        mow()
        return 1
    
    if(result == "u"):
        upgrade()
        return 1
    
    if(result == "q"):
        quit()
        return 1
    
    print("no valid options given")
    
    actions()
   

def mow():
    print("you mowed")
    # print(tools[1]["profit"])
    mower["money"] += tools[mower["tool"]]["profit"]
    print(f"You have ${mower["money"]}")
    win()
    
def upgrade():
    if mower["tool"] + 1 < len(tools) and  mower["money"] >= tools[mower["tool"]]["price"]:
        mower["tool"] += 1
        mower["money"] -= tools[mower["tool"]]["price"]
        print(f"You have upgraded to {tools[mower["tool"]]["name"]}")
        print(f"You have ${mower["money"]}")
    elif mower["money"] < tools[mower["tool"]]["price"]:
        print('You do not have the funds')   
    else: print("No more items to buy!")
    
    win()

def quit():
    print("game ends")

def win():
    if mower["money"] > 1000 and mower["tool"] == 4:
        mower["winner"] = True
        print("You win!")
    else: actions()


actions()



