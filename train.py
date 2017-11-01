import sys


tokens = []
pos = []
# read the line by line
for line in sys.stdin:
	#print(line)
	if '\t' not in line:
		continue
	#if 'sent_id = 103' in line:
	#	break
	#print(line)
	row = line.split('\t')
	if row[4] != '_':
		tokens.append(row[1])
		#print(row[4])
		pos.append(row[4])


# make a matrix of word → tag and a separate frequency list for tags
# m = {}
# for w1 in tokens: 
# 	if w1 not in m: 
# 		m[w1] = {}
# 	for w2 in pos:
# 		m[w1][w2] = 0


# print('\t' + '\t'.join(pos))
# for w1 in m:
#         print('%s\t' % (w1), end='')
#         for w2 in m[w1]:
#                 print('%d\t' % (m[w1][w2]), end='')
#         print('')


pos_tokens_pairs = []
for i in range(len(tokens)):
	pos_tokens_pairs.append(pos[i] + '\t' + tokens[i])

pos_tokens_pairs_freq = {}
for i in pos_tokens_pairs:
	if i not in pos_tokens_pairs_freq:
		pos_tokens_pairs_freq[i] = 1
	else: pos_tokens_pairs_freq[i] += 1

pos_freq = {}
for i in pos:
	if i not in pos_freq:
		pos_freq[i] = 1
	else: pos_freq[i] += 1

#print(pos_tokens_pairs_freq)


output = '# P\tcount\ttag\tform\n'
for i in pos_freq:
	output += str(round(pos_freq[i] / len(tokens)), 2)
	output += '\t'
	output += str(pos_freq[i])
	output += '\t' 
	output += i
	output += '\t_\n'
for i in pos_tokens_pairs_freq:
	#print(pos_tokens_pairs_freq[i])
	output += str(pos_tokens_pairs_freq[i])
	output += '\t' 
	output += i
	output += '\n'

sys.stdout.write(output)


#for i in tokens:
#	sys.stdout.write(i, end = ' ')

#for i in pos:
#	print(i, end = ' ')

#print(len(tokens))
#print(len(pos))
