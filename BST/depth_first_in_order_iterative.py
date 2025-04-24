class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self

    def dft_in_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty!")
        current_node = self.root
        stack = []
        visited = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node.value)
                if not visited_node.right:
                    continue
                current_node = visited_node.right
        return visited


bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(15)
bst.insert(25)
bst.insert(31)
bst.insert(22)
bst.insert(5)
bst.insert(8)
bst.insert(3)

print(bst.dft_in_order_iterative())