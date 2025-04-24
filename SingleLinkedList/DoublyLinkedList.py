class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def display(self):
        temp_node = self.head
        values = []
        while temp_node is not None:
            values.append(str(temp_node.value))
            temp_node = temp_node.next
        print("->".join(values))

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("List is empty!")
        temp_node = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = temp_node.next
            temp_node.next = None
            self.head.previous = None
        self._length -= 1
        return temp_node.value

    def pop_right(self):
        if not self._length:
            raise Exception("List is empty!")
        temp_node = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = temp_node.previous
            temp_node.previous = None
            self.tail.next = None
        self._length -= 1
        return temp_node.value

    def remove(self, value):
        if not self._length:
            raise Exception("List is empty!")
        if self.head.value == value:
            print("Head")
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("Item not found in list!")
        if current_node.next is None:
            print("Tail")
            return self.pop_right()
        current_node.next.previous = previous_node
        previous_node.next = current_node.next
        current_node.next = None
        current_node.previous = None
        self._length -= 1
        return current_node.value

d_list = DoublyLinkedList()

d_list.append(5)
d_list.append(2)
d_list.append(9)
d_list.append(12)
d_list.prepend(10)
d_list.prepend(99)

d_list.display()
print("-------------------")

item = d_list.pop_left()
print("Item removed = " + str(item) )

d_list.display()
print("-------------------")

item = d_list.pop_right()
print("Item removed = " + str(item) )

d_list.display()
print("-------------------")

item = d_list.remove(2)
print("Item removed = " + str(item) )

d_list.display()
print("-------------------")

item = d_list.remove(10)
print("Item removed = " + str(item) )

d_list.display()
print("-------------------")

item = d_list.remove(9)
print("Item removed = " + str(item) )

d_list.display()
print("-------------------")