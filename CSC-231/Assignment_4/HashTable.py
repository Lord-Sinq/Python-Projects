'''
Name: Sinclair DeYoung
Date: jun 12, 2023
Description: This lab is focused on hash tables.
'''
from LinkedList import LinkedList
class HashTableChaining:
    def __init__(self, size=53):
        '''
        Construtor
        '''
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(LinkedList())
    def __hash(self, value):
        '''
        Hashing Function
        '''
        return value % len(self.__buckets)
    def insert(self, value):
        '''
        Insert Function
        '''
        bucketNum = self.__hash(value)
        self.__buckets[bucketNum].append(0, value)
    def find(self, value):
        '''
        Find Function
        '''
        bucketNum = self.__hash(value)
        result = self.__buckets[bucketNum].find(value)
        return result
    def __str__(self):
        '''
        String Function
        '''
        result = ""
        for i in range(len(self.__buckets)):
            # put the bucket number in front of each value
            result += "bucket " + str(i) + ": " + str(len(self.__buckets[i])) +": "
            result += str(self.__buckets[i]) + "\n"
        return result
class HashTableProbing:
    '''
    Create a Hashing Table using Linear Probing for Collision Resolution
    '''
    def __init__(self, size=53):
        '''
        Constructor
        should be a prime number
        '''
        self.__buckets = [None] * size
        self.__skip = 3
    def __hash(self, value):
        '''
        Hash Function
        '''
        return value % len(self.__buckets)
    def __rehash(self, bucketNum):
        '''
        ReHash Function
        '''
        return (bucketNum + self.__skip) % len(self.__buckets)
    def insert(self, value):
        '''
        Insert the value into the hash table
        '''
        # hash tthe value to get the bucket number
        bucketNum = self.__hash(value)
        # keep the original bucket number
        originalBucketNum = bucketNum
        # rehash outside the while loop
        if (self.__buckets[bucketNum] is not None):
            bucketNum = self.__rehash(bucketNum)
        # keep rehashing till we find an empty bucket
        while (self.__buckets[bucketNum] is not None and \
                bucketNum != originalBucketNum):
            bucketNum = self.__rehash(bucketNum)
        # if we found an empty bucket or raise an error
        if (self.__buckets[bucketNum] is None):
            self.__buckets[bucketNum] = value
        else:
            raise Exception('Table Full')
    def find(self, value):
        '''
        Find a value in the table
        '''
        # hash the value to get the bucket number
        bucketNum = self.__hash(value)
        # keep the original bucket number
        originalBucketNum = bucketNum
        # rehash outside the while loop
        if (self.__buckets[bucketNum] is not None and self.__buckets[bucketNum]):
            return self.__buckets[bucketNum]
        else:
            bucketNum = self.__rehash(bucketNum)
        # keep rehashing until we either find the value of find an empy bucket
        while (self.__buckets[bucketNum] is not None and \
                self.__buckets[bucketNum] != value and \
                bucketNum != originalBucketNum):
            bucketNum = self.__rehash(bucketNum)
        # if we found the value or we have gone all the way around
        if (self.__buckets[bucketNum] is not None and self.__buckets[bucketNum]):
            return self.__buckets[bucketNum]
        else:
            return None
    def __str__(self):
        '''
        Create a string
        '''
        result = ""
        for i in range(len(self.__buckets)):
            # put the bucket number in front of each value
            result += "bucket " + str(i) + ": " + str(self.__buckets[i]) + "\n"
        return result
def main():
    # testing HashTableChaining
    print('Testing HashTableChaining:')
    HTC = HashTableChaining()
    import random
    for i in range(0, 80):
        ran = random.randint(0, 100)
        HTC.insert(ran)
    # Output
    print(HTC,)
    # find values
    print('Find value 24:', HTC.find(24))
    print('Find value 53:', HTC.find(53),'\n')
    # Testing HashTableProbing
    HTP = HashTableProbing()
    value = (10,20,30,40,50,12,23,3,60,58,11,2,88,22,55,64,38,16,67,49)
    for i in value:
        HTP.insert(i)
    # Output
    print(HTP)
    # find values
    print('Find value 30:', HTP.find(30))
    print('Find value 50:', HTP.find(50))

if __name__ == '__main__':
    main()