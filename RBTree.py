class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.color = None
		

class RBTree(object):
	def __init__(self):
		self.root = None		