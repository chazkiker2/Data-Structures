class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.heap = [0]
        self.length = 0
        self.comparator = comparator  # defaults to MaxHeap

    def __len__(self):
        return self.length

    def insert(self, value):
        self.heap.append(value)  # add key to heap
        self.length += 1  # increase length (b/c we're inserting)
        self._sift_up(self.length)  # take the freshly appended element and find its correct position in tree

    def delete(self):
        return_val = self.heap[1]  # copy the priority_element
        self.heap[1] = self.heap[self.length]  # assign root to last element
        self.length -= 1  # reduce length (b/c we're deleting)
        self.heap.pop()  # remove last element
        self._sift_down(1)  # take the root element and find its correct position in the tree
        return return_val

    def get_priority(self):
        return self.heap[1]

    def get_size(self):
        return self.length

    def _sift_up(self, index):
        while index // 2 > 0:
            if self.comparator(self.heap[index], self.heap[index // 2]):
                tmp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = tmp
            index //= 2

    def _find_priority_child_index(self, parent_index):
        if parent_index * 2 + 1 > self.length:  # if right_child does not exist
            return parent_index * 2  # return left_child index

        # if left_child is higher priority than right_child
        elif self.comparator(self.heap[parent_index * 2], self.heap[parent_index * 2 + 1]):
            return parent_index * 2  # return left_child index

        else:  # right_child must exist AND must be higher priority than left_child
            return parent_index * 2 + 1

    def _sift_down(self, index):
        while index * 2 <= self.length:
            priority_child_index = self._find_priority_child_index(index)
            if self.comparator(self.heap[priority_child_index], self.heap[index]):
                temp = self.heap[index]
                self.heap[index] = self.heap[priority_child_index]
                self.heap[priority_child_index] = temp

            index = priority_child_index
