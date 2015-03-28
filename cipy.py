import sys

def encrypt(key):
	'''
	126 was using forr ASCII Printable Character map
	http://thelivingpearl.com/printable-ascii-characters/
	'''
	plaintext = raw_input('Masukan pesan: ')
	cipher = ''

	for char in plaintext:
		c = (ord(char) + key) % 126

		if c < 32:
			''' 
			First 32 was some unprintable characters
			'''
			c += 31

		cipher += chr(c)

	print 'Pesan terenkripsi: ' + cipher

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