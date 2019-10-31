class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		self.balance = 0 # balance factor of the node

		
class AVLTree(object):
	def __init__(self):
		self.root = None


	def printBF(self):
		BF = self.calculateBF(self.root)
		print(BF)


	def calculateHeight(self, node):

		# recursively calculates the height of the tree using this formula:
		# Height = 1 + max(Height(left) + Height(right))
		# Where Height(left/right) is the height of the left/right subtree.
		if node is None:
			return -1

		lHeight = self.calculateHeight(node.left)
		rHeight = self.calculateHeight(node.right)

		return 1 + max(lHeight, rHeight)

	def updateBF(self, node):

		# updates the balance factor (BF) of every element in the tree using
		# this formula:
		# BF = Height(left) - Height(right)

		lHeight = self.calculateHeight(node.left)
		rHeight = self.calculateHeight(node.right)

		node.balance = rHeight - lHeight


	def rotateLeft(self, node):
		# rotates the tree to the left. The node to the right goes to the place
		# where the received node was.

		rNode = node.right
		node.right = rNode.left
		rNode.left = node

		if node == self.root:
			self.root = rNode

		# return rNode


	def rotateRight(self, node):
		# rotates the tree to the right. The node to the left goes to the place
		# where the received node was.

		lNode = node.left
		node.left = lNode.right
		lNode.right = node

		if node == self.root:
			self.root = lNode

		# return lNode


	def rotateLeftRight(self, node):

		# a.k.a. double right rotation
		# consists of a left rotation then a right rotation.

		node.left = self.rotateLeft(node.left)
		return self.rotateRight(node)


	def rotateRightLeft(self, node):

		# a.k.a. double left rotation
		# consists of a right rotation then a left rotation.

		node.right = self.rotateRight(node)
		return self.rotateLeft(node)


	def rebalance(self, node):

		# rebalances the tree with rotations.
		# TODO: fix this!!!
		if node is not None:
			self.rebalance(node.left)
			self.rebalance(node.right)
			node.balance = self.calculateBF(node)

			if node.balance > 1:
				if node.right.balance < -1:
					
				elif node:
					

			elif node.balance < -1: # if the BF of the node is negative and...
				# ...the left son is positive, double rotate right (rotate left, then right).
				if node.left.balance >= 0:
					self.rotateLeftRight(node)

				# ...the son is negative, rotate right.
				elif node.right.balance < 0:
					


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
		# TODO: after inserting, balance the tree

		if node is None:
			node = Node(data)
		else:
			stat = self._compare(data, node.data)
			if stat < 0:
				node.left = self._insert(data, node.left)
			else:
				node.right = self._insert(data, node.right)

		self.updateBF(node)
		return node
		

	def printTree(self):
		self._printTree(self.root)


	# recursive print
	def _printTree(self, node):	
		if node is not None:
			print(node.data)
			self._printTree(node.left)
			self._printTree(node.right)