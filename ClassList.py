

class ClassList
	"Creates the decision tree."

	# d - The data in list form
	# Example: ( 2 records )
	# [
	# 	[ age, salary, marital, car ],
	# 	[ age, salary, marital, car ]
	# ]
	
	def __init__(self, d):
		self.data = d
		self.classList = []
		self.attrList = []
		self.addID()
	
	def addID():
		for i in range( self.data ):
			self.data.insert( 0, i )
	
	# Example: ( 2 records )
	#
	# Attribute List:
	# [
	# 	[ 
	#		[ rid, age ],
	#		[ rid, age ]
	#	],
	# 	[ 
	#		[ rid, salary ],
	#		[ rid, salary ]
	#	],
	# 	[ 
	#		[ rid, marital ],
	#		[ rid, marital ]
	#	]
	# ]
	#
	# Class List:
	# [
	# 	[ 
	#		[ rid, car, leaf ],
	#		[ rid, car, leaf ]
	#	],
	# ]
	def createSortedLists():
		for i in range( self.data ):
			row = self.data[i]
			for j in range( row ):
				if j < range( row ) -1:
					self.attrList[i].append( [ row[0], row[j] ) ] )
				else
					self.classList.append( [ row[0], row[j], 1 ] )
		
		# sort by the second value in the attribute list
		for aList in self.attrList:
			aList.sort( key=lambda tup: tup[1] )
			