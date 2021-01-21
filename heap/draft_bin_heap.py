# noinspection DuplicatedCode
class BinMinHeap:
    def __init__(self):
        self.heap = [0]
        self.length = 0

    def __len__(self):
        return self.length

    # Easiest and most efficient way to add an element? Append it!
    # Good news about appending: guarantees that we will maintain the complete tree property
    # Bad news: appending will probably violate the heap structure property.
    # Best news: we can write a method that will allow us to regain the heap structure property by
    # comparing the newly added item with its parent! (see `current._sift_up()`)
    def insert(self, item):
        """This is our client-facing method for inserting a node into the tree.

        Add node into heap, fix current.size, then let _sift_up() do the heavy lifting
        to position the new element correctly.
        """

        self.heap.append(item)
        self.length += 1
        self._sift_up(self.length)

    # place the element at given index in its correct position in the tree
    def _sift_up(self, index):
        """This method compares the item at the given index with its parent node and re-adjusts the tree if necessary.

        This method when called during `current.insert()` takes the newly added item and pushes it UP the tree until
        the heap property is successfully preserved in the tree. If the newly added item is very small (in the case
        of a MinHeap), we might have to swap it up several levels — potentially all the way up until it hits the top.
        Here is where our wasted element [0] is important. Notice that we can compute the parent of any node via
        integer division (aka floor division). The index of the current node divided by 2 (then rounded down) is the
        index of the parent node!
        """

        # note: double slash is integer division (or "floor division")
        # divide operands then round result DOWN
        # 5 / 2 = 2.5
        # 5 // 2 = 2
        while index // 2 > 0:  # while the given index has a parent:
            if self.heap[index] < self.heap[index // 2]:  # if current node is less than its parent
                # then swap child with parent
                tmp = self.heap[index // 2]  # make a copy of parent node
                self.heap[index // 2] = self.heap[index]  # assign current node to parent location
                self.heap[index] = tmp  # place the copy of parent node in its child's location (idx.e., index)

            index //= 2  # shorthand for `idx = idx // 2`

    # place the element at given index in its correct position in the tree
    def _sift_down(self, idx):
        """Re-balance the tree by shifting the element at given index down the tree until heap order
        property is preserved.

        This method takes the node at the given index and first looks to see if that node has children. If it does,
        check to see if one child is less than the other.
        """

        while (idx * 2) <= self.length:  # while element has at least one child
            min_child_idx = self.min_child(idx)  # get the index of the smaller child

            # if current element is larger than its own child, switch child with parent
            if self.heap[idx] > self.heap[min_child_idx]:
                # the following three lines swap the element at idx with its smallest child
                # since its child is smaller than itself.
                temp = self.heap[idx]  # make a temp copy of current element
                self.heap[idx] = self.heap[min_child_idx]  # assign the current placement to smaller child
                self.heap[min_child_idx] = temp  # assign temp (current element) to child

            idx = min_child_idx

    # return minimum element in constant time O(1)!
    def get_min(self):
        return self.heap[1]

    # delete the smallest node, then re-balance the tree
    def del_min(self):
        return_val = self.heap[1]  # copy the smallest element
        self.heap[1] = self.heap[self.length]  # set root element to a duplicate of last element
        self.length -= 1  # reduce size (b/c we're deleting an element)
        self.heap.pop()  # remove the original copy of final element (remember we set the root to that element)
        self._sift_down(1)  # take the root element and find its correct position in the tree.
        return return_val  # return the key of the freshly-deleted minimum element

    # given the index of the parent, find the smaller of that parent's two children
    def min_child(self, idx):
        if idx * 2 + 1 > self.length:  # if right child doesn't exist
            return idx * 2  # return left child index

        elif self.heap[idx * 2] < self.heap[idx * 2 + 1]:  # if the left child is smaller than the right child
            return idx * 2  # return left child index

        else:  # right child must exist AND must be smaller than left child
            return idx * 2 + 1  # return right child index

    # given a list, build a new heap accordingly
    def build_heap(self, list_in):
        idx = len(list_in) // 2
        self.length = len(list_in)
        self.heap = [0] + list_in[:]  # make a copy of list in, set current.heap to that copy but start it with a 0
        while idx > 0:
            self._sift_down(idx)
            idx -= 1


# Driver code to test BinMinHeap
bh = BinMinHeap()
bh.build_heap([9, 5, 6, 2, 3])
print(bh.del_min())
for i, el in enumerate(bh.heap):
    print(f"{i}, {el}")

bh.insert(4)
print(f"min {bh.get_min()}")
bh.insert(3)
for i, el in enumerate(bh.heap):
    print(f"{i}, {el}")

print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
