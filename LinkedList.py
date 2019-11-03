class LinkedList(object):
	def __init__(self):

		# I called the list 'group' since 'list' is a reserved word.

		self.group = []

	def insertMultipleElements(self, elements):

		# Appends elements to the end of the list.

		self.group += elements


	def searchSame(self, group):

		# Searches for elements that are both in the list received and in this list.

		found = []
		for selfElement in self.group:
			for element in group:
				if selfElement == element:
					found.append(selfElement)
					break

		return found


	def insertDifferent(self, group):

		# Inserts the elements that are in the list received and not in this list.

		different = self.group
		for selfElement in self.group:
			for element in group:
				if selfElement == element:
					different.remove(element)
					break

		for element in different:
			self.group.append(element)


	def removeSame(self, group):

		# Removes the elements of the list received that are in it and in this list
		# at the same time.

		same = self.searchSame(group)
		for element in same:
			self.group.remove(element)
