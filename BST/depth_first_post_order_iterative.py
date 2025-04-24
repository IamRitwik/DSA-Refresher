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

    def dft_post_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty!")
        current = previous = self.root
        stack = []
        visited = []
        while current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.value)
                previous = current
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right
        return visited

bst = BinarySearchTree()

bst.insert(20)
bst.insert(10)
bst.insert(25)
bst.insert(7)
bst.insert(18)
bst.insert(24)
bst.insert(32)
bst.insert(2)
bst.insert(9)
bst.insert(15)
bst.insert(21)
bst.insert(28)
bst.insert(41)
bst.insert(37)

print(bst.dft_post_order_iterative())