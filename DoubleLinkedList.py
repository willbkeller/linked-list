import random as r
from LinkedList import Node, LinkedList

class DNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
    

class DoubleLinkedList(LinkedList):
    
    def generateList(self, size):
        if self.head is not None:
            print('List already Created')
        else:
            node = DNode(r.randint(1,100))
            self.head = node
            print(self.head.prev)
            i = 1
            while i < size:
                newNode = DNode(r.randint(1,100))
                node.next = newNode
                newNode.prev = node
                node = newNode
                i+=1
            self.tail = node
    
    def insertion(self, data, index=-1):
        newNode = DNode(data)
        if self.head is None:
            print('created')
            self.head = newNode
            self.tail = newNode
        else:
            if index == 0:
                newNode.next = self.head
                newNode.next.prev = newNode
                self.head = newNode
            elif index == -1:
                newNode.next = None
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                tempNode = self.head
                i = 0
                while i < index - 1:
                    tempNode = tempNode.next
                    i += 1
                    if tempNode == None:
                        print(f'{index} out of bounds')
                        return
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.prev = tempNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode   

    def reverseTraversal(self):
        if self.head is None:
            print('List DNE')
        else:
            node = self.tail
            while node is not None:
                print(node.data, end=' ')
                node = node.prev
            print()
    
    def deletion(self, index):
        if self.head is None:
            print('Nothing to delete')
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
            elif index == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.tail.prev
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                i = 0
                while i < index-1:
                    tempNode = tempNode.next
                    i+=1
                nextNode = tempNode.next 
                tempNode.next = nextNode.next
                nextNode.next.prev = tempNode
                    
