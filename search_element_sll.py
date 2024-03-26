class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next

        print('Noonne')

    def search_key(self, key):
        self.key = key
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        current = self.head
        previous =  None
        siguiente = None

        while current:
            siguiente = current.next
            current.next = previous
            previous = current
            current = siguiente
        while previous:
            print(previous.data, end= ' -> ')
            previous = previous.next
        print('None')

    def find_mid_node(self):
        mid = self.head
        current = self.head
        #Finding the length of the singly linked list to see if its an even number or odd
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next 

        if count % 2 == 0:
            while current and current.next and current.next.next:
                mid = mid.next
                current = current.next.next
            return mid.data

        else:
            while current and current.next:
                mid = mid.next
                current = current.next.next

            return mid.data

       
        

    def find_node_at(self, position):
        self.position = position

        if self.is_empty():
            return None
        else:
            temp = self.head
            count = 1

            while count < position:
                temp = temp.next
                count += 1

            return temp.data
    
    def find_node_from_end(self, position):
        self.position = position
        count = 1
        result = self.head
        current = self.head

        while count < position:
            current = current.next
            count += 1
        while current.next:
            current = current.next
            result = result.next
        return result.data




def main():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(17)
    sll.append(3)
    sll.append(0)
    sll.append(2)
    sll.append(1)
    sll.display()
    print(sll.find_mid_node())
    print(sll.find_node_at(2))
    print(sll.search_key(3))
    print(sll.find_node_from_end(3))
    sll.reverse()
    
    #sll.display()
    
    


if __name__ == '__main__':
    main()