class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._sift_down(0, len(self.storage) - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    # def merge(self, *iterables, key=None, reverse=False):
    #     """Merge multiple sorted inputs into a single sorted output"""
    #
    #     h = []
    #     h_append = h.append
    #
    #     _heapify = heapify

    def heapify(self):
        """Transform list into a heap, in-place, in O(len(x)) time"""
        n = len(self.storage)
        # Transform bottom-up. The largest index there's any point to looking at is
        # the largest with a child index in-range, so must have 2*i + 1 < n,
        # or i
        for i in reversed(range(n // 2)):
            self._sift_up(i)

    def _bubble_up(self, index):
        pass

    # 'heap' is a heap at all indices >= start_pos, except for possibly pos.
    # pos is hte index of a leaf with a possibly out-of-order value.
    # Restore the heap invariant
    def _sift_down(self, start_pos, pos):
        new_item = self.storage[pos]
        # follow the path to the root, moving parents down until finding a place new_item fits
        while pos > start_pos:
            parent_pos = (pos - 1) >> 1
            parent = self.storage[parent_pos]
            if new_item < parent:
                self.storage[pos] = parent
                pos = parent_pos
                continue

            break

        self.storage[pos] = new_item

    def _sift_up(self, pos):
        end_pos = len(self.storage)
        start_pos = pos
        new_item = self.storage[pos]

        # bubble up the smaller child until hitting a leaf
        child_pos = 2 * pos + 1  # leftmost child position
        while child_pos < end_pos:
            # set child_pos to index of smaller child
            right_pos = child_pos + 1
            if right_pos < end_pos and not self.storage[child_pos] < self.storage[right_pos]:
                child_pos = right_pos

            # move the smaller child UP
            self.storage[pos] = self.storage[child_pos]
            pos = child_pos
            child_pos = 2 * pos + 1

        self.storage[pos] = new_item
        self._sift_down(start_pos, pos)
