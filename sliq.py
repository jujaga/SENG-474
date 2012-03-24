# Sliq.py
# SENG 474
# Jeremy Ho & Helen Lin

import os, sys, string#, argparse
from classlist import *

def main():
	"""Main program"""

	# Parse input arguments
	'''parser = argparse.ArgumentParser()
	parser.add_argument('-i', help='input arff file', action='store',
						required=True)
	parser.add_argument('-o', help='output result', action='store',
						default='out.txt')
	args = parser.parse_args()'''
	
	# Read input file
	try:
		f = sys.stdin
	except IOError as e:
		sys.exit("{}".format(e))
	rawinput = []
	for line in f:
		rawinput.append(line[:-1].lower()) # ditch trailing newline
	#f.close()
	
	# Remove non-data lines & format
	rawdata = rawinput[rawinput.index("@data")+1:]
	data = []
	for line in rawdata:
		data.append(line.split(','))
	
	#for line in data:
	#	print line
	
	# Process input
	CL = classlist(data)
	
	# Write to file
	#try:
	#	f = sys.stdout
	#except IOError as e:
	#	sys.exit("{}".format(e))
	#for line in rawinput:
	#	f.write(string.join(line,''))
	#	f.write('\n')
	#f.close()

if __name__ == '__main__':
	main()
