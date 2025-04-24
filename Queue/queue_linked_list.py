class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if not self._size:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self

    def dequeue(self):
        if not self._size:
            raise Exception("Queue is empty!")
        temp_node = self.head
        if self._size == 1:
            self.head = self.tail = None
        else:
            self.head = temp_node.next
            temp_node.next = None
        self._size -= 1
        return temp_node.value

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def peek(self):
        return self.head.value if self.head else None


queue = Queue()
print(queue.peek())
print(queue.get_size())

queue.enqueue("C")
queue.enqueue("Python")
queue.enqueue("Java")
queue.enqueue("Go")
queue.enqueue("Rust")

print(queue.peek())
print(queue.get_size())

queue.dequeue()
queue.dequeue()

print(queue.peek())
print(queue.get_size())
