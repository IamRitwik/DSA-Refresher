class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_size = 10

    def push(self, value):
        new_element = Node(value)
        if self._max_allowed_size == self._size:
            raise Exception("Stack size exceeded")
        if not self._size:
            self._top = new_element
        else:
            new_element.next = self._top
            self._top = new_element
        self._size += 1
        return self

    def pop(self):
        if not self._size:
            raise Exception("List is empty")
        former_top = self._top
        if self._size == 1:
            self._top = None
        else:
            self._top = former_top.next
            former_top.next = None
        self._size -= 1
        return self

    def peek(self):
        return self._top.value if self._top else None

    def clear(self):
        self._top = None
        self._size = 0
        return self

    def get_size(self):
        return self._size


stack = Stack()

print(stack.peek())
print(stack.get_size())

stack.push("C")
stack.push("Python")
stack.push("Java")
stack.push("Go")
stack.push("Rust")

print(stack.peek())
print(stack.get_size())

stack.pop()
stack.pop()

print(stack.peek())
print(stack.get_size())