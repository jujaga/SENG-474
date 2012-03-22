# classlist.py
# SENG 474
# Jeremy Ho & Helen Lin

class classlist:
	"Creates the decision tree."

	# Note: I am changing back to using lists because tuples are immutable

	# d - The input data
	# The last column is the prediction category
	# Example: ( 2 records )
	# [
	# 	[ age, salary, marital, car ],
	# 	[ age, salary, marital, car ]
	# ]
	def __init__(self, d):
		self.data = d
		self.addID()
		self.classList = []
		self.attrList = []
		self.uniqueClassValues = []
		self.init()
		self.totalRecords = len( self.classList )
		self.doSLIQ( self.attrList )

	# Creates the classlist and attributeList
	# Example: ( 2 records )
	#
	# Attribute List:
	# [
	#	[ rid, age, salary, marital ],
	#	[ rid, age, salary, marital ]
	# ]
	#
	# Class List: 
	# [
	#	[ rid, car, leaf ],
	#	[ rid, car, leaf ]
	# ]
	def init():
		for i in range( self.data ):
			row = self.data[i]
			if j < range( row ) -1:
				self.attrList.append( row[0: len(row) - 1] )
			else:
				self.classList.append( [ row[0], row[len(row) - 1], 1 ] )
				classValues.append( row[len(row) - 1] )
				
		self.uniqueClassValues = list( set( classValues ) )
	
	# Adds rid to each record
	# Example: ( 2 records )
	# [
	# 	[ rid, age, salary, marital, car ],
	# 	[ rid, age, salary, marital, car ]
	# ]
	def addID():
		for i in range( self.data ):
			self.data[i].insert( 0, i )
	
	# Sorts the atrribute list base on the column number
	def sortList( attributeList, columnNumber ):
		attributeList.sort( key=lambda value: value[columnNumber] )
	
	# Returns a record from a list with matching rid
	# The list is either attribute list or classlist
	def getRecordBaseOnRID( aList, rid ):
		for record in aList:
			if record[0] == rid:
				return record
				
	
	# Returns attribute records with the same leaf number
	def getAttrListBaseOnLeaf( leaf ):
		newAttrList = []
		for record in self.classList:
			if record[2] == leaf:
				newAttrList.append( self.getRecordBaseOnRID( self.attrList, record[0] ) )
		return newAttrList
		
		
	# Returns the entropy calculated by the list of probabilities
	# make sure the list of probabilities sums up to total
	def calculateEntropy( probabilities, total ):
		entropy = 0
		for probability in probabilities:
			prob = probability / total 
			entropy += -1 *  prob  * math.log( prob, 2 )
		return entropy
		
		
	# Calculate the expected info of an attribute
	# Example list
	# 			   (	predictValue1, 		predictValue2, 		predictValue3   )
	#			[
	# (attrValue1)	   	   [	1,			2,			3  		]
	# (attrValue2)	   	   [	3,			4,			6  		]	
	#			]
	def calculateExpectedInfo( histogramList ):
		expectedInfo = 0
		for attrValueRow in histogramList:
			listSum = sum( attrValueRow )
			expectedInfo += ( listSum / self.totalRecords ) * self.calculateEntropy( attrValueRow, listSum )
		return expectedInfo
	
	
	# Perform SLIQ base on the provided attribute list of one type of leaf
	def doSLIQ( attrLeafList ):
		# For every attribute in the record calculate best entropy
		# keep track of the best entropy attribute selected
		# update leaf label
		# get attribute records with the same leaf number with the best entropy attribute removed
		# run doSLIQ again with the new attribute lists
		# stop when last attribute is used 
		
		for row in attrLeafList:
			# starting with the first attribute at index 1
			for i in range( 1, len(row) ):
				self.sortList( attrLeafList, i )
				if row[i].isDigit():
					# do numerical entropy calculation
				else:
					# do categorical entropy calculation
		return 0