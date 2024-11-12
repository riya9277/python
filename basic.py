import random
while True:
    choices=["rock","paper","scissors"]
    computer= random.choice(choices)
    player=None
    while player not in choices:
        player=input()
    
    if(player==computer):
        print("tie")
    elif(player=="scissors"):
        if(computer=="paper"):
            print(computer)
            print("you win")
        if(computer=="rock"):
            print(computer)
            print("you loose")
    elif(player=="paper"):
        if(computer=="scissors"):
            print(computer)
            print("you loose")
        if(computer=="rock"):
            print(computer)
            print("you win")
    elif(player=="rock"):
        if(computer=="scissors"):
            print(computer)
            print("you win")
        if(computer=="paper"):
            print(computer)
            print("you loose")
    playagain=input("yes or no")
    if playagain!="yes":
        break

#    --------------------------------------------------------------
#walrus operator
foods=list()
while food:=input("enter food")!="exit":
    foods.append(food)
#---------------------------------------------------------------------
#higher order function

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text=func("hello")
    print(text)

hello(loud)
hello(quiet)