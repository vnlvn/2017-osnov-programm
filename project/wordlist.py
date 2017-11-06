frequency = {}

def import_file(fname):
	#read line by line and make a frequency dictionary
	with open('fname') as f:
	for line in f.readlines():
		row = line.split(': ')
		transliteration[row[0]] = row[1].strip()

def add_another_file(fname):
	#if in dictionary: += frequency
	#if not in dictionary: add

def output(fname):
	#write the dictionary into a file

def main():
	import_file(/home/apertium/2017-osnov-programm/project/wordlist-ivelt.txt)
	add_another_file(/home/apertium/2017-osnov-programm/project/wordlist-kaveshtiebel.txt)
	output(???) #

main()