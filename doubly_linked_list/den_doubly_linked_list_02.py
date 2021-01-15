"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given key in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        # increments the length attribute after adding node to list
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the key of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None
        removed = self.head.key
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return removed
        else:
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return removed

    """
    Wraps the given key in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        # check if empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # increase length of list
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the key of the removed Node.
    """

    def remove_from_tail(self):
        # check if empty list
        if self.length == 0:
            return None
        removed = self.tail.key
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return removed

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 0:
            return
        if self.head is node:
            return
        if self.tail is not node:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node
        self.head.prev = None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return
        if self.tail is node:
            return
        if self.head is not node:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # check if list is empty
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            removed = node.key
            if self.head is node:
                self.head = node.next
            elif self.tail is node:
                self.tail = node.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.next = node.prev = None
            self.length -= 1
            return removed

    """
    Finds and returns the maximum key of all the nodes 
    in the List.
    """

    def get_max(self):
        max_value = self.head.key
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            # checks if the key is larger than our max key so far
            if max_value < current_node.key:
                max_value = current_node.key
        return max_value

    """
    Prints the doubly linked list
    """

    def print(self):
        self = self.head
        while self is not None:
            print(self.key)
            self = self.next
