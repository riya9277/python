
from tkinter import *

def submit():
    print("temp is"+str(scale.get())+"degree")
window =Tk()

scale=Scale(window,from_=0 ,to=100)
scale.pack()

button=Button(window,text='submit',command=submit)
button.pack()
window.mainloop()