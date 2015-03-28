import sys

def encrypt(key):
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
			c = (ord(char) + key) % 126
			if c < 32:
				c += 31

			cipher += chr(c)
		target.write(str(cipher))
		target.write('\n')

	print 'Pesan terenkripsi: chiper.txt'

def decrypt(key):
	pathEnc = raw_input('Masukan path .txt terenkripsi: ')
	target = open('decrypt.txt', 'w')
	ciphertext = open(pathEnc)

	for line in ciphertext:
		plaintext = ''
		for char in line:
			indexchar = (ord(char) - key) % 126

			if indexchar < 32:
				indexchar += 95

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
	if (len(sys.argv) != 3):
		sys.exit('Format: python cipy.py <key> <mode>')

	if sys.argv[2] == 'e':
		encrypt(int(sys.argv[1]))
	elif sys.argv[2] == 'd':
		decrypt(int(sys.argv[1]))
	else:
		sys.exit('Format exc error')

if __name__ == '__main__':
	main(sys.argv[1:])