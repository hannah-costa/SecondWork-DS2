class LinkedList(object):
	def __init__(self):
		self.group = []

	def readFile(self, filename):
		for line in open(filename, "r"):
			self.group.append(line[:-1])

	def searchSame(self, group):
		found = []
		for selfElement in self.group:
			for element in group:
				if selfElement == element:
					found.append(selfElement)
					break

		return found

	def insertDifferent(self, group):
		different = self.group
		for selfElement in self.group:
			for element in group:
				if selfElement == element:
					different.remove(element)
					break

		for element in different:
			group.append(element)

		return group

	def removeSame(self, group):
		same = self.searchSame(group)
		for element in same:
			self.group.remove(element)

		return same


class HashTable(object):
	# TODO!!!
	def __init__(self, arg):
		super(Hash, self).__init__()
		self.arg = arg
		

if __name__ == '__main__':
	groupA = LinkedList()
	groupA.readFile("fileA.txt")
	groupB = LinkedList()
	groupB.readFile("fileB.txt")

	print(groupA.removeSame(groupB.group))
	print(len(groupA.group))
	# print(groupA.insertDifferent(groupB.group))
