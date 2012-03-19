# Sliq.py
# SENG 474
# Jeremy Ho & Helen Lin

import os, sys, string, argparse

def main():
	"""Main program"""

	# Parse input arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', help='input bbb file', action='store',
						required=True)
	parser.add_argument('-o', help='output file result', action='store',
						default='out.bbb')
	args = parser.parse_args()
	
	# Read input file
	try:
		f = open(args.i, 'r')
	except IOError as e:
		sys.exit("{}".format(e))
	rawinput = []
	for line in f:
		rawinput.append(line[:-1]) # ditch trailing newline
	f.close()

	# Process input
	
	# Write to file
	try:
		f = open(args.o, 'w')
	except IOError as e:
		sys.exit("{}".format(e))
	for line in rawinput:
		f.write(string.join(line,''))
		f.write('\n')
	f.close()

if __name__ == '__main__':
	main()
