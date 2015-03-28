import sys

def encrypt(key, level=1):
	'''
	126 was using forr ASCII Printable Character map
	http://thelivingpearl.com/printable-ascii-characters/
	'''
	pathMsg = raw_input('Masukan path .txt pesan: ')
	target = open('chiper.txt', 'w')
	msg = open(pathMsg)

	for line in msg:
		cipher = ''
		for char in line:
			'''
			Default level is 1, which is only one iteration encrypt

			'''
			for nLvl in range(int(level)):
				indexchar = (ord(char) + key) % 126
				if indexchar < 32:
					c += 31
				char = chr(indexchar)

			cipher += char
		target.write(str(cipher))
		target.write('\n')

	print 'Pesan terenkripsi: chiper.txt'

def decrypt(key, level=1):
	pathEnc = raw_input('Masukan path .txt terenkripsi: ')
	target = open('decrypt.txt', 'w')
	ciphertext = open(pathEnc)

	for line in ciphertext:
		plaintext = ''
		for char in line:
			'''
			Default level is 1, which is only one iteration encrypt

			'''
			for nLvl in range(int(level)):
				indexchar = (ord(char) - key) % 126

				if indexchar < 32:
					indexchar += 95
				char = chr(indexchar) 

			plaintext += chr(indexchar)
		target.write(str(plaintext))
		target.write('\n')

	print 'Pesan: decrypt.txt'

def main(argv):
	'''
	key: jumlah penggeseran (key < len(alphabet))
	mode: e for encrypt
			  d for decrypt
	'''
	if (len(sys.argv) != 4):
		sys.exit('Usage: python cipy.py <key> <mode> <level>')

	if sys.argv[2] == 'e':
		encrypt(int(sys.argv[1]), int(sys.argv[3]))
	elif sys.argv[2] == 'd':
		decrypt(int(sys.argv[1]), int(sys.argv[3]))
	else:
		sys.exit('Format exc error')

'''
if __name__ == '__main__':
	
	for i in range(0, len(sys.argv)):
		print i, sys.argv[i]
'''	

main(sys.argv[1:])
