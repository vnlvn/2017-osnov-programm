import sys
import codecs


text =  sys.stdin.read()
for i in '!.?…':
	text = text.replace(i + ' ', i + '\n')


f = codecs.open('tokenized_corpus.txt', 'w', 'utf-8')
f.write(text)
f.close()

