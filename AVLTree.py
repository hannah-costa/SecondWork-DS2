class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1


class AVLTree(object):
	def __init__(self):
		self.root = None


	def getHeight(self, node):

		# Getter for the height attribute of the node. 

		if node is None:
			return 0

		return node.height


	def getBalance(self, node):

		# Calculates the BF of the node.

		if node is None:
			return 0

		return self.getHeight(node.right) - self.getHeight(node.left)


	def rotateLeft(self, node):

		# Rotates the tree to the left. The node to the right goes to the place
		# where the received node was.
		
		rNode = node.right
		node.right = rNode.left
		rNode.left = node

		# update height of the nodes
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		rNode.height = 1 + max(self.getHeight(rNode.left), self.getHeight(rNode.right))

		return rNode


	def rotateRight(self, node):

		# Rotates the tree to the right. The node to the left goes to the place
		# where the received node was.

		lNode = node.left
		node.left = lNode.right
		lNode.right = node

		# update height of the nodes
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
		lNode.height = 1 + max(self.getHeight(lNode.left), self.getHeight(lNode.right))

		return lNode


	def rotateLeftRight(self, node):

		# A.k.a. double right rotation
		# consists of a left rotation then a right rotation.

		node = self.rotateLeft(node.left)
		return self.rotateRight(node)


	def rotateRightLeft(self, node):

		# A.k.a. double left rotation
		# consists of a right rotation then a left rotation.

		node = self.rotateRight(node.right)
		return self.rotateLeft(node)


	def rebalance(self, node):

		# Recursively rebalances the tree with rotations.

		if node is not None:
			
			node.left = self.rebalance(node.left)
			node.right = self.rebalance(node.right)
			balance = self.getBalance(node)
			balanceL = self.getBalance(node.left)
			balanceR = self.getBalance(node.right)

			if balance > 1: # if the BF of the node is positive and...
				
				if balanceR >= 0: # ...right child is positive, rotate left.
					node = self.rotateLeft(node)

				elif balanceR < 0: # ...left child is negative, rotate right, then left.
					node = self.rotateRightLeft(node)
					
			elif balance < -1: # if the BF of the node is negative and...
				if balanceL >= 0: # ...left child is positive, rotate left, then right.
					node = self.rotateLeftRight(node)

				elif balanceL < 0: # ...left child is negative, rotate right.
					node = self.rotateRight(node)
		
		return node


	def insertMultipleElements(self, elements):

		# Reads the file into a string, which is converted to an auxiliar list
		# for inserting its elements into the AVL tree.

		for element in elements:
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
		self.root = self.rebalance(self.root)
		

	def _insert(self, data, node):

		# Recursive insertion.

		if node is None:
			return Node(data)
		else:
			stat = self._compare(data, node.data)

			if stat < 0:
				node.left = self._insert(data, node.left)

			else:
				node.right = self._insert(data, node.right)

		# Updating height of the inserted node.
		node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

		return node


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

		# Searches for elements that are both in the list and in the AVL tree.

		same = []
		for element in group:
			if self.search(element) is not None:
				same.append(element)

		return same


	def insertDifferent(self, group):

		# Inserts the elements that are in the list and not in the AVL tree.

		different = []
		for element in group:
			if self.search(element) is None:
				different.append(element)

		for element in different:
			self.insert(element)


	def removeSame(self, group):

		# Removes the elements of the list that are in the AVL tree and in the list
		# at the same time.

		same = self.searchSame(group)

		for element in same:
			group.remove(element)


	def printTree(self):
		self._printTree(self.root)


	def _printTree(self, node):	

		# Recursive print of the tree in pre order.

		if node is not None:
			print(str(node.data) + ' ' + str(node.balance))
			self._printTree(node.left)
			self._printTree(node.right)