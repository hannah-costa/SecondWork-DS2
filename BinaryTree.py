class Node(object):
	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data


class BinaryTree(object):
	def __init__(self):
		self.root = None

		self.comparisons = 0
		self.attributions = 0


	def _compare(self, newData, oldData):

		# Comparison method made for integers.
		# Change this method depending on the type you're dealing with.

		if newData > oldData:
			self.comparisons += 1
			return 1
		elif newData < oldData:
			self.comparisons += 1
			return -1
		else:
			self.comparisons += 1
			return 0


	def insert(self, data):
		self.root = self._insert(data, self.root)
		self.attributions += 1


	def _insert(self, data, node):

		# Recursive insertion.

		if node is None:
			self.comparisons += 1
			return Node(data)
		else:
			self.comparisons += 1
			stat = self._compare(data, node.data)
			self.attributions += 1
			if stat < 0:
				self.comparisons += 1
				node.left = self._insert(data, node.left)
				self.attributions += 1
			else:
				self.comparisons += 1
				node.right = self._insert(data, node.right)
				self.attributions += 1

		return node

	
	def insertMultipleElements(self, elements):

		# Reads the file into a string which is converted to an auxiliar list
		# for inserting its elements into the binary tree.

		for element in elements:
			self.attributions += 1
			self.insert(element)


	# TODO. Not necessary, but I want to implement it anyway
	# def _remove(self, node):


	def search(self, data):
		return self._search(data, self.root)

	
	def _search(self, data, node):

		# Recursive search.
		# Returns the data of the node if it has been found, returns None otherwise.

		if node is not None:
			self.comparisons += 1
			stat = self._compare(data, node.data)
			self.attributions += 1
			if stat == 0:
				self.comparisons += 1
				return node.data
			elif stat < 0:
				self.comparisons += 1
				return self._search(data, node.left)
			else:
				self.comparisons += 1
				return self._search(data, node.right)

		return None


	def searchSame(self, group):

		# Searches for elements that are both in the list and in the binary tree.

		same = []
		self.attributions += 1
		for element in group:
			self.attributions += 1
			if self.search(element) is not None:
				self.comparisons += 1
				same.append(element)
				self.attributions += 1

		return same


	def insertDifferent(self, group):

		# Inserts the elements that are in the list and not in the binary tree.

		different = []
		self.attributions += 1
		for element in group:
			self.attributions += 1
			if self.search(element) is None:
				self.comparisons += 1
				different.append(element)
				self.attributions += 1

		for element in different:
			self.attributions += 1
			self.insert(element)


	def removeSame(self, group):

		# Removes the elements of the list that are in the binary tree and in the list
		# at the same time.

		same = self.searchSame(group)
		self.attributions += 1

		for element in same:
			self.attributions += 1
			group.remove(element)
			self.attributions += 1


	def printTree(self):
		self._printTree(self.root)


	# recursive print
	def _printTree(self, node):	
		if node != None:
			self.comparisons += 1
			self._printTree(node.left)
			print(node.data, ' ')
			self._printTree(node.right)
