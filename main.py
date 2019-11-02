import LinkedList as LL
import HashTable as HT
import BinaryTree as BT
import AVLTree as AVL
import RBTree as RB

if __name__ == '__main__':
	groupA = LL.LinkedList()
	groupA.readFile("fileA.txt")
	print("group A: ", groupA.group)

	groupB = HT.HashTable()
	groupB.readFile("fileB.txt")
	print("groupB: ", groupB.hashTable)
	# groupB.printTree()
	# print(groupB.searchSame(groupA.group))
	groupB.removeSame(groupA.group)
	print("new groupA: ", groupA.group)