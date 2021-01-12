
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.next = self.head
        self.head = new_node

    def remove_head(self):
        if self.head is None:
            # no items in list
            return

        old_head = self.head.value

        if self.head.next is None:
            # only one item in list
            self.tail = None

        # most important part of method below
        self.head = self.head.next
        return old_head

    def remove_tail(self):
        if self.head is None:
            # no items in the list
            return

        old_tail = self.tail.value
        if self.head.next is None:
            # only one item in the list
            self.head = None
            self.tail = None
            return old_tail

        current_node = self.head
        while current_node.next is not self.tail:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node
        return old_tail
