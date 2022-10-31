# This project practice using BinarySearchTree to complete a simple application that can accept ANY number of tree node
# integer values to create a binary tree and output the parent of its nodes,the number of non-leaf nodes, and the number
# of leaf nodes shown in the sample output.

from Node import Node
from BinarySearchTree import BinarySearchTree

def createBinaryTree():
    Tree = BinarySearchTree()
    while True:
        nodevalue = input("Please input ONE node integer value:")
        Tree.insertNode(int(nodevalue))
        user_y_n = input("Want to input more node integer value?(Yes/No)")  # Ask user if input new node.
        if user_y_n == "Yes" or user_y_n == "yes" or user_y_n == "YES":
            pass
        else:
            break
    return Tree


def printBinaryTree(Tree):
    print()
    print(str(Tree.getRoot().getVal()) + " is a root node.")
    lst = Tree.printParentNode().split()
    for x in lst:  # Search all parent nodes' child nodes.
        if Tree.searchNode(int(x)).getLeft() is not None:
            LeftNode = Tree.searchNode(float(x)).getLeft()
            print(x + " is the parent of " + str(LeftNode.getVal()))
        if Tree.searchNode(int(x)).getRight() is not None:
            RightNode = Tree.searchNode(float(x)).getRight()
            print(x + " is the parent of " + str(RightNode.getVal()))
    print()
    print("The number of leaves nodes of this tree: ", Tree.countLeaves())
    print()
    print("The number of non-leaves nodes of this tree: ", Tree.countNonLeaves())


def main():
    print("Let's create a binary tree!")
    while True:
        MyTree = createBinaryTree()  # Call the createBinaryTree()
        printBinaryTree(MyTree)    # Call the printBinaryTree()
        newtree_y_n = input("Is there any new tree?(Yes/No)")  # Ask user if create a new tree.
        if newtree_y_n == "Yes" or newtree_y_n == "yes" or newtree_y_n == "YES":
            pass
        elif newtree_y_n == "No" or newtree_y_n == "no" or newtree_y_n == "NO":
            break
    print()
    print("Thank You for Using My Application")

if __name__ == "__main__":
    main()
