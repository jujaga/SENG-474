# Sliq.py
# SENG 474
# Jeremy Ho & Helen Lin

import os, sys, string
from classlist import *

def main():
	"""Main program"""
	
	# Read input file
	try:
		f = sys.stdin
	except IOError as e:
		sys.exit("{}".format(e))
	rawinput = []
	for line in f:
		if line.startswith("%"):
			continue
		rawinput.append(line[:-1].lower()) # ditch trailing newline
	
	# Remove non-data lines & format
	rawdata = rawinput[rawinput.index("@data")+1:]
	data = []
	for line in rawdata:
		data.append(line.split(','))
	
	#for line in data:
	#	print line
	
	# Process input
	CL = classlist(data)
	#print CL.leaves
	print CL.displayTree()

if __name__ == '__main__':
	main()