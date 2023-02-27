# General node for any datatype
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None




# Contains crucial methods for navigating and modifying linked lists
class LinkedLists:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_value(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

