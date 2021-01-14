class BinMaxHeap:
    def __init__(self):
        self.heap = [0]
        self.length = 0

    def __len__(self):
        return self.length

    def insert(self, item):
        self.heap.append(item)
        self.length += 1
        self._sift_up(self.length)

    def _sift_up(self, index):
        while index // 2 > 0:  # while given index has a parent
            if self.heap[index] > self.heap[index // 2]:  # if current item > parent item
                tmp = self.heap[index // 2]  # temp = parent item value
                self.heap[index // 2] = self.heap[index]  # assign current item value to parent's location
                self.heap[index] = tmp  # assign parent item value to child/current item's location
            index //= 2  # shorthand for `index = index // 2`

    def max_child(self, idx):
        if idx * 2 + 1 > self.length:  # if index greater than length, right child does not exist
            return idx * 2  # return left_child index
        elif self.heap[idx * 2] > self.heap[idx * 2 + 1]:  # if left_child > right_child
            return idx * 2  # return left_child index
        else:  # right_child must exist and must be greater than left_child
            return idx * 2 + 1

    def get_max(self):
        return self.heap[1]

    def del_max(self):
        return_val = self.heap[1]
        self.heap[1] = self.heap[self.length]
        self.length -= 1
        self.heap.pop()
        self._sift_down(1)
        return return_val

    def _sift_down(self, idx):
        while (idx * 2) <= self.length:  # while child position exists
            max_child_idx = self.max_child(idx)  # get index of larger child
            if self.heap[idx] < self.heap[max_child_idx]:  # if current item is smaller than item's largest child
                tmp = self.heap[idx]  # tmp = current_node
                self.heap[idx] = self.heap[max_child_idx]  # set largest_child to current_location
                self.heap[max_child_idx] = tmp  # set current_node to largest_child's location
            idx = max_child_idx  # new idx = the index of larger child... now repeat

    def build_heap(self, list_in):
        idx = (len(list_in) // 2)
        self.length = len(list_in)
        self.heap = [0] + list_in[:]
        while idx > 0:
            print(f"idx={idx}")
            self._sift_down(idx)
            idx -= 1


# Driver code to test BinMaxHeap
# full feature test file will be written later
bh = BinMaxHeap()
bh.build_heap([9, 5, 6, 2, 3])
print(bh.del_max())
print(f"max={bh.get_max()}")
bh.insert(8)
bh.insert(8)
print(f"max={bh.get_max()}")

print(bh.del_max())
print(f"max={bh.get_max()}")
print(bh.del_max())
print(f"max={bh.get_max()}")
print(bh.del_max())
print(bh.del_max())
