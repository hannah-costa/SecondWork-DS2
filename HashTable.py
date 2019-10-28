class HashTable(object):
	# TODO: setLength and getLength
	def __init__(self):
		self.hashTable = []
		self.length = 0
		

	def _indexer(self, length, element = None):
		# returns the index of a certain element. If no element parameter is received,
		# returns the index of the next free position for element.
		index = hash(element) % length
		if index < 0:
			index *= -1

		if self.hashTable[index] == element:
			return index

		else:
			i = 1
			while self.hashTable[index] != element and i <= length:
				index = (index + i**2) % length
				i += 1
				
			if i > length: # could not find a valid index
				return None

			return index



	def isFull(self):
		# checks if the hashtable is full.
		if None in self.hashTable:
			return False
		return True


	def _realloc(self):
		# reallocates 50% more space for the hashtable.
		newHashTable = [None] * int(self.length * 1.5)
		for element in self.hashTable:
			self._insert(newHashTable, element)

		self.hashTable = newHashTable
		self.length = len(self.hashTable)


	def _insert(self, hashTable, element):
		# _insert function takes hashTable as a parameter because of _realloc().
		if self.isFull():
			self._realloc()

		index = self._indexer(len(hashTable))
		if index is not None:
			hashTable.insert(index, element)


	def readFile(self, filename):
		# reads the file into an auxiliar list and converts it into a hashtable.

		elements = []
		for line in open(filename):
			elements.append(line[:-1])


		self.length = len(elements)
		self.hashTable = [None] * int(self.length * 1.5)

		for element in elements:
			self._insert(self.hashTable, element)

		elements.clear()


	def _search(self, element):
		# returns the index of the element searched if found.
		# returns None otherwise.

		return self._indexer(self.length, element)

	def searchSame(self, group):
		same = []
		for element in group:
			found = self._search(element)
			if found is not None:
				same.append(element)

		return same

			
	def insertDifferent(self, group):
		# Inserts the elements that are in group A and not in the hashtable.

		for element in group:
			found = self._search(element)
			if found is None:
				self._insert(self.hashTable, element)

		return self.hashTable


	def removeSame(self, group):
		# Removes the elements of the group that are in the hashtable and in the group
		# at the same time.

		for element in group:
			found = self._search(element)
			if found is not None:
				group.remove(element)
