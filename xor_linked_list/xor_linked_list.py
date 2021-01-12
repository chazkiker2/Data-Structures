import ctypes


class Node:
    def __init__(self, value):
        self.value = value
        self.npx = 0


"""
An ordinary Doubly Linked List requires space for two address fields to store the 
addresses of previous and next nodes. A memory-efficient version of Doubly Linked List can 
be created using only one space for the address field with every node. This memory efficient Doubly Linked List 
is called XOR Linked List or Memory Efficient as the list uses the bitwise XOR operator to save space for one address.
In the XOR Linked List, instead of storing actual memory addresses, every node stores the XOR of addresses of previous 
and next nodes.

The XOR Linked List in Python is not of much use because the Python garbage collector doesn't allow 
to save the node whose address is being XORed.

Source: https://www.geeksforgeeks.org/implementation-of-xor-linked-list-in-python/
"""


class XorLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = []

    # method to insert a node at the beginning of the list
    def insert_at_head(self, value):
        node = Node(value)

        if self.head is None:  # list is empty
            self.head = node
            self.tail = node

        else:
            self.head.npx = id(node) ^ self.head.npx
            node.npx = id(self.head)
            self.head = node

        self.__nodes.append(node)

    # method to insert a node at the end of the list
    def insert_at_tail(self, value):
        node = Node(value)

        if self.head is None:  # If list is empty
            self.head = node
            self.tail = node

        else:
            self.head.npx = id(node) ^ self.head.npx
            node.npx = id(self.head)
            self.head = node

        self.__nodes.append(node)

    # method to remove node at beginning
    def delete_at_head(self):
        if self.is_empty():  # if list is empty
            return "List is empty"

        elif self.head == self.tail:  # If list has 1 node
            self.head = self.tail = None

        elif (0 ^ self.head.npx) == id(self.tail):  # If list has 2 nodes
            self.head = self.tail
            self.head.npx = self.tail.npx = 0

        else:  # If list has more than 2 nodes
            res = self.head.value
            x = self.__type_cast(0 ^ self.head.npx)  # Address of next node
            y = (id(self.head) ^ x.npx)  # Address of next of next node (the node following next)
            self.head = x
            self.head.npx = 0 ^ y
            return res

    def delete_at_tail(self):
        if self.is_empty():  # If list is empty
            return "List is empty!"

        elif self.head == self.tail:  # If list has 1 node
            self.head = self.tail = None

        elif self.__type_cast(0 ^ self.head.npx) == self.tail:  # If list has 2 nodes
            self.tail = self.head
            self.head.npx = self.tail.npx = 0

        else:  # If list has more than 2 nodes
            prev_id = 0
            node = self.head
            next_id = 1
            while next_id:
                next_id = prev_id ^ node.npx
                if next_id:
                    prev_id = id(node)
                    node = self.__type_cast(next_id)

            res = node.value
            x = self.__type_cast(prev_id).npx ^ id(node)
            y = self.__type_cast(prev_id)
            y.npx = x ^ 0
            self.tail = y
            return res

    # method to traverse linked list
    def print(self):
        """We are printing values rather than returning it because
        for returning we have to append all values in a list
        and it takes extra memory to save all values in a list."""

        if self.head is not None:
            prev_id = 0
            node = self.head
            next_id = 1
            print(node.value, end=' ')
            while next_id:
                next_id = prev_id ^ node.npx
                if next_id:
                    prev_id = id(node)
                    node = self.__type_cast(next_id)
                    print(node.value, end=' ')
                else:
                    return
        else:
            print("List is empty !")

            # method to traverse linked list in reverse order

    # Print Values in reversed order.
    def reverse_print(self):
        """We are printing values rather than returning it because
        for returning we have to append all values in a list
        and it takes extra memory to save all values in a list."""

        if self.head is not None:
            prev_id = 0
            node = self.tail
            next_id = 1
            print(node.value, end=' ')
            while next_id:
                next_id = prev_id ^ node.npx
                if next_id:
                    prev_id = id(node)
                    node = self.__type_cast(next_id)
                    print(node.value, end=' ')
                else:
                    return
        else:
            print("List is empty !")

            # method to get length of linked list

    def length(self):
        if not self.isEmpty():
            prev_id = 0
            node = self.head
            next_id = 1
            count = 1
            while next_id:
                next_id = prev_id ^ node.npx
                if next_id:
                    prev_id = id(node)
                    node = self.__type_cast(next_id)
                    count += 1
                else:
                    return count
        else:
            return 0

    # method to get node data value by index
    def print_by_index(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.npx

            if next_id:
                prev_id = id(node)
                node = self.__type_cast(next_id)
            else:
                return "Value not found index out of range."
        return node.value

    # method to check if linked list is empty or not
    def is_empty(self):
        if self.head is None:
            return True

        return False

    # method to return a new instance of type
    @staticmethod
    def __type_cast(id_param):
        return ctypes.cast(id_param, ctypes.py_object).value
