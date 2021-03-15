import codecs
import os

path = r'C:\Users\STEFAN-PC\Desktop'

with codecs.open(os.path.join(path, 'text.txt'), encoding='utf-8') as fh:
	text = fh.read()

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