import sys

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