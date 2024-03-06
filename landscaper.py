# Character Attributes
mower = {
    "money": 0,
    "weapon": 0
}

# Tools Available
tools = [
    {"name": "teeth", "price": 0,"profit": 1},
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
    mower["money"] += 1
    print(mower["money"])
    win()
    
def upgrade():
    print("you upgraded")
    mower["tools"] += 1
    print(tools[mower["tools"]])
    win()

def quit():
    print("game ends")

def win():
    actions()

actions()