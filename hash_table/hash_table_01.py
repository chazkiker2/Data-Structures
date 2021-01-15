class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        # in a fully-featured hash_table will have prime cap and it will be alterable
        # but for the sake of simplicity, we'll implement separate chaining hash table
        # that will set capacity once and never change it. good for simplicity, bad for scalability
        self.capacity = 50  # maximum number of storable units
        self.size = 0  # number of elements stored
        self.buckets = [None] * self.capacity

    def hash(self, key) -> int:
        hash_sum = 0

        # for each character in key
        for idx, c in enumerate(key):

            # Add (index + length of key) ^ (current char code)
            hash_sum += (idx + len(key)) ** ord(c)

            # perform modulus to keep hash_sum in range [0, self.capacity - 1]
            hash_sum = hash_sum % self.capacity

        return hash_sum

    def insert(self, key, value):
        # 1. increment size
        self.size += 1

        # go to the node corresponding to the hash
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            return

        # 4. Collision! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next

        # Add a new node at the end of the list with provided key/key
        prev.next = Node(key, value)
