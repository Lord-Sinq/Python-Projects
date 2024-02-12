'''
Name: Sinclair DeYoung
Date: Jun 9, 2023
Description: This file uses AVL tree's to balance and re organize a binary tree.
This can be used to take random numbers and organize them in a tree.
'''
# calling Binary files
from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    '''
    This class use's two other classes to build a binary tree and make it
    balanced following AVL's case's
    '''
    def balanced(self):
        '''
        This function checks for an imbalance in the Tree
        '''
        if self.getLeftChild() is not None:
            lHeight = self.getLeftChild().getHeight()
        else:
            lHeight = -1
        if self.getRightChild() is not None:
            rHeight = self.getRightChild().getHeight()
        else:
            rHeight = -1
        return (abs(lHeight - rHeight) < 2)
    def insert(self, x):
        '''
        This function inserts a new value into the AVL Tree
        '''
        if self.isEmpty():
            self.setPayload(x)
            return self
        elif x < self.getPayload():
            if self.getLeftChild() is None:
                self.setLeftChild(AVLTree(x))
                self.computeHeight()
                return self
            else:
                self.setLeftChild(self.getLeftChild().insert(x))
                if not self.balanced():
                    # case 1
                    if x < self.getLeftChild().getPayload():
                        return self.rotateWithLeftChild()
                    # case 2
                    else:
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                        return (self.rotateWithLeftChild())
                self.computeHeight()
                return self
        else:
            if self.getRightChild() is None:
                self.setRightChild(AVLTree(x))
                self.computeHeight()
                return self
            else:
                self.setRightChild(self.getRightChild().insert(x))
                if not self.balanced():
                    # case 4
                    if x >= self.getRightChild().getPayload():
                        return self.rotateWithRightChild()
                    # case 3
                    else:
                        self.setRightChild(self.getRightChild().rotateWithLeftChild())
                        return (self.rotateWithRightChild())
                self.computeHeight()
                return self
    def rotateWithLeftChild(self):
        '''
        This function rotates self with its left child
        '''
        k1 = self.getLeftChild()
        if k1 is not None:
            # move the child of k1 over to self
            self.setLeftChild(k1.getRightChild())
            # hang self off of k1
            k1.setRightChild(self)
            # compute the height
            self.computeHeight()
            k1.computeHeight()
            # returns the root
            return k1
    def rotateWithRightChild(self):
        '''
        This function rotates self with its right child
        '''
        k2 = self.getRightChild()
        if k2 is not None:
            # move the child of k1 over to self
            self.setRightChild(k2.getLeftChild())
            # hang self off of k1
            k2.setLeftChild(self)
            # compute the height
            self.computeHeight()
            k2.computeHeight()
            # returns the root
            return k2

def main():
    '''
    Main function used to test the AVL tree class
    '''
    avlBST = AVLTree()
    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]
    # using a for loop to grab evey element in the values list
    # to add them to the binary tree
    for i in values:
        avlBST = avlBST.insert(i)
        print(avlBST)
    else:
        None
    print('The final reults of the binary tree are below:','\n', avlBST)

if __name__ == '__main__':
    main()