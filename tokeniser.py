import codecs
import sys


with open('segmented_corpus.txt') as f:
    text = f.readlines()
#f = codecs.open('tokenized_corpus.txt', 'a', 'utf-8')
tokenized_text = ''

sent_counter = 1
for line in text:
	line = line.strip()
	if line == '':
		continue
	if line == ' ':
		continue	
	tokenized_text += '# sent_id = %d\n' % (sent_counter)
	sent_counter += 1
	tokenized_text += '# text = %s\n' % (line)
	line = line.replace('.', ' .')
	line = line.replace(',', ' ,')
	line = line.replace('?', ' ?')
	line = line.replace('!', ' !')
	line = line.replace('…', ' …')
	line = line.replace(':', ' :')
	line = line.replace(';', ' ;')
	line = line.replace('(', '( ')
	line = line.replace(')', ' )')
	line = line.replace('"', ' "')
	line = line.replace("'", " '")
	line = line.split(' ')
	word_counter = 1
	for i in line:
		tokenized_text += '%d\t' % (word_counter)
		tokenized_text += '%s\t_\t_\t_\t_\t_\t_\t_\t_\n' % (i)
		word_counter += 1
	tokenized_text += '\n'

sys.stdout.write(tokenized_text)
