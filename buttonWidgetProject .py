#thanks codemy and freeCodeCamp.org for this awesome code on how to use tkinter.

from tkinter import *

root = Tk()
e = Entry(root,width=50,bg="skyblue",fg="white")
e.pack()

def myClick():
    #Since python is super flexiable and an OOPs language you can 
    #pass an argument inside of Label() called text which allows 
    #to create some text inside that label. great thing about the text
    #argument is that you can concatinate strings with built in functions like in OOPs
    #so in this case .get() which retrieves the text that you enter into our Entry() function 
    #so our input text fields. In the code below i have 2 examples one using fstring and another 
    #using concatination. the reason i chose to use fstring is becuase since we are talking OOPs
    #why not see if fstring also works as a value for the text argument. so yes you can use fstring
    #as a value and have it do the same thing that you would with the code that is not commented out
    #in the myClick function. 
    
    
    #you can also use variables inside your click button function
    # so x = "hello"
    # so y = e.get()
   
    #myLabel = Label(root,text=f'{x} {y}')
    myLabel = Label(root,text="Hello " + e.get())
    myLabel.pack()

# how to call back to myClick function 

#in the Button() function you can pass an argument called command 
#with command you can assign it the value of your function name and 
#when the button is clicked you can have a function execute some code.
#in this example when you click the button a label is executed. inside 
# the label a message in the form of text is also execute 
myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick,fg="green",bg="grey")
myButton.pack()



root.mainloop()
