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
	if (len(sys.argv) != 2):
		sys.exit('Format: python cipy.py <key>')

	plaintext = list(raw_input('Masukan pesan: '))
	alphabet = list('abcdefghijklmnopqrstupwxyz')
	key = int(sys.argv[1])
	cipher = ''

	for char in plaintext:
		if char in alphabet:
			cipher += alphabet[(alphabet.index(char) + key) % (len(alphabet))]

	print 'Pesan terenkripsi: ' + cipher

if __name__ == '__main__':
	main(sys.argv[1:])