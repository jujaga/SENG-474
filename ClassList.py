

class ClassList
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
		self.init()
	
	
	# Adds rid to each record
	# Example: ( 2 records )
	# [
	# 	[ rid, age, salary, marital, car ],
	# 	[ rid, age, salary, marital, car ]
	# ]
	def addID():
		for i in range( self.data ):
			self.data[i].insert( 0, i )
	
	
	# Creates the classList and attributeList
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
			else
				self.classList.append( [ row[0], row[len(row) - 1], 1 ] )
	
	
	# Sorts the atrribute list base on the column number
	def sortAtrributeList( columnNumber )
		self.attrList.sort( key=lambda value: value[columnNumber] )
	
	
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
		
		
	# Perform SLIQ
	def doSLIQ( attrLeafList ):
		# For every attribute in the record calculate best entropy
		# keep track of the best entropy attribute selected
		# update leaf label
		# get attribute records with the same leaf number with the best entropy attribute removed
		# run doSLIQ again with the new attribute lists
		# stop when last attribute is used 
		
	
			