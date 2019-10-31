import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB

if __name__ == '__main__':
	groupA = LL.LinkedList()
	groupA.readFile("fileA.txt")

	groupB = AVL.AVLTree()
	groupB.insert(7)
	groupB.insert(3)
	groupB.insert(8)
	groupB.insert(2)
	groupB.insert(5)
	groupB.insert(4)
	groupB.insert(6)
	# groupB.insert(7)
	# groupB.insert(2)
	groupB.printTree()
	#groupB.leftRightRotation(groupB.root)
	# print("-------------------------")
	# groupB.printTree()
