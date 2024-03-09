# Character Attributes
mower = {
    "money": 0,
    "tool": 0
}



# Tools Available
tools = [
    {"name": "teeth", "price": 0,"profit": 5},
    {"name": "scissors", "price": 5,"profit": 5}
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
    mower["money"] += tools[0]["profit"]
    print(f"You have ${mower["money"]}")
    win()
    
def upgrade():
    print("you upgraded")
    if mower["money"] >= tools[0]["price"]:
        mower["tool"] += 1
        print(f"You have upgraded to {tools[mower["tool"]]["name"]}")
    # elif mower["money"] <= tools[]
        # print(tools[mower["tool"]]["name"])    
    win()

def quit():
    print("game ends")

def win():
    actions()

actions()

