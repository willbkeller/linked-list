class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def traverseList(self):
        if self.head is None:
            print('List DNE')
            return
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next
        print()
            
    def search(self, nodeValue):
        if self.head is None:
            print('List Empty')
            return
        node = self.head
        i = 0
        lst=[]
        while node is not None:
            if node.data == nodeValue:
                lst.append(i)
            node = node.next
            i+=1
        if len(lst) != 0:
            print(f'{nodeValue} found at: ', end='')
            for i in lst[:-1]:
                print(i, end=', ')
            print(lst[-1])
            return
        else:
            print('Node DNE')
            return
    
            
