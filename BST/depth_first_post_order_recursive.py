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

    def dft_post_order_recursive(self):
        if self.root is None:
            raise Exception("List is empty!")
        visited = []
        def _traverse(node):
            if not node:
                return
            _traverse(node.left)
            _traverse(node.right)
            visited.append(node.value)

        _traverse(self.root)
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

print(bst.dft_post_order_recursive())