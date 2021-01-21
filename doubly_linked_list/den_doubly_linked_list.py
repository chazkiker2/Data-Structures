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
        new_node = ListNode(value)
        new_node.next = self.head

        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        self.head = new_node

    # Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the key of the removed Node.
    def remove_from_head(self):
        if self.head is None:  # if no items in list
            return

        if self.head.next is None:
            self.head = self.tail = None
            self.length = 0
            return

        old_head_val = self.head.key
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1

        return old_head_val

    # Wraps the given key in a ListNode and inserts it
    # as the new tail of the list. Don't forget to handle
    # the old tail node's next pointer accordingly.
    def add_to_tail(self, value):
        new_node = ListNode(value)

        self.length += 1

        if self.head is None:  # if no items in list
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Removes the List's current tail node, making the
    # current tail's previous node the new tail of the List.
    # Returns the key of the removed Node.
    def remove_from_tail(self):
        if self.head is None:
            return  # list is already empty

        self.length -= 1
        old_tail = self.tail  # get current tail

        if self.head.next is None:  # if only one thing in the list
            self.head = self.tail = None
            return old_tail.key

        old_tail.prev = None  # remove pointer to what will be new tail (garbage collection)

        self.tail = self.tail.prev
        self.tail.next = None

        return old_tail.key

    # move given node to front of list (retain order of other nodes)
    def move_to_front(self, node):
        # is node already the head
        if self.head is node:
            return  # node is already at head

        if self.tail is not node:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # input node IS tail, assign it's prev key as new tail

        # first, take input node out — connect surrounding nodes
        node.prev.next = node.next  # assign the previous node's next to current node's next
        self.head.prev = node  # take old head's prev key, point it at input node
        node.next = self.head
        node.prev = None
        self.head = node

        # then, move it to front of list

    # move given node to end of list (retain order of other nodes)
    def move_to_end(self, node):
        if self.tail is node:  # node is already at end!
            return

        if self.head is not node:  # node is not head
            node.prev.next = node.next
        else:
            self.head = node.next  # input node IS head — assign it's next key as new head

        node.next.prev = node.prev
        self.tail.next = node  # current tail's next points at node
        node.prev = self.tail  # new node comes after current tail
        node.next = None  # tail never has next
        self.tail = node  # node is new tail

    def delete(self, node):
        # most important thing — nothing is pointing to node, node is pointing to nothing
        deleted_node_val = node.key

        if self.length == 0:  # if there is nothing to delete
            return

        self.length -= 1

        # edge case 2 — node is head AND node is tail
        if self.length == 1:
            self.head = self.tail = None
            return deleted_node_val

        if node is self.head:
            self.head = node.next  # assign node.next as new head
            self.head.prev = None  # assign newly assigned head's prev pointer to point at None
            node.next = node.prev = None  # garbage collect node's pointers
            return deleted_node_val

        elif node is self.tail:
            self.tail = node.prev  # assign node.prev as new tail
            self.tail.next = None  # assign newly assigned tail's Next pointer to point at None
            node.prev = node.next = None  # garbage collect node's pointers
            return deleted_node_val

        # this assumes node is neither the head nor the tail
        node.prev.next = node.next  # deleting node B from A->B->C — A.next = C,
        node.next.prev = node.prev  # C.prev = A
        node.prev = None
        node.next = None

        return deleted_node_val

    # return the max node in list
    def get_max(self):
        if self.head is None:  # can't compare max of nothing — list does not exist
            return

        current_max_val = self.head.key  # original max val will initialize at the current head
        current_node = self.head.next  # current_node can point to head.next because current_max_val is ALREADY saved

        while current_node is not None:  # while there is a new node to compare
            if current_node.key > current_max_val:  # if val is larger than max, then reassign max
                current_max_val = current_node.key
            current_node = current_node.next  # reassign current_node to the next pointer

        return current_max_val
