'''
Name: Sinclair DeYoung
Date: Jun 6, 2023
Description: Binary Tree, this python file first builds a binary tree
and then shows the results of traversing through the tree.
This demonstrates how to get In, Pre, and Post traversals involving a Binary Tree
'''

class BinaryTree:
    '''
    This class is used for traversing a Binary Tree.
    This allows for post, in, and pre order traversals to show how moving around
    the tree can produce different results.
    '''
    def __init__(self, payload=None,leftchild=None,rightchild=None):
        self.__payload = payload
        self.__leftChild = leftchild
        self.__rightChild = rightchild
    def getPayload(self):
        # get the payload
        return self.__payload
    def setPayload(self,payload):
        # set the payload
        self.__payload = payload
    def getLeftChild(self):
        # get the left branch of the tree
        return self.__leftChild
    def setLeftChild(self, leftchild):
        # set the left branch of the tree
        self.__leftChild = leftchild
    def getRightChild(self):
        # get the right branch of the tree
        return self.__rightChild
    def setRightChild(self,rightchild):
        # set the right branch of the tree
        self.__rightChild = rightchild
    def __str__(self):
        # string
         return self.inorderTraversal()
    def inorderTraversal(self):
        '''
        This function traverses in the middle of the root node
        '''
        result = " "
        if self.isEmpty():
            return result
        else:
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().preorderTraversal()
            result += ' ' + str(self.getPayload())
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().preorderTraversal()
            return result
    def preorderTraversal(self):
        '''
        This function traversesbefore the root node
         '''
        result = " "
        if self.isEmpty():
            return result
        else:
            result += str(self.getPayload())
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().preorderTraversal()
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().preorderTraversal()
            return result
    def postorderTraversal(self):
        '''
        This function traverses after the root node
        '''
        result = " "
        if self.isEmpty():
            return result
        else:
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().preorderTraversal()
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().preorderTraversal()
            result += ' ' + str(self.getPayload())
            return result
    def isEmpty(self):
        # checks for an empty tree
        return self.__payload is None

def main():
    '''
    This main function was provided for this lab.
    '''
    BT = BinaryTree()
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)
    BT.setPayload(101)
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)
    BT.setLeftChild(BinaryTree(50))
    print(BT)
    BT.setRightChild(BinaryTree(250))
    print(BT)
    BT.getLeftChild().setLeftChild(BinaryTree(42))
    print(BT)
    BT.getLeftChild().getLeftChild().setLeftChild(BinaryTree(31))
    print(BT)
    BT.getRightChild().setRightChild(BinaryTree(315))
    print(BT)
    BT.getRightChild().setLeftChild(BinaryTree(200))
    print(BT)
    print("Inorder traversal: " + BT.inorderTraversal())
    print("Preorder traversal: " + BT.preorderTraversal())
    print("Postorder traversal: " + BT.postorderTraversal())
if __name__ == '__main__':
    main()