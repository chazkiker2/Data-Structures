import unittest
# from avl_tree import AVLTree
# from avl_tree import Node
from avl_tree_02 import AvlTree as AVLTree, TreeNode as Node


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_update_height(self):
        self.assertEqual(self.tree.height, -1)
        self.tree.node = Node(5)
        self.tree.update_height()
        self.assertEqual(self.tree.height, 0)

        self.tree.node.left = AVLTree(Node(3))
        self.tree.update_height()
        self.assertEqual(self.tree.node.left.height, 0)
        self.assertEqual(self.tree.height, 1)

        self.tree.node.right = AVLTree(Node(6))
        self.tree.update_height()
        self.assertEqual(self.tree.height, 1)

        self.tree.node.right.node.right = AVLTree(Node(8))
        self.tree.update_height()
        self.assertEqual(self.tree.height, 2)

    def test_left_rotation(self):
        self.tree.node = Node(5)
        self.tree.node.left = AVLTree(Node('row_i'))
        self.tree.node.right = AVLTree(Node(8))
        self.tree.node.right.node.left = AVLTree(Node('c'))
        self.tree.node.right.node.right = AVLTree(Node(9))
        self.tree.node.right.node.right.node.left = AVLTree(Node('col_i'))
        self.tree.node.right.node.right.node.right = AVLTree(Node('z'))

        self.tree.left_rotate()

        self.assertEqual(self.tree.node.key, 8)
        self.assertEqual(self.tree.node.left.node.key, 5)
        self.assertEqual(self.tree.node.right.node.key, 9)
        self.assertEqual(self.tree.node.left.node.left.node.key, 'row_i')
        self.assertEqual(self.tree.node.left.node.right.node.key, 'c')
        self.assertEqual(self.tree.node.right.node.left.node.key, 'col_i')
        self.assertEqual(self.tree.node.right.node.right.node.key, 'z')

    def test_right_rotation(self):
        self.tree.node = Node(5)
        self.tree.node.right = AVLTree(Node('row_i'))
        self.tree.node.left = AVLTree(Node(4))
        self.tree.node.left.node.right = AVLTree(Node('c'))
        self.tree.node.left.node.left = AVLTree(Node(3))
        self.tree.node.left.node.left.node.left = AVLTree(Node('col_i'))
        self.tree.node.left.node.left.node.right = AVLTree(Node('z'))

        self.tree.right_rotate()

        self.assertEqual(self.tree.node.key, 4)
        self.assertEqual(self.tree.node.left.node.key, 3)
        self.assertEqual(self.tree.node.right.node.key, 5)
        self.assertEqual(self.tree.node.left.node.left.node.key, 'col_i')
        self.assertEqual(self.tree.node.left.node.right.node.key, 'z')
        self.assertEqual(self.tree.node.right.node.left.node.key, 'c')
        self.assertEqual(self.tree.node.right.node.right.node.key, 'row_i')

    def test_rebalancing(self):
        self.tree.node = Node(5)
        self.tree.node.right = AVLTree(Node('row_i'))
        self.tree.node.left = AVLTree(Node(3))
        self.tree.node.left.node.right = AVLTree(Node(4))
        self.tree.node.left.node.left = AVLTree(Node('c'))
        self.tree.node.left.node.right.node.left = AVLTree(Node('col_i'))
        self.tree.node.left.node.right.node.right = AVLTree(Node('z'))

        self.tree.rebalance()

        self.assertEqual(self.tree.node.key, 4)
        self.assertEqual(self.tree.node.left.node.key, 3)
        self.assertEqual(self.tree.node.right.node.key, 5)
        self.assertEqual(self.tree.node.left.node.left.node.key, 'c')
        self.assertEqual(self.tree.node.left.node.right.node.key, 'col_i')
        self.assertEqual(self.tree.node.right.node.left.node.key, 'z')
        self.assertEqual(self.tree.node.right.node.right.node.key, 'row_i')

    def test_insertion(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.node.key, 5)

        self.tree.insert(3)
        self.assertEqual(self.tree.node.left.node.key, 3)

        self.tree.insert(6)
        self.assertEqual(self.tree.node.right.node.key, 6)

        self.tree.insert(7)
        self.assertEqual(self.tree.node.right.node.right.node.key, 7)

        self.tree.insert(8)
        self.assertEqual(self.tree.node.right.node.key, 7)
        self.assertEqual(self.tree.node.right.node.left.node.key, 6)
        self.assertEqual(self.tree.node.right.node.right.node.key, 8)


if __name__ == '__main__':
    unittest.main()
