from collections import deque

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

    def breadth_first_traversal(self):
        if self.root is None:
            raise Exception("List is empty!")
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.value)
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return visited

    def breadth_first_traversal_2(self):
        if self.root is None:
            raise Exception("List is empty!")
        queue = deque()
        queue.append(self.root)
        visited = []
        while queue:
            visited_node = queue.popleft()
            visited.append(visited_node.value)
            if visited_node.right:
                queue.append(visited_node.right)
            if visited_node.left:
                queue.append(visited_node.left)
        return visited




bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(15)
bst.insert(25)
bst.insert(31)
bst.insert(22)
bst.insert(5)
bst.insert(3)
bst.insert(8)

print(bst.breadth_first_traversal())

print(bst.breadth_first_traversal_2())