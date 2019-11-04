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

	#################
	#    GROUP A    #
	#################

	# groupA = LL.LinkedList()
	# groupA.insertMultipleElements(readFile("file1000.txt"))

	#################
	#    GROUP B    #
	#################

	# groupB = LL.LinkedList()
	# groupB.insertMultipleElements(readFile("file5000.txt"))

	# groupB = BT.BinaryTree()
	# groupB.insertMultipleElements(readFile("file5000.txt"))

	# groupB = AVL.AVLTree()
	# groupB.insertMultipleElements(readFile("file5000.txt"))


	####################
	#    OPERATIONS    #
	####################

	# groupB.searchSame(groupA.group)
	# groupB.insertDifferent(groupA.group)
	# groupB.removeSame(groupA.group)
