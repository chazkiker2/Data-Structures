"""
Should have the methods insert, delete, get_max, _bubble_up, and _sift_down.
 - insert
    adds the input key into the heap; this method should ensure that the
    inserted key is in the correct spot in the heap
 - delete
    removes and returns the 'topmost' key from the heap;
    this method needs to ensure that the heap property is maintained after the topmost element has been removed.
 - get_max
    returns the maximum key in the heap in constant time.
 - get_size
    returns the number of elements stored in the heap.
 - _bubble_up
    moves the element at the specified idx "up" the heap by swapping it with its
     parent if the parent's key is less than the key at the specified idx.
 - _sift_down
    grabs the indices of this element's children and determines which child has a larger key.
    If the larger child's key is larger than the parent's key, the child element is swapped with the parent.
"""


class MaxHeap:
    def __init__(self, root=None):
        self.heap = [0] * 10
        # if root is None else [root]

        # if root is not None:
        #     self.heap.append(root)
        self.n = 1 if root is not None else 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def insert(self, value):
        """adds the input key into the heap;
        this method should ensure that the inserted key is in the correct spot in the heap"""
        # self.n += 1
        # n = self.n
        print(f"ln41: n={self.n}")
        self.heap[self.n] = value
        self.swim(self.n)

    def delete(self):
        """removes and returns the 'topmost' key from the heap.
        this method needs to ensure that the heap property is maintained after the topmost element has been removed."""
        current_max = self.heap[1]
        self.exchange(1, self.n-1)
        self.heap[self.n+1] = None
        self.sink(1)
        return current_max

    # def get_max(self):
    #     """returns the maximum key in the heap in constant time"""

    def get_size(self):
        """returns the number of elements stored in the heap"""
        return self.n

    def _bubble_up(self, index):
        """moves the element at the specified idx "up" the heap by swapping it with its parent
        if the parent's key is less than the key at the specified idx"""
        pass

    def _sift_down(self, index):
        """grabs the indices of this element's children and determines which child has a larger key.
        If the larger child's key is larger than the parent's key, the child element is swapped with the parent
        """
        pass

    def exchange(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t

    def swim(self, k):
        while k > 1 and self.less(k / 2, k):
            self.exchange(k / 2, k)
            k = k / 2

    def sink(self, k):
        while 2 * k <= self.n:
            j = 2 * k
            if j < self.n and self.less(j, j + 1):
                j += 1

            self.exchange(k, j)
            k = j

    def less(self, i, j):
        return self.heap[i] < self.heap[j]


# Driver code to test
mh = MaxHeap()
print(mh.get_size())
mh.insert(2)
print(mh.get_size())
print(mh.is_empty())
mh.insert(9)
mh.insert(6)
print(mh.get_size())
mh.delete()
print(mh.get_size())
