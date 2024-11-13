#Temperature Scale-----------------------------------------------------
from tkinter import *
'''
def submit():
    print("temp is"+str(scale.get())+"degree")
window =Tk()

scale=Scale(window,
            from_=0 ,to=100,
            length=600
            ,orient=VERTICAL,
            font=('Consolas',20),
            tickinterval=10,
            showvalue=0,
            resolution=5,
            troughcolor='#FF1C00',
            fg='#FF1C00',
            bg='#111111')
scale.set(50)
scale.pack()

button=Button(window,text='submit',command=submit)
button.pack()
window.mainloop()

'''
#Listbox----------------------------------------------------------

'''
window=Tk()
def submit():
    food=[]
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    print("you ordered")
  
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


listbox=Listbox(window,
                bg="#f7ffde",
                font=("Contantis",35),
                width=12,
                selectmode=MULTIPLE)
listbox.pack

listbox.insert(1,"pizza")

listbox.insert(2,"pasta")

listbox.insert(3,"garlic bread")

listbox.insert(4,"soup")

listbox.insert(5,"salad")
listbox.config(height=listbox.size())
entryBox=Entry(window)
entryBox.pack()

submitButton=Button(window,text="submit",command=submit)
submitButton.pack()

addButton=Button(window,text="add",command=add)
addButton.pack()

delButton=Button(window,text="delete",command=delete)
delButton.pack()


'''

#colorchooser

'''

from tkinter import colorchooser
def click():
    color=colorchooser.askcolor()
    colorhex=color[1]
    window.config(bg=colorhex)

window =Tk()
window.geometry("420x420")
button =Button(txt='click me',command=click)
button.pack()
window.mainloop()

'''

#text area
'''
def submit():
    input=text.get("1.0",END)
    print(input)
window=Tk()
text=text=Text(window,
               bg="light yellow",
               font=("Ink Free",25),
               height=8,
               width=20,
               padx=20,
               pady=20,
               fg="purple")
text.pack()
button=Button(window,text="submit",command=submit)
button.pack()
window.mainloop()
'''

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath=filedialog.askopenfilename(initialdir="C:\Users\JIBIN_JOY\Desktop\github-riya",
                                         title="open file okay",
                                          filetypes=(("text files","*.txt"),
                                                     ("all files","*.*")) )
    file =open(filepath,'r')
    print(file.read())

window=Tk()
button=Button(text="Open",command=openFile)
button.pack()
window.mainloop()