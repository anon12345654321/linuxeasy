#import data (Tkinter)
from Tkinter import *
#main
Alpha = Tk()
#gui configration (weith, hight, title, enz)
app = Frame(Alpha)
app.grid()
Alpha.title("wordlist line gen. non selective ")
Alpha.geometry("320x260")


#firts label
label1 = Label(Alpha, text="minimal lengt passwords")
label1.grid(row = 0, column =0)


#input %s
svalue = StringVar() 
w = Entry(Alpha,textvariable=svalue)
w.grid(row = 1, column = 0)

#second label
label2 = Label(Alpha, text="maximal lengt passwords")
label2.grid(row = 2, column = 0)

#input %r
rvalue = StringVar() 
v = Entry(Alpha,textvariable=rvalue)
v.grid(row = 3, column = 0)

#tirth label
label3 = Label(Alpha, text="all carracters that wil be generated")
label3.grid(row = 4, column = 0)

#input %sr
srvalue = StringVar() 
x = Entry(Alpha,textvariable=srvalue)
x.grid(row = 5, column = 0)

#fourth label
label4 = Label(Alpha, text="file name")
label4.grid(row = 6, column = 0)

#input %q
qvalue = StringVar()
y = Entry(Alpha,textvariable=qvalue)
y.grid(row = 7, column = 0)

#fifth label
label5 = Label(Alpha, text="  copy line below (crunch.....txt) to other terminal ")
label5.grid(row = 8, column = 0)

#sixth label
label6 = Label(Alpha, text = "  use control+c to copy & right klik, paste, to paste")
label6.grid(row = 9, column = 0)
#output
Text = Text(Alpha,width = 25, height = 1, wrap = NONE)
Text.grid(row = 10, column = 0, columnspan = 2)




def hardprintfirst():
	#all inputs to variables
	input1 = "crunch %s "   %svalue.get()
	input2 = "%s"   %rvalue.get()
	input3 = "%s"   %srvalue.get()
	input4 = "%s"   %qvalue.get()

	#all preconfiguered carracters
	car1 = " -o "
	car2 = " /root/Desktop/"
	car3 = ".txt"
	OUTPUT = (input1) + (input2) + " " +(input3) + (car1) + (car2) + (input4) + (car3)
	Text.delete(0.0,END)
	Text.insert(0.0,OUTPUT)

#button
try:
 bulletimg = PhotoImage(file="/pic/anonops.png")
 bulletimgCOMPRSD = bulletimg.subsample(21,21)
 hardprintbutton2 = Button(Alpha,text="generate wordlist line",command=hardprintfirst)
 hardprintbutton2.grid()
 hardprintbutton2.config(image=bulletimgCOMPRSD,compound=RIGHT)
except:
 hardprintbutton2 = Button(Alpha,text="generate wordlist line",command=hardprintfirst)
 hardprintbutton2.grid()








Alpha.mainloop()
