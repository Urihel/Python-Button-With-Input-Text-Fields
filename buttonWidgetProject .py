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

# how to call back to myClick function 

#in the Button() function you can pass an argument called command 
#with command you can assign it the value of you function name and 
#when the button is clicked you can have a function execute some code.
#in this example when you click the button a label is executed. inside 
# the label a message in the form of text is also execute 
myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick,fg="green",bg="grey")
myButton.pack()



root.mainloop()
