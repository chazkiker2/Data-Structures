"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


class DoublyLinkedList:
    """ Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Wraps the given key in a ListNode and inserts it
    # as the new head of the list.
    # Don't forget to handle the old head node's previous pointer accordingly.
    def add_to_head(self, value):
        """add a node to the beginning of the list
        """

        self.length += 1
        new_node = ListNode(value)

        if self.head is None:  # If list is empty
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the key of the removed Node.
    def remove_from_head(self):
        """Remove the first element in the list
        """

        self.length -= 1
        if self.head is None:  # If no items in list
            return

        old_head_val = self.head.key

        if self.head.next is None:  # If only one item in list
            self.head = self.tail = None
        else:
            self.head = self.head.next  # current head's next ref is the new head

        return old_head_val

    # Wraps the given key in a ListNode and inserts it
    # as the new tail of the list. Don't forget to handle
    # the old tail node's next pointer accordingly.
    def add_to_tail(self, value):
        """Add a node to the end of the list
        """

        self.length += 1
        new_node = ListNode(value)
        new_node.next = None  # tail is last therefore never has next

        if self.head is None:  # If list is empty
            # new node is only element, it will be head & tail
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            return

        # last = current.head
        #
        # while last.next is not None:
        #     last = last.next
        #
        # last.next = new_node

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Removes the List's current tail node, making the
    # current tail's previous node the new tail of the List.
    # Returns the key of the removed Node.
    def remove_from_tail(self):
        """Remove the item at the end of the list
        """
        if self.head is None:  # If no items in list
            return

        self.length -= 1
        old_tail_val = self.tail.key
        if self.head.next is None:  # If only one item in list
            self.tail = self.head = None
            return old_tail_val

        before_last = self.tail.prev
        before_last.next = None
        self.tail = before_last

        return old_tail_val

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""

        if node is self.head:
            return
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
            return

        # first, take node out of place
        prev_ref = node.prev
        next_ref = node.next
        prev_ref.next = next_ref
        next_ref.prev = prev_ref

        # then, place node in front
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""

        # if node is current.tail and node is current.head:
        #     # print("node is already head and tail — it's at the end")
        #     return
        if node is self.tail:
            # print("node is already the tail — it's at the end!")
            return
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            return

        # first, take node out of place
        prev_ref = node.prev
        next_ref = node.next
        prev_ref.next = next_ref
        next_ref.prev = prev_ref

        # then, place node at end
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def delete(self, node):
        """Deletes the input node from the List, preserving the
        order of the other elements of the List."""
        self.length -= 1

        if node is self.head and node is self.tail:
            # print("node is head and tail!")
            self.head = self.tail = None
            self.length = 0
            return node.key

        elif node is self.head:
            # print("current.head is input node")
            self.head = self.head.next
            self.head.prev = None
            return node.key

        elif node is self.tail:
            # print("current.tail is input node")
            self.tail = self.tail.prev
            self.tail.next = None
            return node.key

        else:
            prev_ref = node.prev
            next_ref = node.next
            prev_ref.next = next_ref
            next_ref.prev = prev_ref
            return node.key

    def get_max(self):
        """Finds and returns the maximum key of all the nodes
        in the List."""

        # initialize temp and max to point at head
        if self.head is None:
            return None

        max_node = temp = self.head

        while temp is not None:
            if temp.key > max_node.key:
                max_node = temp

            temp = temp.next

        return max_node.key
