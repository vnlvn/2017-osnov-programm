import sys
#print('getting started')

transliteration = {}

with open('transliteration_table.txt') as f:
	for line in f.readlines():
		row = line.split('\t')
		transliteration[row[0]] = row[1].strip()
	#print('I know how to transliterate')

transliterated_text = ''
for line in sys.stdin.readlines(): 
	#print(line)
	for i in transliteration:
		line = line.replace(i, transliteration[i])
	#print(line.__class__)
	#print(line)
	transliterated_text += line
	#print("I've read a line")

sys.stdout.write(transliterated_text)
