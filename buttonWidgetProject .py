from tkinter import *

root = Tk()
e = Entry(root,width=50,bg="skyblue",fg="white")
e.pack()

def myClick():
    #you can also use variables inside your click button function
    # so x = "hello"
    # so y = e.get()
   
    #myLabel = Label(root,text=f'{x} {y}')
    myLabel = Label(root,text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick,fg="green",bg="grey")
myButton.pack()



root.mainloop()
