def transcribe(dna):
	'''
	dna is a string containing all bases of the dna to transcribe
	
	Returns a string continaing the RNA transcribed
	'''
	trans_start = dna.find('TATAAT') + 10
	trans_end = trans_start
	
	# find the terminator
	while trans_end < len(dna):
		terminator = complement(dna[trans_end:trans_end + 6])
		if dna.find(terminator[::-1], trans_end + 6) != -1:
			break
		trans_end += 1
		
	return complement(dna[trans_start:trans_end], True)
	
	
def complement(dna, is_rna=False):
	'''
	dna is a string of a dna sequence.
	is_rna is a boolean indicating if we obtain a complement RNA-transcribeed
	and if it's True then T is replaced with U.
	
	Returns the complement of the dna sequence as a string
	'''
	dna_lst = list(dna)
	for i in range(len(dna_lst)):
		if dna_lst[i] == 'A':
			dna_lst[i] = 'T'
			if is_rna:
				dna_lst[i] = 'U'
		elif dna_lst[i] == 'T':
			dna_lst[i] = 'A'
		elif dna_lst[i] == 'C':
			dna_lst[i] = 'G'
		elif dna_lst[i] == 'G':
			dna_lst[i] = 'C'
	return ''.join(dna_lst)

# Main program

for i in range(5):
	# Read input
	dna = input()
	# Transcribe input dna into a rna seq
	rna = transcribe(dna)
	# Output rna seq
	print(f'{i+1}: {rna}')
	
