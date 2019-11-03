import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB

def readFile(filename):
	with open(filename, "r") as file:
		string = file.read()

	elements = [int(x) for x in string[1:-2].split(", ") ]
	return elements

if __name__ == '__main__':
	# groupA = LL.LinkedList()
	# groupA.insertMultipleElements( readFile("fileA.txt") )
	# print(groupA.group)

	# groupB = BT.BinaryTree()
	# groupB.insertMultipleElements(readFile("fileB.txt"))
	# groupB.removeSame(groupA.group)
	# print(groupA.group)

	groupB = AVL.AVLTree()
	groupB.insertMultipleElements(readFile("fileA.txt"))
	groupB.printTree()

	# groupB = HT.HashTable()
	# groupB.readFile("fileB.txt")
	# groupB.removeSame(groupA.group)
	# print(groupA.group)