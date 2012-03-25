SENG 474
Authors: Jeremy Ho, Helen Lin
----------------------------------------

This repository has a sliq implementation in Python
classlist.py: stores, holds, and performs sliq algorithm
sliq.py: main function - input & output

----------------------------------------
Usage
----------------------------------------
Windows
	python sliq.py < input.arff [ > output file ]

		OR

	type input.arff | python sliq.py [ > output file ]

Unix
	python sliq.py < input.arff [ > output file ]

		OR

	cat input.arff | python sliq.py [ > output file ]

----------------------------------------
Notes
----------------------------------------
input should be an .arff file
All input and output will go through stdin and stdout respectively.
