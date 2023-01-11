import random as r
from LinkedList import Node, LinkedList

class SingleLinkedList(LinkedList):
    
    def generateList(self, size):
        if self.head is not None:
            print('list already created')
            return
        node = Node(r.randint(1,10))
        self.head = node
        i = 1
        while i < size:
            newNode = Node(r.randint(1,100))
            node.next = newNode
            node = newNode
            i+=1
        self.tail = node
    
    def insertion(self, data, index=-1):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            elif index == -1:
                newNode.next = None
                self.tail.next = newNode
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
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    def deletion(self, index):
        if self.head is None:
            print('Nothing to delete')
            return
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif index == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
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
        
            
        