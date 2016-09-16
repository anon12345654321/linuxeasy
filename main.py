from Tkinter import *
Alpha = Tk()
window = Frame(Alpha)
window.grid
Alpha.title("hoofdmenu")
try:
 import sys, os, ntpath, signal, re, subprocess 
 import Queue
except:
 print"FOUT:  import fout"

def catpy():
 try:
  from catswitch import *
  print "[-] import catswitch.py"
  print "[-] import correct"
 except:
  print "FOUT: kan bestand niet importeren, probeer opnieuw"  

def crunchpy():
 try:
  from crunch import *
  print "[-] import crunch.py"
  print "[-] import correct"
 except:
  print"FOUT: kan bestand niet importeren, probeer opnieuw"



catButton = Button(Alpha, text = "cat  ", command=catpy)
catButton.grid(row = 2, column = 1, sticky = W)

crunchButton = Button(Alpha, text = "crunch",command=crunchpy)
crunchButton.grid(row = 3, column = 1, sticky = W)




Alpha.mainloop()
