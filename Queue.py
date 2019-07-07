'''
class Queue:
    def __init__(self):
         # TODO: Initialize the Queue
         self.storage=[]
    def size(self):
         # TODO: Check the size of the Queue
         return len(self.storage)
    def enqueue(self, item):
         # TODO: Enter item into Queue
         self.storage.append(item)
    def dequeue(self):
         # TODO: Remove item from the Queue\
         return self.storage.pop(0)
'''

import Stack
class Queue:
    def __init__(self):
        self.instorage=Stack.Stack()
        self.outstorage=Stack.Stack()
    def size(self):
        return self.instorage.size() +self.outstorage.size()
    def enqueue(self,item):
        self.instorage.push(item)
    def dequeue(self):
        if not self.outstorage.items:
            while self.instorage.items:
                self.outstorage.push(self.instorage.pop())
        return self.outstorage.pop()
