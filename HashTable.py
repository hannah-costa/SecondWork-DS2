class HashTable(object):

	def __init__(self):
		self.hashTable = []
		self.length = 0

		self.comparisons = 0
		self.attributions = 0
		

	def _indexer(self, length, element):

		# Returns the index of the next free position for element.

		index = hash(element) % length
		self.attributions += 1
		if index < 0:
			self.comparisons += 1
			index *= -1
			self.attributions += 1

		if self.hashTable[index] is not None:
			self.comparisons += 1
			i = 1
			self.attributions += 1
			while self.hashTable[index] != None and i <= length:
				self.comparisons += 2
				index = (index + i**2) % length
				self.attributions += 1
				i += 1
				self.attributions += 1
			
			if i > length: # Could not find a valid index.
				self.comparisons += 1
				return None

		return index


	def isFull(self):

		# Checks if the hashtable is full.

		if None in self.hashTable:
			self.comparisons += 1
			return False
		return True


	def _realloc(self):

		# Reallocates 50% more space for the hashtable.

		newHashTable = [None] * int(self.length * 1.5)
		self.attributions += 1
		for element in self.hashTable:
			self.attributions += 1
			self._insert(newHashTable, element)

		self.hashTable = newHashTable
		self.attributions += 1
		self.length = len(self.hashTable)
		self.attributions += 1


	def _insert(self, hashTable, element):

		# _insert function has to be generic and takes hashTable as a 
		# parameter because of _realloc().

		if self.isFull():
			self.comparisons += 1
			self._realloc()

		index = self._indexer(len(hashTable), element)
		self.attributions += 1
		if index is not None:
			self.comparisons += 1
			hashTable.insert(index, element)
			self.attributions += 1


	def insertMultipleElements(self, elements):

		# Reads the file into a string which is converted to an auxiliar list
		# for inserting the elements into the hashtable.

		self.hashTable = [None] * int(len(elements) * 1.5)
		self.attributions += 1
		self.length = len(self.hashTable)
		self.attributions += 1

		for element in elements:
			self.attributions += 1
			self._insert(self.hashTable, element)


	def _search(self, element):

		# Returns the index of the element searched if found.
		# Returns None otherwise.

		length = self.length
		self.attributions += 1
		index = hash(element) % length
		self.attributions += 1
		if index < 0:
			self.comparisons += 1
			index *= -1
			self.attributions += 1

		if self.hashTable[index] != element:
			self.comparisons += 1
			i = 1
			self.attributions += 1
			while self.hashTable[index] != element and i <= length:
				self.comparisons += 2
				index = (index + i**2) % length
				self.attributions += 1
				i += 1
				self.attributions += 1
			
			if i > length: # Could not find a valid index.
				self.comparisons += 1
				return None

		return index


	def searchSame(self, group):

		# Searches for elements that are both in the list and in the hashtable.

		same = []
		self.attributions += 1
		for element in group:
			self.attributions += 1
			found = self._search(element)
			self.attributions += 1
			if found is not None:
				self.comparisons += 1
				same.append(element)
				self.attributions += 1

		return same

			
	def insertDifferent(self, group):

		# Inserts the elements that are in the list and not in the hashtable.

		for element in group:
			self.attributions += 1
			found = self._search(element)
			self.attributions += 1
			if found is None:
				self.comparisons += 1
				self._insert(self.hashTable, element)


	def removeSame(self, group):

		# Removes the elements of the list that are in the hashtable and in the list
		# at the same time.

		same = self.searchSame(group)
		self.attributions += 1
		for element in same:
			self.attributions += 1
			group.remove(element)
			self.attributions += 1
