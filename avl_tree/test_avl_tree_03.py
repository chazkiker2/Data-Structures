import unittest
from avl_tree_03 import AvlTree


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.avl_tree = AvlTree

    @staticmethod
    def validate_bst(root_in) -> bool:
        def validate(root, current_min, current_max):
            if not root:
                return True
            if current_min < root.key < current_max:
                # recur left and right and update intervals accordingly
                return validate(root.left, current_min, root.key) and validate(root.right, root.key, current_max)
            else:
                return False  # not valid

        return validate(root_in, float("-inf"), float("inf"))

    def test_left_left(self):
        ll = [24, 20, 26, 15, 22]
        self.avl_tree = AvlTree.burst_insert(ll)
        assert self.validate_bst(self.avl_tree.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)
        self.avl_tree.insert(14)
        assert self.validate_bst(self.avl_tree.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)

        ll = [13, 10, 15, 5, 11, 16, 4, 8]
        t1 = AvlTree.burst_insert(ll)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)
        t1.insert(3)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)

        print('PASSED LEFT-LEFT')

    def test_right_right(self):
        rr = [23, 20, 26, 25, 28, 24, 34]
        t1 = AvlTree.burst_insert(rr)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)

        rr = [20, 10, 30, 8, 25, 40, 50]
        t1 = AvlTree.burst_insert(rr)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)
        t1.insert(60)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)

        print('PASSED RIGHT-RIGHT')

    def test_left_right(self):
        lr = [24, 20, 26, 14, 22]
        t1 = AvlTree.burst_insert(lr)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)
        t1.insert(21)
        # pretty_print_tree(avl_tree.root)
        assert self.validate_bst(t1.root), 'ERROR!'

        print('PASSED LEFT-RIGHT')

    def test_right_left(self):
        rl = [23, 20, 26, 25, 28]
        t1 = AvlTree.burst_insert(rl)
        assert self.validate_bst(t1.root), 'ERROR!'
        # pretty_print_tree(avl_tree.root)
        t1.insert(24)
        # pretty_print_tree(avl_tree.root)
        assert self.validate_bst(t1.root), 'ERROR!'

        print('PASSED LEFT-RIGHT')

    # def test_correctness(self):
    #     # CORRECTNESS TEST
    #     # try:
    #     self.test_left_left()
    #     self.test_right_right()
    #     self.test_left_right()
    #     self.test_right_left()
    #     print('> PASSED CORRECTNESS TEST')
    #     # except:
    #     #     print('ERROR!')


if __name__ == '__main__':
    unittest.main()
