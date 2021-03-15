from tkinter import *
import tkinter as tk
import codecs
import os

def replacediac(text):
	new = list(text)

	for i in range(len(new)):
		if(new[i] == 'ă'):
			new[i] = 'a'
		if(new[i] == 'Ă'):
			new[i] = 'A'
		if(new[i] == 'Â'):
			new[i] = 'A'
		if(new[i] == 'â'):
			new[i] = 'a'
		if(new[i] == 'Î'):
			new[i] = 'I'
		if(new[i] == 'î'):
			new[i] = 'i'
		if(new[i] == 'Ș'):
			new[i] = 'S'
		if(new[i] == 'ș'):
			new[i] = 's'
		if(new[i] == 'Ț'):
			new[i] = 'T'
		if(new[i] == 'ț'):
			new[i] = 't'

	text = ''.join(new)

	return text

root = Tk()
root.geometry('800x600')

path = r'C:\Users\STEFAN-PC\Desktop'

with codecs.open(os.path.join(path, 'text.txt'), encoding='utf-8') as fh:
    #Label(root, text=replacediac(fh.read())).pack()
    T = Text(root, height = 5, width = 52)
    T.pack()
    T.insert(tk.END, replacediac(fh.read())) 

root.mainloop()