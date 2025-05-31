class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def display(self):
        temp_node = self.head
        values = []
        while temp_node:
            values.append(str(temp_node.value))
            temp_node = temp_node.next
        print("->".join(values))

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
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
        self._length -= 1
        return temp_node.value

    def pop_right(self):
        if not self._length:
            raise Exception("List is empty!")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value

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
            self.tail = previous_node
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node.value

    def reverse(self):
        if self._length < 2:
            return self
        left_node = None
        middle_node = self.head
        while middle_node is not None:
            right_node = middle_node.next
            middle_node.next = left_node
            left_node = middle_node
            middle_node = right_node
        self.head, self.tail = self.tail, self.head
        return self

    def __iter__(self):
        current = self.head
        while current:
            yield (current.value, current.next)
            current = current.next


my_list = SinglyLinkedList()

my_list.append(5)
my_list.append(2)
my_list.append(9)
my_list.append(12)
my_list.prepend(10)
my_list.prepend(99)

print("####################")

print(dict(my_list))

print("####################")

my_list.display()
print("-------------------")

my_list.reverse()
my_list.display()
print("-------------------")

my_list.reverse()
my_list.display()
print("-------------------")

item = my_list.pop_left()
print("Item removed -> " + str(item))
my_list.display()
print("-------------------")
item = my_list.pop_right()
print("Item removed -> " + str(item))
my_list.display()

item = my_list.remove(2)
print("Item removed -> " + str(item))
print("-------------------")
my_list.display()

item = my_list.remove(10)
print("Item removed -> " + str(item))
print("-------------------")
my_list.display()

item = my_list.remove(9)
print("Item removed -> " + str(item))
print("-------------------")
my_list.display()

