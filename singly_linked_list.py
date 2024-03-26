"""
Singly linked list is a collection of Node, where usually the first Node is the head and initially point to NUll
whenever we add other element, each node gonna point on the data on the next node until the last one which eventually pointed to NUll

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_node_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_node_start(self, data):
        new_head = Node(data)
        if self.is_empty():
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head

    def insert_node(self, data, position):
        self.data = data
        self.position = position
        new_node = Node(data)

        if self.position == 1:
            new_node.next = self.head
            self.head = new_node

        else:
            count = 1
            previous = self.head

            while count < position - 1:
                previous = previous.next
                count += 1

            current = previous.next
            new_node.next = current
            previous.next = new_node
        
    def find_length(self):
        current = self.head
        size = 0

        while current:
            size += 1
            current = current.next
        return size

    def delete_first(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            new_head = self.head.next
            temp.next = None

            while new_head:
                print(new_head.data, end=' -> ')
                new_head = new_head.next
            print('None')
        
           
    def delete_end(self):
        if self.is_empty():
            return None

        elif self.head.next is None:
            self.head = None

        else:
            current = self.head
            previous = None
            while current.next:
                previous = current
                current = current.next
            previous.next = None
        

    def delete_at(self, position):
        self.position = position

        if self.position == 1:
            temp = self.head
            new_head = self.head.next
            temp.next = None

            while new_head:
                print(new_head.data, end=' -> ')
                new_head = new_head.next
            print('None')
        else:
            previous = self.head
            count = 1

            while count < position - 1:
                previous = previous.next
                count += 1
            current = previous.next
            previous.next = current.next
            current.next = None


    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next

        print('None')

singly_linked_list = SinglyLinkedList()
singly_linked_list.add_node_end(10)
singly_linked_list.add_node_end(5)
singly_linked_list.add_node_end(7)
singly_linked_list.add_node_end(3)
singly_linked_list.display()
singly_linked_list.add_node_start(0)
singly_linked_list.insert_node(11, 3)
singly_linked_list.display()

#singly_linked_list.delete_end()
singly_linked_list.delete_first()

#singly_linked_list.delete_at(1)
