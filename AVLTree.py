class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1

		
class AVLTree(object):
	def __init__(self):
		self.root = None
		self.comparisons = 0
		self.attributions = 0


	def getHeight(self, node):
		if node is None:
			self.comparisons += 1
			return 0

		return node.height


	def getBalance(self, node):
		if node is None:
			self.comparisons += 1
			return 0

		return self.getHeight(node.right) - self.getHeight(node.left)

	# def calculateHeight(self, node):

	# 	# recursively calculates the height of the tree using this formula:
	# 	# Height = 1 + max(Height(left) + Height(right))
	# 	# Where Height(left/right) is the height of the left/right subtree.

	# 	if node is None:
	# 		return -1

	# 	lHeight = self.calculateHeight(node.left)
	# 	rHeight = self.calculateHeight(node.right)

	# 	return 1 + max(lHeight, rHeight)


	# def updateBF(self, node):

	# 	# updates the balance factor (BF) of every element in the tree using
	# 	# this formula:
	# 	# BF = Height(left) - Height(right)
	# 	if node is not None:
	# 		lHeight = self.calculateHeight(node.left)
	# 		rHeight = self.calculateHeight(node.right)
	# 		node.balance = rHeight - lHeight

	# 		self.updateBF(node.left)
	# 		self.updateBF(node.right)


	def rotateLeft(self, node):

		# rotates the tree to the left. The node to the right goes to the place
		# where the received node was.
		
		rNode = node.right
		self.attributions += 1
		node.right = rNode.left
		self.attributions += 1
		rNode.left = node
		self.attributions += 1

		# update height of the nodes
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		self.attributions += 1
		rNode.height = 1 + max(self.getHeight(rNode.left), self.getHeight(rNode.right))
		self.attributions += 1

		return rNode


	def rotateRight(self, node):

		# rotates the tree to the right. The node to the left goes to the place
		# where the received node was.

		lNode = node.left
		self.attributions += 1
		node.left = lNode.right
		self.attributions += 1
		lNode.right = node
		self.attributions += 1

		# update height of the nodes
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		self.attributions += 1
		lNode.height = 1 + max(self.getHeight(lNode.left), self.getHeight(lNode.right))
		self.attributions += 1

		return lNode


	def rotateLeftRight(self, node):

		# a.k.a. double right rotation
		# consists of a left rotation then a right rotation.

		node = self.rotateLeft(node.left)
		self.attributions += 1
		return self.rotateRight(node)


	def rotateRightLeft(self, node):

		# a.k.a. double left rotation
		# consists of a right rotation then a left rotation.

		node = self.rotateRight(node.right)
		self.attributions += 1
		return self.rotateLeft(node)


	def rebalance(self, node):

		# Recursively rebalances the tree with rotations.

		if node is not None:
			self.comparisons += 1
			node.left = self.rebalance(node.left)
			self.attributions += 1
			node.right = self.rebalance(node.right)
			self.attributions += 1
			balance = self.getBalance(node)
			self.attributions += 1
			balanceL = self.getBalance(node.left)
			self.attributions += 1
			balanceR = self.getBalance(node.right)
			self.attributions += 1

			if balance > 1: # if the BF of the node is positive and...
				self.comparisons += 1
				if balanceR >= 0: # ...right child is positive, rotate left.
					self.comparisons += 1
					node = self.rotateLeft(node)
					self.attributions += 1
				elif balanceR < 0: # ...left child is negative, rotate right, then left.
					self.comparisons += 1
					node = self.rotateRightLeft(node)
					self.attributions += 1
					
			elif balance < -1: # if the BF of the node is negative and...
				self.comparisons += 1
				if balanceL >= 0: # ...left child is positive, rotate left, then right.
					self.comparisons += 1
					node = self.rotateLeftRight(node)
					self.attributions += 1
				elif balanceL < 0: # ...left child is negative, rotate right.
					self.comparisons += 1
					node = self.rotateRight(node)
					self.attributions += 1
		
		return node


	def insertMultipleElements(self, elements):

		# Reads the file into a string, which is converted to an auxiliar list
		# for inserting its elements into the AVL tree.

		for element in elements:
			self.attributions += 1
			self.insert(element)


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

		# Inserts an element into the AVL tree and then rebalances the tree if needed.

		self.root = self._insert(data, self.root)
		self.attributions += 1
		# self.updateBF(self.root)
		self.root = self.rebalance(self.root)
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

		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		self.attributions += 1

		return node


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

		# Searches for elements that are both in the list and in the AVL tree.

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

		# Inserts the elements that are in the list and not in the AVL tree.

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

		# Removes the elements of the list that are in the AVL tree and in the list
		# at the same time.

		same = self.searchSame(group)
		self.attributions += 1

		for element in same:
			self.attributions += 1
			group.remove(element)


	def printTree(self):
		self._printTree(self.root)


	def _printTree(self, node):	

		# Recursive print of the tree in pre order.

		if node is not None:
			self.comparisons += 1
			print(str(node.data) + ' ' + str(self.getBalance(node)))
			self._printTree(node.left)
			self._printTree(node.right)