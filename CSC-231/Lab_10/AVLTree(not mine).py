# PROGRAM PURPOSE:... Lab 10
# AUTHOR:............ Lawlor, Nicholas
# COURSE:............ CSC 231-001
# TERM:.............. Summer 2023

from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def balanced(self):
        '''
        Return true if the tree is unbalanced.
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
        """
        Insert a value into the AVL tree.
        """
        # Since self cant be a non-existent tree, the only way for it to be
        # an empty tree is for it to have no payload.
        if self.isEmpty():
            self.setPayload(x)
            return self

        # if this is a <, instead of a <= then duplicates will go in the RST,
        # preserving the order in which they were inserted.
        elif x < self.getPayload():
            if self.getLeftChild() is None:
                self.setLeftChild(AVLTree(x))
                self.computeHeight()
                return self
            else:
                self.setLeftChild(self.getLeftChild().insert(x))

            if not self.balanced():
                # case 1
                if self.getLeftChild().getPayload() is not None and x < self.getLeftChild().getPayload():
                    return self.rotateWithLeftChild()
                # case 2
                else:
                    self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                    return (self.rotateWithLeftChild())

        else:
            if self.getRightChild() is None:
                self.setRightChild(AVLTree(x))
            else:
                self.setRightChild(self.getRightChild().insert(x))

            if not self.balanced():
                # case 4
                if self.getRightChild().getPayload() is not None and x > self.getRightChild().getPayload():
                    return self.rotateWithRightChild()
                # case 3
                else:
                    self.setRightChild(self.getRightChild().rotateWithLeftChild())
                    return (self.rotateWithRightChild())

        self.computeHeight()
        return self

    def rotateWithLeftChild(self):
        """
        Rotate self with its left child.
        """
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
        """
        Rotate self with its right child.
        """
        k2 = self.getRightChild()
        if k2 is not None:
            # move the child of k2 over to self
            self.setRightChild(k2.getLeftChild())
            # hang self off of k2
            k2.setLeftChild(self)
            # compute the height
            self.computeHeight()
            k2.computeHeight()
            # returns the root
            return k2

def main():
    """
    Main Function for testing.
    """

    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]

    avlBST = AVLTree()

    for x in values:
        avlBST = avlBST.insert(x)
        print(avlBST)

    print(" ",avlBST)



if __name__ == "__main__":
        main()