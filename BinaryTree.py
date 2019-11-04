class Node(object):
	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data


class BinaryTree(object):
	def __init__(self):
		self.root = None


	def _compare(self, newData, oldData):

		# Comparison method made for integers.
		# Change this method depending on the type you're dealing with.

		if newData > oldData:
			return 1
		elif newData < oldData:
			return -1
		else:
			return 0


	def insert(self, data):
		self.root = self._insert(data, self.root)


	def _insert(self, data, node):

		# Recursive insertion.

		if node is None:
			node = Node(data)
		else:
			stat = self._compare(data, node.data)
			if stat < 0:
				node.left = self._insert(data, node.left)
			else:
				node.right = self._insert(data, node.right)

		return node

	
	def insertMultipleElements(self, elements):

		# Reads the file into a string which is converted to an auxiliar list
		# for inserting its elements into the binary tree.

		for element in elements:
			self.insert(element)


	# TODO. Not necessary, but I want to implement it anyway
	# def _remove(self, node):


	def search(self, data):
		return self._search(data, self.root)

	
	def _search(self, data, node):

		# Recursive search.
		# Returns the data of the node if it has been found, returns None otherwise.

		if node is not None:
			stat = self._compare(data, node.data)
			if stat == 0:
				return node.data
			elif stat < 0:
				return self._search(data, node.left)
			else:
				return self._search(data, node.right)

		return None


	def searchSame(self, group):

		# Searches for elements that are both in the list and in the binary tree.

		same = []
		for element in group:
			if self.search(element) is not None:
				same.append(element)

		return same


	def insertDifferent(self, group):

		# Inserts the elements that are in the list and not in the binary tree.

		different = []
		for element in group:
			if self.search(element) is None:
				different.append(element)

		for element in different:
			self.insert(element)


	def removeSame(self, group):

		# Removes the elements of the list that are in the binary tree and in the list
		# at the same time.

		same = self.searchSame(group)

		for element in same:
			group.remove(element)


	def printTree(self):
		self._printTree(self.root)


	# recursive print
	def _printTree(self, node):	
		if node != None:
			self._printTree(node.left)
			print(node.data, ' ')
			self._printTree(node.right)
