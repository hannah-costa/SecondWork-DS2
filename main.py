import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB
import time
import sys

def readFile(filename):
	with open(filename, "r") as file:
		string = file.read()

	elements = [int(x) for x in string[1:-1].split(", ") ]
	return elements


if __name__ == '__main__':
	sys.setrecursionlimit(500000)
	print("reading files...")
	groupA = LL.LinkedList()
	groupA.insertMultipleElements( readFile("file100000.txt") )

	# groupB = LL.LinkedList()
	# groupB.insertMultipleElements(readFile("file500000.txt"))

	groupB = HT.HashTable()
	groupB.insertMultipleElements(readFile("file500000.txt"))

	# groupB = BT.BinaryTree()
	# groupB.insertMultipleElements(readFile("file500000.txt"))
	#groupB.printTree()

	# groupB = AVL.AVLTree()
	# groupB.insertMultipleElements(readFile("file500000.txt"))

	start = time.time()
	print("doing first operation...")
	groupB.searchSame(groupA.group)
	end = time.time()
	print("elapsed time for op1: ", end-start)

	start = time.time()
	print("doing second operation...")
	groupB.insertDifferent(groupA.group)
	end = time.time()
	print("elapsed time for op2: ", end-start)


	start = time.time()
	print("doing third operation...")
	groupB.removeSame(groupA.group)
	end = time.time()
	print("elapsed time for op3: ", end-start)


	print("GROUP A - attributions: ", groupA.attributions, "; comparisons: ", groupA.comparisons)
	print("GROUP B - attributions: ", groupB.attributions, "; comparisons: ", groupB.comparisons)
