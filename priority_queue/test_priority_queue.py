import unittest
from priority_queue import PriorityQueue


class PriorityQueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pq = PriorityQueue()

    def test_len_returns_0_for_empty_queue(self):
        self.assertEqual(len(self.pq), 0)

    def test_len_returns_correct_length_after_enqueue(self):
        self.assertEqual(len(self.pq), 0)
        self.pq.enqueue(2)
        self.assertEqual(len(self.pq), 1)


if __name__ == '__main__':
    unittest.main()
