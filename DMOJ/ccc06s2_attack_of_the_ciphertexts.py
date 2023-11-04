plaintext = input()
ciphertext = input()
encrypted = input()

cipher_to_plain = {}

for i in range(len(plaintext)):
	cipher_to_plain[ciphertext[i]] = plaintext[i]

# try to guess one missing char
if len(cipher_to_plain) == 26:
	all_chars = set(' ')
	for i in range(26):
		all_chars.add(chr(ord('A') + i))
		
	missing_plain = all_chars - set(plaintext)
	missing_ciph = all_chars - set(ciphertext)
	cipher_to_plain[missing_ciph.pop()] = missing_plain.pop()

decrypted = []
for c in encrypted:
	decrypted.append(cipher_to_plain.get(c, '.'))
	
print(''.join(decrypted))
