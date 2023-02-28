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
# Adds a new node to the linked list
    def append_node(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

# Searches for a data point in a node in a linked list and returns true or false depending if the node is present
    def find_node(self, data_to_find):
        current = self.head

        while current is not None:
            if current.data is data_to_find:
                return True
            
            current = current.next
        
        return False