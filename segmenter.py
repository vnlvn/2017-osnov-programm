import sys
import codecs


text =  sys.stdin.read()
text = text.replace('. ', '.\n')
text = text.replace('? ', '.\n')
text = text.replace('! ', '.\n')

f = codecs.open('segmented_corpus.txt', 'w', 'utf-8')
f.write(text)
f.close()

