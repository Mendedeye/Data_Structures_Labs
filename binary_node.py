class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left  = None

    def insert_node(self, data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = BinaryNode(data)
                else: 
                    self.right.insert_node(data)
            elif data < self.data:
                if self.left is None:
                    self.left = BinaryNode(data)
                else: 
                    self.left.insert_node(data)
        else:
            self.data = data

# Searches for a given node and tells the path to the node
    def search_for_node(self, data):
        is_found = "Node Found!"
        not_found = "Node not found."

        if self.data == data:
            return(print(is_found))
        else: 
            if data > self.data:
                print("Right")
                if self.right.data == data:
                    return(print(is_found))
                elif self.right.data == None:
                    return(print(not_found))
                else:
                    self.right.search_for_node(data)
            elif data < self.data:
                print("Left")
                if self.left.data == data:
                    return(print(is_found))
                elif self.left.data == None:
                    return(print(not_found))
                else: 
                    self.left.search_for_node(data)

root = BinaryNode(20)
root.insert_node(15)
root.insert_node(265)
root.insert_node(25)
root.insert_node(22)
root.insert_node(17)
root.search_for_node(22)