import math

"""
SkipList is made up of SkipListNodes as defined in the SkipListNode class below.

The overall structure follows that of a linked-list, where each index is populated by a node.
Skip pointers are also created to link individual that bypass adjacent nodes, with the distance of each skip determined by:
>>> math.floor(math.sqrt(length_of_postings_array))
"""

class SkipList:

	# Constructor
	def __init__(self, postings_array=None):
		self.length = 0
		self.skip = False # initialise skip marker to False

		if postings_array == None:
			self.head = None #empty	
			self.tail = None #empty

		else: # initialised with populated postings_array
			postings_array.sort() #sort in order of increasing docID number
			for i in postings_array:
				node = SkipListNode(i)
				self.add(node)

	def __len__(self):
		return self.length

	# add node at back of list
	def add(self, node):
		if len(self) == 0:
			self.head = node
			self.tail = node
		else:
			self.tail.add_next_node(node)
			self.tail = node

		self.length = self.length + 1

	# if skip pointers are created for this list
	def is_skipped(self):
		return self.skip

	# calculate the skip distance of the list
	def skip_distance(self):
		length_of_list = len(self)
		skip_distance = math.floor(math.sqrt(length_of_list)) # using the recommended skip distance calculation formula
		return skip_distance

	# get a specific node according to its index
	def get_node(self, index_of_node):
		currentNode = self.head
		while index_of_node > 0: # traversing nodes to reach specific node
			currentNode = currentNode.next
			index_of_node -= 1
		return currentNode

	# sets the skip pointer of node with first_index to point to node with second_index
	def skip_to(self, first_index, second_index):
		first_node = self.get_node(first_index)
		second_node = self.get_node(second_index)
		first_node.skip = second_node

	# create skip pointes for the entire list
	def generate_skips(self):
		if self.is_skipped():
			self.clearSkips()
		else:
			current_index = 0 # initialise current = 0
			target_index = 0 + self.skip_distance() # initialise first skip index = 0 + skip distance
			while target_index < self.length:
				self.skip_to(current_index, target_index)
				current_index = target_index
				target_index += self.skip_distance()
			self.skip = True # set skip marker to true
		return self

	def to_list(self):
		result = []
		current = self.head
		while current.has_next():
			result.append(current.docID)
			current = current.next
		result.append(self.tail.docID)
		return result

	"""
	def clear_skips(self):
		if self.skip == True:
			current = self.head
			while current.has_next():
				if current.has_skip():
					current.skip = None
				current = current.next
			self.skip = False
		return self
	"""

"""
SkipListNode is used in SkipList class.

A SkipListNode contains three attributes:

1. DocID
2. Next Node
3. Skipped to Node
"""

class SkipListNode: 

	# Constructor
	def __init__(self, doc_id=None): 
		self.docID = int(doc_id)
		self.next = None 
		self.skip = None

	# Setters
	def add_next_node(self, next_node):
		self.next = next_node

	# Checkers
	def has_next(self):
		return self.next != None

	def has_skip(self):
		return self.skip != None

	# Override str representation for convenient printing (testing)
	def __str__(self):
		return "Node: " + str(self.data)


"""
AdapterList : 

Adapter class to allow compatibility between SkipList and the native List library in python.
This will provide ease to processing intermediate results and newly retrieved postings. 
"""

class AdapterList:

	# constructor
	def __init__(self, list_to_adapt):
		self.data = list_to_adapt
		self.length = len(list_to_adapt)
		self.is_list = type(list_to_adapt) is list
		if not self.is_list:
			self.current = self.data.get_node(0)
			if self.length > 0:
				self.current_data = self.current.docID
		else:
			self.current = 0
			if self.length > 0:
				self.current_data = list_to_adapt[0]
			
	def __len__(self):
		return self.length

	def current_docID(self):
		return self.current_data

	def has_next(self):
		if not self.is_list:
			return self.current.next != None
		else:
			return self.current +1 < self.length

	def next(self):
		if not self.has_next():
			return False 

		if self.is_list:
			self.current += 1
			self.current_data = self.data[self.current]
		else:
			self.current = self.current.next
			self.current_data = self.current.docID
		return True

	def has_skip(self):
		if not self.is_list:
			return self.current.has_skip()
		else:
			return False
			return self.has_next()

	def skip_docID(self):
		if not self.is_list:
			return self.current.skip.docID
		else:
			# have to calculate min here due to possibility of getting index out of bounds 
			return self.data[min(int(math.sqrt(self.length)) + self.current, self.length - 1)] 	
		
	def skip_to_next(self):
		if not self.is_list:
			self.current = self.current.skip
			self.current_data = self.current.docID
		else:
			jump_to_index = min(self.length - 1, int(math.sqrt(self.length)) + self.current)
			self.current = jump_to_index
			self.current_data = self.data[jump_to_index] 

	def to_list(self):
		if not self.is_list:
			return self.data.to_list()
		else:
			return self.data