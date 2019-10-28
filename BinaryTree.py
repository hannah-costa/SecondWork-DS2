class Node(object):
	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data

	def setData(self, data):
		self.data = data

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right



class BinaryTree(object):
	def __init__(self):
		self.root = None


	# change this function depending on the type you're dealing with.
	# made for ints
	def _compare(self, newData, oldData):
		if newData > oldData:
			return 1
		elif newData < oldData:
			return -1
		else:
			return 0

	# def insert(self, data):
	# 	self._insert(data, self.root)

	def insert(self, data):
		self.root = self._insert(data, self.root)


	def _insert(self, data, node):
		if node is None:
			node = Node(data)
		else:
			stat = self._compare(data, node.data)
			if stat < 0:
				node.left = self._insert(data, node.left)
			else:
				node.right = self._insert(data, node.right)

		return node

	# def readFile(self, filename):



	# def _remove(self, node):


	# def _search(self, node):


	# def searchSame(self, group):


	# def insertDifferent(self, group):


	# def removeSame(self, group):


	def printTree(self):
		self._printTree(self.root)


	def _printTree(self, node):	
		if node != None:
			self._printTree(node.left)
			print(node.data, ' ')
			self._printTree(node.right)
