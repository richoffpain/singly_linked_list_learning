""" Given a singly linked list with k element
    sort the linked list
    search for  a specific value
    insert node in the sorted singly linked list and still maintening the sort sequence

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

    # agregar elementos a la lista
    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    # sort the list

    def find_mid(self):
        mid = self.head
        current = self.head

        while current.next and current.next.next:
            mid = mid.next
            current = current.next.next
        
        return mid

    def merge_sort(self, head=None):
        if head is None:
            head = self.head
        if head is None or head.next is None:
            return head
        else:
            temp = self.head
            mid = self.find_mid() # <__main__.Node object at 0x0000028E15EA0B10>
            second_half = mid.next
            mid.next = None

            #recursive sorting
            left = self.merge_sort(temp)
            right = self.merge_sort(second_half)

        return self.merge(left, right)

    def merge(self, left, right):
        #first we have to determinate the new head of the singly linked list
        if left.data < right.data:
            self.head = left
            left = left.next
        else:
            self.head = right
            right = right.next
        current = self.head
        while left != None and right != None:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        # add the remaining eleement of the halves list if there is any
        if left != None:
            current.next = left
            #left = left.next
        if right != None:
            current.next = right
            #right = right.next
        return current
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

def main():
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(1)
    linked_list.append(7)
    linked_list.append(0)
    linked_list.append(2)
    linked_list.display()
    print(linked_list.find_mid())
    linked_list.merge_sort()
    linked_list.display()


if __name__ == '__main__':
    main()