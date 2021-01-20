import unittest
# from avl_tree import AVLTree
# from avl_tree import Node
from avl_tree_02 import AvlTree


class AvlTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = AvlTree()

    # def test_update_height(current):
        # current.assertEqual(current.tree.height, -1)
        # current.tree.node = Node(5)
        # current.tree.update_height()
        # current.assertEqual(current.tree.height, 0)

        # current.tree.node.left = AVLTree(Node(3))
        # current.tree.update_height()
        # current.assertEqual(current.tree.node.left.height, 0)
        # current.assertEqual(current.tree.height, 1)
        #
        # current.tree.node.right = AVLTree(Node(6))
        # current.tree.update_height()
        # current.assertEqual(current.tree.height, 1)
        #
        # current.tree.node.right.node.right = AVLTree(Node(8))
        # current.tree.update_height()
        # current.assertEqual(current.tree.height, 2)

    # def test_left_rotation(current):
    #     current.tree.node = Node(5)
    #     current.tree.node.left = AVLTree(Node('x'))
    #     current.tree.node.right = AVLTree(Node(8))
    #     current.tree.node.right.node.left = AVLTree(Node('c'))
    #     current.tree.node.right.node.right = AVLTree(Node(9))
    #     current.tree.node.right.node.right.node.left = AVLTree(Node('y'))
    #     current.tree.node.right.node.right.node.right = AVLTree(Node('z'))
    #
    #     current.tree.left_rotate()
    #
    #     current.assertEqual(current.tree.node.key, 8)
    #     current.assertEqual(current.tree.node.left.node.key, 5)
    #     current.assertEqual(current.tree.node.right.node.key, 9)
    #     current.assertEqual(current.tree.node.left.node.left.node.key, 'x')
    #     current.assertEqual(current.tree.node.left.node.right.node.key, 'c')
    #     current.assertEqual(current.tree.node.right.node.left.node.key, 'y')
    #     current.assertEqual(current.tree.node.right.node.right.node.key, 'z')

    # def test_right_rotation(current):
    #     current.tree.node = Node(5)
    #     current.tree.node.right = AVLTree(Node('x'))
    #     current.tree.node.left = AVLTree(Node(4))
    #     current.tree.node.left.node.right = AVLTree(Node('c'))
    #     current.tree.node.left.node.left = AVLTree(Node(3))
    #     current.tree.node.left.node.left.node.left = AVLTree(Node('y'))
    #     current.tree.node.left.node.left.node.right = AVLTree(Node('z'))
    #
    #     current.tree.right_rotate()
    #
    #     current.assertEqual(current.tree.node.key, 4)
    #     current.assertEqual(current.tree.node.left.node.key, 3)
    #     current.assertEqual(current.tree.node.right.node.key, 5)
    #     current.assertEqual(current.tree.node.left.node.left.node.key, 'y')
    #     current.assertEqual(current.tree.node.left.node.right.node.key, 'z')
    #     current.assertEqual(current.tree.node.right.node.left.node.key, 'c')
    #     current.assertEqual(current.tree.node.right.node.right.node.key, 'x')
    #
    # def test_rebalancing(current):
    #     current.tree.node = Node(5)
    #     current.tree.node.right = AVLTree(Node('x'))
    #     current.tree.node.left = AVLTree(Node(3))
    #     current.tree.node.left.node.right = AVLTree(Node(4))
    #     current.tree.node.left.node.left = AVLTree(Node('c'))
    #     current.tree.node.left.node.right.node.left = AVLTree(Node('y'))
    #     current.tree.node.left.node.right.node.right = AVLTree(Node('z'))
    #
    #     current.tree.rebalance()
    #
    #     current.assertEqual(current.tree.node.key, 4)
    #     current.assertEqual(current.tree.node.left.node.key, 3)
    #     current.assertEqual(current.tree.node.right.node.key, 5)
    #     current.assertEqual(current.tree.node.left.node.left.node.key, 'c')
    #     current.assertEqual(current.tree.node.left.node.right.node.key, 'y')
    #     current.assertEqual(current.tree.node.right.node.left.node.key, 'z')
    #     current.assertEqual(current.tree.node.right.node.right.node.key, 'x')

    # def test_insertion(current):
    #     current.tree.insert(5)
    #     # current.assertEqual(current.tree.root, 5)
    #     nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    #
    #     for num in nums:
    #         root = current.tree.insert(root, num)
    #
    #     # pre-order traversal
    #     print("Preorder Traversal after insertion - ")
    #     current.tree.pre_order(root)
    #     print()


if __name__ == '__main__':
    unittest.main()
