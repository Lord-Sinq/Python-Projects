'''
Name: Sinclair DeYoung
Date: May 31, 2023
Description: Lab_5 is about linked list.
'''
class ListNode:
    '''
    This is the list node that creates and assigns the values to their
    respected places.
    '''
    def __init__(self,payload,next=None):
        self.__payload = payload
        self.__next = next
    # getter
    def getPayload(self):
        return self.__payload
    # setter
    def setPayload(self, payload):
        self.__payload = payload
    # getter
    def getNext(self):
        return self.__next
    # setter
    def setNext(self, next):
        self.__next = next

class LinkedList:
    '''
    This class is used for making the elements being sent to it follow certain
    parameters.
    '''
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    # used to get a specific place in the node
    def __getIthNode(self,i):
        if i < 0:
            i = self.__size + i
        elif i >= self.__size:
            raise IndexError ('List index out of range')
        current = self.__head
        count = 0
        while current is not None and count < i:
            count += 1
            current = current.getNext()
        return current
    # places values in new spots
    def insert(self,i,x):
        if self.isEmpty():
            self.__head = ListNode(x)
            self.__tail = self.__head
        elif i <= 0:
            self.__head = ListNode(x, self.__head)
        elif i >= self.__size:
            self.__tail.setNext(ListNode(x))
            self.__tail = self.__tail.getNext()
        else:
            previous = self.__getIthNode(i - 1)
            previous.setNext(ListNode(x, previous.getNext()))
            if self.__tail == previous:
                self.__tail = self.__tail.getNext()
        self.__size += 1
    # front
    def front(self):
        if self.__head is None:
            raise IndexError('List index out of range')
        return self.__head.getPayload()
    # back
    def back(self):
        if self.__tail is None:
            raise IndexError('List index out of range')
        return self.__tail.getPayload()
    # size of node
    def __len__(self):
        return self.__size
    # Check if empty
    def isEmpty(self):
        return self.__head is None
    # string
    def __str__(self):
        result = ''
        current = self.__head
        while current is not None:
            result += str(current.getPayload()) + ''
            current = current.getNext()
        return result.strip()

def main():
    myList = LinkedList()
    # Test len(), is_empty(), and printing of the list before putting anything into it
    print("Length:", len(myList))
    print("Is empty?", myList.isEmpty())
    print("List:", myList)
    # Insert values into the list and test various operations
    # Insert at the beginning
    myList.insert(0, 10)
    print("List:", myList)
    # Insert in the middle
    myList.insert(1, 20)
    print("List:", myList)
    # Insert at the end
    myList.insert(-1, 30)
    print("List:", myList)
    # Test front(), back(), len(), is_empty(), and printing of the list after inserting values
    print("Front:", myList.front())
    print("Back:", myList.back())
    print("Length:", len(myList))
    print("Is empty?", myList.isEmpty())
    print("List:", myList)

if __name__ == '__main__':
    main()