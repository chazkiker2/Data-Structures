"""
Source: https://www.geeksforgeeks.org/binary-heap/

A Binary Heap is a Binary Tree with the following properties:
 - It's a complete tree. All levels are completely filled except possibly the last level and the last level has all keys
 as far left as possible. This property of Binary Heap makes them  suitable to be stored in an array!
 - A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among
 all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree.
 Max Binary Heap is similar to MinHeap.
"""
from heapq import heappush, heappop, heapify


class MinHeap:
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i-1) / 2)

    def insert_key(self, k):
        heappush(self.heap, k)

    def decrease_key(self, i, new_val):
        i = int(i)
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extract_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    # get the minimum element from the heap
    def get_min(self):
        return self.heap[0]


# # Driver program to test above function
# heapObj = MinHeap()
# heapObj.insert_key(3)
# heapObj.insert_key(2)
# heapObj.delete_key(1)
# heapObj.insert_key(15)
# heapObj.insert_key(5)
# heapObj.insert_key(4)
# heapObj.insert_key(45)
#
# print(heapObj.extract_min())
# print(heapObj.get_min())
# heapObj.decrease_key(2, 1)
# print(heapObj.get_min())
