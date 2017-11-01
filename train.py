import sys


tokens = []
pos = []
for line in sys.stdin:
	if '\t' not in line:
		continue
	row = line.split('\t')
	if row[4] != '_':
		tokens.append(row[1])
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


# get a dictionary of pos-tokens pairs and their frequency
pos_tokens_pairs = []
for i in range(len(tokens)):
	pos_tokens_pairs.append(pos[i] + '\t' + tokens[i])

pos_tokens_pairs_freq = {}
for i in pos_tokens_pairs:
	if i not in pos_tokens_pairs_freq:
		pos_tokens_pairs_freq[i] = 1
	else: pos_tokens_pairs_freq[i] += 1

# pos frequency
pos_freq = {}
for i in pos:
	if i not in pos_freq:
		pos_freq[i] = 1
	else: pos_freq[i] += 1

# tokens frequency
tokens_freq = {}
for i in tokens:
	if i not in tokens_freq:
		tokens_freq[i] = 1
	else: tokens_freq[i] += 1

output = '# P\tcount\ttag\tform\n'
for i in pos_freq:
	output += str((pos_freq[i] / len(tokens)))
	output += '\t'
	output += str(pos_freq[i])
	output += '\t' 
	output += i
	output += '\t_\n'
for i in pos_tokens_pairs_freq:
	# calculate the P column for the word → tag by dividing the frequency of a word = tag pair
	# by the total number of instances of the word
	output += str(pos_tokens_pairs_freq[i] / tokens_freq[i.split('\t')[1]])
	output += '\t'
	output += str(pos_tokens_pairs_freq[i])
	output += '\t' 
	output += i
	output += '\n'

sys.stdout.write(output)

