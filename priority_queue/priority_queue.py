from heap.draft_binary_heap import MinHeap


class PriorityQueue:
    def __init__(self):
        self.size = 0
        self.storage = MinHeap()

    def __len__(self):
        return self.size

    def enqueue(self, item):
        self.size += 1
        self.storage.insert_key(item)

    def dequeue(self):
        if self.size == 0:  # If test_queue is empty
            return

        self.size -= 1
        return self.storage.extract_min()
