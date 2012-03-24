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
		self.addID
		self.classList = []
		self.attrList = []
		self.uniqueClassValues = []
		self.newLeaf = 1;
		self.tree = []
		
		self.init
		self.totalRecords = len( self.classList )
		
		# The following line has an odd argument mismatch error helen - commented it out just to have proper execution for now - jeremy
		#self.doSLIQ( self.attrList, 1, 1 )

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
				self.classList.append( [ row[0], row[len(row) - 1], self.newLeaf ] )
				classValues.append( row[len(row) - 1] )
				
		self.uniqueClassValues = list( set( classValues ) )
		self.newLeaf += 1
	
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
	
	
	# Returns an list of values of a single attribute
	def getSingleAttrList( leafList, colIndex ):
		aList = []
		for record in leafList:
			aList.append( record[colIndex] )
		return aList
	
	# Returns a record from a list with matching rid
	# The list is either attribute list or classlist
	def getRecordBaseOnRID( aList, rid ):
		for record in aList:
			if record[0] == rid:
				return record
				
	
	# Returns the class of a record
	def getClassByRID( rid ):
		for record in self.classList:
			if record[0] == rid:
				return record[2]
	
	
	# Returns attribute records with the same leaf number
	def getAttrListBaseOnLeaf( leaf ):
		newAttrList = []
		for record in self.classList:
			if record[2] == leaf:
				newAttrList.append( self.getRecordBaseOnRID( self.attrList, record[0] ) )
		return newAttrList
		
	# Initialize an histogram structure
	# Eaxmple: n = 2, len( self.uniqueClassValues ) = 3
	# [
	#		[	0, 0, 0	]
	#		[	0, 0, 0	]
	# ]
	def createEmptyHistogram( n ):
		emptyHistogram = []
		
		for i in range( 0, n ):
			row = []
			for i in self.uniqueClassValues:
				row.append(0)
			emptyHistogram.append( row )
		return emptyHistogram
		
		
	# Returns the entropy calculated by the list of probabilities
	# make sure the list of probabilities sums up to total
	def calculateEntropy( probabilities, total ):
		entropy = 0
		for probability in probabilities:
			prob = probability / total
			if prob != 0:
				entropy += -1 *  prob  * math.log( prob, 2 )
		return entropy
		
		
	# Calculate the expected info of an attribute from a histogram
	# Example list
	# 			   		(	predictValue1, 	predictValue2, 	predictValue3  )
	#					[
	# (attrValue1)		[	1,						2,						3  				]
	# (attrValue2)		[	3,						4,						6  				]	
	#					]
	def calculateExpectedInfo( histogramList ):
		expectedInfo = 0
		for attrValueRow in histogramList:
			listSum = sum( attrValueRow )
			expectedInfo += ( listSum / self.totalRecords ) * self.calculateEntropy( attrValueRow, listSum )
		return expectedInfo
	
	
	# Perform SLIQ base on the provided attribute list of one type of leaf
	# Example of self.tree that will be poplated by this function
	# [
	#		[ level, leafNum, expectedInfo, attributeType, columnIndex, splitAtValue ]
	# [
	# level 				- which level of the tree this leaf is at
	# leafNum			- the leaf number
	# expectedInfo		- expectedInfo of this attribute
	# attributeType	- either numeric of category
	# columnIndex		- the index of the attribute in attrlist
	# splitAtValue		- the value the numeric attribute splite at using <= as the comparing operater
	def doSLIQ( attrLeafList, leafNum, level ):
		info = []					# holds all the expected info that have been calculated
		for row in attrLeafList:
			# starting with the first attribute at index 1
			for i in range( 1, len(row) ):
				self.sortList( attrLeafList, i )
				if row[i].isDigit():
					# do numerical calculation
					info.append( self.numericalCalculation( attrLeafList, i ) )
				else:
					# do categorical calculation
					info.append( self.categoricalCalculation( attrLeafList, i ) )
		
		# sort the gathered info values
		self.sortList( info, 0 )
		bestInfo = info[0]
		bestInfo.insert( 0, leafNum )
		bestInfo.insert( 0, level )
		self.tree.append( bestInfo )
		
		# update leaf number
		
		return 0
		
	
	# Returns the expected info for this categorical attribute
	# Eaxample output:
	# [ expectedInfo, "category", columnIndex ] 
	def categoricalCalculation( leafList, colIndex ):
		attrUniqueValues = list( set(self.getSingleAttrList( leafList, colIndex )) )
		histogram = self.createEmptyHistogram( len(attrUniqueValues) )
		
		for row in leafList:
			attrValueIndex = attrUniqueValues.index( row[colIndex] )
			classValueIndex = self.uniqueClassValues.index( getClassByRID( row[0] ) )
			histogram[attrValueIndex][classValueIndex] += 1
			
		return [ self.calculateExpectedInfo( histogram ), "category", colIndex ]
		
		
	# Returns the expected info for this numerical attribute
	# Eaxample output:
	# [ expectedInfo, "numeric", columnIndex, split at value ] 
	def numericalCalculation( leafList, colIndex ):
		infoList = []
		for splitRow in leafList:
			splitValue = splitRow[colIndex]
			histogram = self.createEmptyHistogram( 2 )
			
			for row in leafList:
				classValueIndex = self.uniqueClassValues.index( getClassByRID( row[0] ) )
				if row[colIndex] <= splitRow:
					histogram[0][classValueIndex] += 1
				else:
					histogram[1][classValueIndex] += 1
		
			infoList.append( self.calculateExpectedInfo( histogram ) )
		
		bestInfo = min( infoList )
		bestInfoIndex = infoList.index( bestInfo )
		
		return [ bestInfo, "numeric", colIndex, leafList[bestInfoIndex][colIndex] ]