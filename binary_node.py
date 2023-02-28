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

    def search_for_node(self, data):
        pass



root = BinaryNode(20)
root.insert_node(15)
root.insert_node(265)
root.insert_node(25)
root.insert_node(22)
root.insert_node(17)