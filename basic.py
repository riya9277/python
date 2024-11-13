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
#eg2
def divisor(x):
    def divident(y):
        return(y/x)
    return divident

divide=divisor(2)
print(divide(10))

#lambda

sum=lambda x,y:x+y
print(sum(4,2))

#sort

student=(("fina","A",23),
         ("kelly","B",20))
age=lambda ages:ages[2]
sortedstud=sorted(student,key=age)

for i in sortedstud:
    print(i)

#map
store=[("shirt",20.0),
       ("pants",40.0)]
to_euro=lambda data:(data[0],data[1]*0.82)
storeeuro=list(map(to_euro,store))
for i in storeeuro:
    print(i)

#filter

friends=[("rache",43),
         ("mia",12)]
age=lambda data:data[1]>=18
buddies=list(filter(age,friends))
for i in buddies:
    print(i)

# reduce()
import functools
Letters=["H","E","l","l","O"]
word=functools.reduce(lambda x,y:x+y,Letters)
print(word)

#List comprehension

squares=[i*i for i in range(1,11)]
print(squares)

stud=[34,90,56,20,100]
#pstud=list(filter(lambda x:x>60,stud))
#passedstud=[i for i in stud if i>=60]
passedstud=[i if i>=60 else "failed" for i in stud ]
print(passedstud)

#dictionary comprehension
cities={"NY":32,"USA":90}
CITIES={key:((value-32)*(5/9)) for (key,value) in cities.items()}
print(CITIES)

#ZIP FUNCTION
username=["raj","michel","ken"]
passw=["8uj#","89iu","9j89"]
login=["9-09-23","8-09-22","05-04-23"]

users=zip(username,passw,login)
for i in users:
    print(i)

#Threading

import threading
import time
print(threading.active_count())
print(threading.enumerate())

def eat_break():
    time.sleep(3)
    print("you eat")
def drink_coffee():
    time.sleep(4)
    print("you drink coffee")
def study():
    time.sleep(5)
    print("you study")

x=threading.Thread(target=eat_break,args=())
x.start()

y=threading.Thread(target=drink_coffee,args=())
y.start()

z=threading.Thread(target=study,args=())
z.start()

  #  eat_break()
   # drink_coffee()
    #study()
print(threading.active_count())
print(threading.enumerate())

import threading
import time

def timer():
    print()
    count=0
    while True:
        time.sleep(1)
        count+=1
        print("logged in",count)

x= threading.Thread(target=timer,daemon=True)
x.start()
anw=input("exit?")


