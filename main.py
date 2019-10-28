import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB

if __name__ == '__main__':
	groupA = LL.LinkedList()
	groupA.readFile("fileA.txt")

	groupB = BT.BinaryTree()
	groupB.readFile("fileB.txt")
	# groupB.printTree()
	print("----------------------")
	print(groupB.searchSame(groupA.group))