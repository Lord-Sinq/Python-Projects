'''
Name: Sinclair DeYoung
Date: Jun 7, 2023
Description: Lab_9 is an extension on Lab_8. Adding Height, computeHeight, insert, find, minValue
, and maxValue.
Allowing you to search the tree for specific elements or insert and element.
'''
# import Lab_8 file
from BinaryTree import BinaryTree
# Lab_9
class BinarySearchTree(BinaryTree):
    def __init__(self, payload = None, leftchild = None, rightchild = None):
        '''
        construtor that overloads BinaryTree's construtor
        '''
        BinaryTree.__init__(self, payload, leftchild, rightchild)
        if (self.getPayload() is None):
            self.__height = -1
        else:
            self.__height = 0
    def getHeight(self):
        '''
        Gets the height of the binary tree
        '''
        return self.__height
    def computeHeight(self):
        '''
        Used to calculate the height of the binary tree
        '''
        height = -1
        if (self.getLeftChild() is not None):
            height = max(height, self.getLeftChild().getHeight())
        if (self.getRightChild() is not None):
            height = max(height, self.getRightChild().getHeight())
        self.__height = height + 1
    def setPayload(self, x):
        '''
        Sets the payload using the binarytree class in the binary tree file
        '''
        BinaryTree.setPayload(self, x)
        self.computeHeight()
    def insert(self, x):
        '''
        Insert a new value into the Binary Search Tree
        '''
        # checks for an empty tree
        if self.isEmpty():
            self.setPayload(x)
        # must use a < not a <= as if it is equal it must go on the right side
        elif x < self.getPayload():
            if self.getLeftChild() is None:
                # there is no left subtree
                self.setLeftChild(BinarySearchTree(x))
                self.computeHeight()
            else:
                # Recursively put into left subtree
                self.getLeftChild().insert(x)
                self.computeHeight()
        else: # x >= self.payload
            if self.getRightChild() is None:
                # there is no right subtree
                self.setRightChild(BinarySearchTree(x))
                self.computeHeight()
            else:
                # Recursively put into right subtree
                self.getRightChild().insert(x)
                self.computeHeight()
    def find(self, x):
        '''
         Find a specific element in the Binary Tree
        '''
        # checks for empty
        if self.isEmpty():
            return None
        # if x is equal to payload
        elif x == self.getPayload():
            return self.getPayload()
        # if x is less then payload
        elif x < self.getPayload():
            # checks that the left spot is holding x
            if self.getLeftChild() is None:
                return None
            else:
                return self.getLeftChild().find(x)
        # checks the right for x
        else:
            if self.getRightChild() is None:
                return None
            else:
                return self.getRightChild().find(x)
    def minValue(self):
        '''
        Searches for the min value and returns the min value
        :return:
        '''
        if self.getLeftChild() is None:
            return self.getPayload()
        else:
            return self.getLeftChild().minValue()
    def maxValue(self):
        '''
        Searches for the max value and returns the max value
        '''
        if self.getRightChild() is None:
            return self.getPayload()
        else:
            return self.getRightChild().maxValue()
    def inorderTraversal(self):
        '''
        This function traverses in the middle of the root node
        '''
        result = " "
        if self.isEmpty():
            return result
        else:
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().inorderTraversal()
            result += ' ' + str(self.getPayload()) + "(" + str(self.getHeight()) + ")"
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().inorderTraversal()
            return result
def main():
    '''
    This main function uses insert to add to the binary tree not
    setter's.
    '''
    # the class
    BST = BinarySearchTree()
    # Insert values to make the tree
    BST.insert(8)
    BST.insert(3)
    BST.insert(9)
    BST.insert(2)
    BST.insert(4)
    BST.insert(11)
    BST.insert(15)
    BST.insert(14)
    BST.insert(12)
    BST.insert(7)
    # Shows the in order list traversal
    print("In order tree Traversal:",'\n',BST.inorderTraversal())
    # Get the height of the tree
    print("Height of the tree:", BST.getHeight())
    # Find a value in the tree
    value = [9,6,5,14]
    for v in value:
        result = BST.find(v)
        if result is not None:
            print("Found ", v, "in the binary tree")
        else:
            print(v, "not found in the binary tree")
    # Find the minimum and maximum values
    print("Minimum value:", BST.minValue())
    print("Maximum value:", BST.maxValue())

if __name__ == "__main__":
    main()