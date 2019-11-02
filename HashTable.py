class HashTable(object):

	def __init__(self):
		self.hashTable = []
		self.length = 0
		

	def _indexer(self, length, element = None):

		# Returns the index of a certain element. If no element parameter is received,
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
				
			if i > length: # Could not find a valid index.
				return None

			return index



	def isFull(self):

		# Checks if the hashtable is full.

		if None in self.hashTable:
			return False
		return True


	def _realloc(self):

		# Reallocates 50% more space for the hashtable.

		newHashTable = [None] * int(self.length * 1.5)
		for element in self.hashTable:
			self._insert(newHashTable, element)

		self.hashTable = newHashTable
		self.length = len(self.hashTable)


	def _insert(self, hashTable, element):

		# _insert function has to be generic and takes hashTable as a 
		# parameter because of _realloc().

		if self.isFull():
			self._realloc()

		index = self._indexer(len(hashTable))
		if index is not None:
			hashTable.insert(index, element)


	def readFile(self, filename):

		# Reads the file into an auxiliar list and converts it into a hashtable.

		elements = []
		for line in open(filename, "r"):
			elements.append(int(line[:-1])) # Change this line according to the type in the file.


		self.length = len(elements)
		self.hashTable = [None] * int(self.length * 1.5)

		for element in elements:
			self._insert(self.hashTable, element)

		elements.clear()


	def _search(self, element):

		# Returns the index of the element searched if found.
		# Returns None otherwise.

		return self._indexer(self.length, element)

	def searchSame(self, group):

		# Searches for elements that are both in the list and in the hashtable.

		same = []
		for element in group:
			found = self._search(element)
			if found is not None:
				same.append(element)

		return same

			
	def insertDifferent(self, group):

		# Inserts the elements that are in the list and not in the hashtable.

		for element in group:
			found = self._search(element)
			if found is None:
				self._insert(self.hashTable, element)


	def removeSame(self, group):

		# Removes the elements of the list that are in the hashtable and in the list
		# at the same time.

		same = self.searchSame(group)
		for element in same:
			group.remove(element)
