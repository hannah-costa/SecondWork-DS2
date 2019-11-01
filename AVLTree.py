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

		print("rotating left...")
		rNode = node.right
		node.right = rNode.left
		rNode.left = node

		if node == self.root:
			self.root = rNode

		return rNode


	def rotateRight(self, node):
		# rotates the tree to the right. The node to the left goes to the place
		# where the received node was.

		print("rotating right...")
		lNode = node.left
		node.left = lNode.right
		lNode.right = node

		if node == self.root:
			self.root = lNode

		return lNode


	def rotateLeftRight(self, node):

		# a.k.a. double right rotation
		# consists of a left rotation then a right rotation.

		print("rotating left then right...")
		node.left = self.rotateLeft(node.left)
		return self.rotateRight(node)


	def rotateRightLeft(self, node):

		# TODO: CHECK THIS
		# a.k.a. double left rotation
		# consists of a right rotation then a left rotation.

		print("rotating right then left...")
		node.right = self.rotateRight(node.right)
		return self.rotateLeft(node)


	def rebalance(self, node):

		# rebalances the tree with rotations.
		# TODO: test this!!!
		if node is not None:
			self.rebalance(node.left)
			self.rebalance(node.right)
			node.balance = self.updateBF(node)

			if node.balance > 1: # if the BF of the node is positive and...
				# ...the right son is negative, double rotate left (rotate right, then left).
				if node.right.balance <= 0:
					node = self.rotateRightLeft(node)

				# ...the left son is positive, rotate left.
				elif node.left.balance > 0:
					node = self.rotateLeft(node)
					

			elif node.balance < -1: # if the BF of the node is negative and...
				# ...the left son is positive, double rotate right (rotate left, then right).
				if node.left.balance >= 0:
					node = self.rotateLeftRight(node)

				# ...the right son is negative, rotate right.
				elif node.right.balance < 0:
					node = self.rotateRight(node)


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