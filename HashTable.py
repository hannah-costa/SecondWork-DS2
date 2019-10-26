class HashTable(object):
	# TODO!!!
	def __init__(self):
		self.hashTable = []

	def fileLines(self, filename):
		lines = 0
		for line in open(filename, "r"):
			lines += 1

		return lines

	def readFile(self, filename):
		index = 0
		lines = self.fileLines(filename)
		for line in open(filename, "r"):
			index = hash(line[:-1]) % lines
			if index