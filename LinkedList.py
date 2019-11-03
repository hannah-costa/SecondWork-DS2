class LinkedList(object):
	def __init__(self):

		# I called the list 'group' since 'list' is a reserved word.

		self.group = []
		self.comparisons = 0
		self.attributions = 0


	def insertMultipleElements(self, elements):

		# Appends elements to the end of the list.

		self.group += elements
		self.attributions += len(elements)


	def searchSame(self, group):

		# Searches for elements that are both in the list received and in this list.

		found = []
		self.attributions += 1
		for selfElement in self.group:
			self.attributions += 1
			for element in group:
				self.attributions += 1
				if selfElement == element:
					self.comparisons += 1
					found.append(selfElement)
					self.attributions += 1
					break

		return found


	def insertDifferent(self, group):

		# Inserts the elements that are in the list received and not in this list.

		# different = self.group
		# self.attributions += 1
		# for selfElement in self.group:
		# 	self.attributions += 1
		# 	for element in group:
		# 		self.attributions += 1
		# 		if selfElement == element:
		# 			self.comparisons += 1
		# 			different.remove(element)
		# 			self.attributions += 1
		# 			break

		# for element in different:
		# 	self.attributions += 1
		# 	self.group.append(element)
		# 	self.attributions += 1

		different = []
		self.attributions += 1
		for selfElement in self.group:
			self.attributions += 1
			if selfElement not in group:
				self.comparisons += 1
				different.append(selfElement)
				self.attributions += 1

		for element in different:
			self.attributions += 1
			self.group.append(element)
			self.attributions += 1


	def removeSame(self, group):

		# Removes the elements of the list received that are in it and in this list
		# at the same time.

		same = self.searchSame(group)
		self.attributions += 1
		for element in same:
			self.attributions += 1
			self.group.remove(element)
			self.attributions += 1
