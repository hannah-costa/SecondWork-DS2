class Node(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		self.balance = 0 # balance factor of the node

		
class AVLTree(object):
	def __init__(self):
		self.root = None


	def calculateBF(self):
		


	def balance(self, node):
		# TODO!!!


	def leftRotation(self):



	def rightRotation(self):



	def leftRightRotation(self):



	def rightLeftRotation(self):




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

		return node
		