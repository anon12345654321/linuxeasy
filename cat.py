from Tkinter import *
Alpha = Tk()
app = Frame(Alpha)
app.grid()



#looks && butons && labels && inputs && outputs
Alpha.title("file creator")

label1 = Label(Alpha, text = "		create files")
label1.grid(row = 1, column = 1, sticky = W, columnspan = 15)

label2 = Label(Alpha, text = "NAME FILE")
label2.grid(row = 2, column = 1, sticky = W, columnspan = 15)

label3 = Label(Alpha, text = "TYPE FILE")
label3.grid(row = 2, column = 2, sticky = W, columnspan = 15)

avalue = StringVar()
z = Entry(Alpha,textvariable=avalue)
z.grid(row = 3, column = 1, sticky = W)

bvalue = StringVar()
y = Entry(Alpha, textvariable=bvalue)
y.grid(row = 3, column = 2, columnspan = 15, sticky = W)

output1 = Text(Alpha,width = 47, height = 1,wrap = NONE)
output1.grid(row = 5, column = 0, columnspan = 15, sticky = W)

def help():
 Alpha1 = Tk()
 app = Frame(Alpha1)
 app.grid()
 Alpha1.title("help")



 label11 = Label(Alpha1, text = "help")
 label11.grid()
 label12 = Label(Alpha1, text = "copy &paste  genererated line (to new terminal)\ncontr + c for copy, right mouse klik then -paste- to paste\n  ")
 label12.grid()
 label13 = Label(Alpha1, text = "examples for second input (TYPE FILE):\ntxt for text file\npy for python file\n ")
 label13.grid()



 Alpha1.mainloop()


def command1():
 print"all correct"
 input1 = "%s" %avalue.get()
 input2 = "%s" %bvalue.get()
 OUTPUT = ("cat > ") + (input1) + (".") + (input2)
 output1.delete(0.0,END)
 output1.insert(0.0,OUTPUT)





button1 = Button(Alpha, text = "generate",command=command1)
button1.grid(row = 4, column = 1)

button2 = Button(Alpha, text = "help",command=help)
button2.grid(row = 4, column = 2)

Alpha.mainloop()

