from typing import List


class AvlTreeNode:
    def __init__(self, key, val=None, balance_factor=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # track parent for easier rotations
        self.balance_factor = balance_factor  # balance factor of current node
        self.height = 1


class AvlTree:
    def __init__(self):
        self.root = None  # root node
        self.n = 0  # node count

    def insert(self, key, val=None):
        self.root = self._insert(self.root, key, val)  # returns root of resulting tree after insertion
        self.n += 1

    def _insert(self, root: AvlTreeNode, key, val=None) -> AvlTreeNode:
        if not root:
            return AvlTreeNode(key, val, balance_factor=0)
        if key < root.key:
            left_sub_root = self._insert(root.left, key, val)  # insert and update left subroot
            root.left = left_sub_root
            left_sub_root.parent = root
        elif key > root.key:
            right_sub_root = self._insert(root.right, key, val)  # insert and update right subroot
            root.right = right_sub_root
            right_sub_root.parent = root
        else:
            return root  # no duplicate keys allowed; no insertion, return current root as is
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.balance_factor = self._get_height(root.left) - self._get_height(root.right)
        return self.rebalance(root)  # Re-balance current root (if required)

    def rebalance(self, root: AvlTreeNode) -> AvlTreeNode:
        if root.balance_factor == 2:
            if root.left.balance_factor < 0:  # L-R
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            else:  # L-L
                return self.rotate_right(root)
        elif root.balance_factor == -2:
            if root.right.balance_factor > 0:  # R-L
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
            else:  # R-R
                return self.rotate_left(root)
        else:
            return root  # no need to re-balance

    def rotate_left(self, root: AvlTreeNode) -> AvlTreeNode:
        pivot = root.right
        tmp = pivot.left

        # Re-assign pivot's left child to root and update parent pointers
        pivot.left, pivot.parent, root.parent = root, root.parent, pivot

        # 2. use saved left child of pi
        root.right = tmp
        if tmp:  # tmp could be None
            tmp.parent = root

        if pivot.parent:
            if pivot.parent.left == root:  # if the parent's left subtree is the none to be updated
                pivot.parent.left = pivot  # assign the pivot as the new child
            else:
                pivot.parent.right = pivot  # assign the pivot as new child
        # update heights and balance_factors using tracked heights
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.balance_factor = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.balance_factor = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot

    def rotate_right(self, root: AvlTreeNode) -> AvlTreeNode:
        pivot = root.left
        tmp = pivot.right

        # 1. Re-assign pivot's right child to root and update parent pointers
        pivot.right, pivot.parent, root.parent = root, root.parent, pivot

        # 2. use saved right child of pivot and assign it to root's left and update its parent
        root.left = tmp
        if tmp:  # tmp can be None, only assign parent if it's not None
            tmp.parent = root

        # update pivot's parent (manually check which one matches the root that was passed)
        if pivot.parent:
            if pivot.parent.left == root:  # if the parent's left subtree is the one to update
                pivot.parent.left = pivot  # assign the pivot as the new child
            else:
                pivot.parent.right = pivot  # vice-versa for right child

        # update heights and balance_factors using tracked heights
        root.height = max(self._get_height(root.left), self._get_height(pivot.right)) + 1
        root.balance_factor = self._get_height(root.left) - self._get_height(root.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.balance_factor = self._get_height(pivot.left) - self._get_height(pivot.right)
        return pivot  # return root of new tree

    def _get_height(self, root: AvlTreeNode) -> int:
        if not root:  # empty tree means height of 0
            return 0
        else:
            return root.height  # return instance var height

    @staticmethod
    def burst_insert(a: List):
        """
        Inserts a list of n items into an AVL Tree and returns the root
        :param a: list of items
        :Time: O(n*log(n))
        :Space: O(n)
        :return: tree root
        """
        root = AvlTree()
        for item in a:
            root.insert(item)
        return root
