import sys
import codecs


text =  sys.stdin.read()
text = text.replace('.', ' .')
text = text.replace('? ', ' ?')
text = text.replace('! ', ' !')
text = text.replace('… ', '… ')
tetx = tetx.replace(' ', '\n')


f = codecs.open('tokenized_corpus.txt', 'w', 'utf-8')
f.write(text)
f.close()

