import SingleLinkedList as SLL

sll = SLL.SingleLinkedList()

if __name__ == '__main__':
    start = int(input('1. Generate Random List\n2. Create Own List\n> '))
    size = int(input('Size of list\n> '))
    if start == 1:
        print(f'Generating Random List of {size} elements')
        sll.generateList(size)
    else:
        for i in range(size):
            element = int(input(f'Element {i+1}: '))
            sll.insertion(element)
            
    while True:
        sll.traverseList()
        print('Options:\n  1. Instert Element\n  2. Delete Element\n  3. Search Value\n  0. Exit')
        choice = int(input('> '))
        if choice == 1:
            values = input('Enter element and index [e i]\n> ')
            e, i = values.split()
            sll.insertion(int(e), int(i))
        elif choice == 2:
            index = int(input(f'Enter index to delete [0-{size-1}]\n> '))
            sll.deletion(index)
            size-=1
        elif choice == 3:
            element = int(input('Enter value to search\n> '))
            sll.search(element)
        else: break    