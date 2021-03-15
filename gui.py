import tkinter as tk
from tkinter import *

def Take_Input():
	INPUT = inputtxt.get("1.0", "end-1c")
	#print(INPUT)

	new = list(INPUT)

	#print(new)

	for i in range(len(new)):
		if(new[i] == 'ă'):
			new[i] = 'a'
		elif(new[i] == 'Ă'):
			new[i] = 'A'
		elif(new[i] == 'Â'):
			new[i] = 'A'
		elif(new[i] == 'â'):
			new[i] = 'a'
		elif(new[i] == 'Î'):
			new[i] = 'I'
		elif(new[i] == 'î'):
			new[i] = 'i'
		elif(new[i] == 'Ș'):
			new[i] = 'S'
		elif(new[i] == 'ș'):
			new[i] = 's'
		elif(new[i] == 'Ț'):
			new[i] = 'T'
		elif(new[i] == 'ț'):
			new[i] = 't'

	text = ''.join(new)

	#Output.delete('1.0', END)
	Output.insert(END, text)

root= tk.Tk()

root.geometry("800x580")
root.title(" Replace Diactricics - Romanian Edition ")

l = Label(text = "Inlocuieste diacriticele") 
l.config(font=("Arial Black", 23))

inputtxt = Text(root, height = 30, width = 45, bg="light cyan")

Output = Text(root, height = 30, width = 45, bg="light yellow")

Display = Button(root, height = 2, width = 20, text = "Replace", command=lambda:Take_Input())

Delete = Button(root, text='Clear Output', height = 2, command=lambda: Output.delete(1.0, END))

l.pack()
inputtxt.place(x=10,y=40)
Output.place(x=423,y=40)
Display.place(x=320,y = 530)
Delete.place(x=708, y= 530)

root.mainloop()