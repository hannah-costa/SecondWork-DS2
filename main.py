import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB

if __name__ == '__main__':
	groupA = LL.LinkedList()
	groupA.readFile("fileA.txt")

	groupB = AVL.AVLTree()
	groupB.readFile("fileB.txt")
	groupB.printTree()
