"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


"""
A tree class to keep track of things like the
balance factor and the re-balancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0  # refers to left vs right balance — determines next node direction

    """
    Display the whole tree. Uses recursive def.
    """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node is not None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 1, '<')
            if self.node.right is not None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """

    def update_height(self, recursive=True):
        # recursive param acts as flag for whether we should recurse — defaults to true

        if self.node:  # if node exists
            if recursive:
                if self.node.left:
                    self.node.left.update_height()  # recurse

                if self.node.right:
                    self.node.right.update_height()  # recurse

            # update height of AVL tree by comparing height of left and right node
            self.height = 1 + max(self.node.left.height, self.node.right.height)
            # note max() takes the maximum of params

        else:  # self.node does not exist
            self.height = -1  # set to -1 for 0 index (next node added will take height to 0)

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balance()  # potentially an error

                if self.node.right:
                    self.node.right.update_balance()  # potentially an error

            self.balance = self.node.left.height - self.node.right.height

        else:  # self.node does not exist
            self.balance = 0  # set to 0 b/c node does not exist

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """

    def left_rotate(self):
        if not self.node:
            return

        # please change — circle back
        new_root = self.node.right.node
        new_left = new_root.left.node
        old_root = self.node
        self.node = new_root
        old_root.right = new_left
        new_root.left.node = old_root

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """

    def right_rotate(self):
        if not self.node:
            return

        new_root = self.node.left.node
        new_right = new_root.right.node
        old_root = self.node
        self.node = new_root
        old_root.left = new_right
        new_root.right.node = old_root

    """
    Sets in motion the re-balancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """

    def rebalance(self):
        self.update_height(recursive=False)
        self.update_balance(recursive=False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:  # if left subtree is larger than right subtree
                if self.node.left.balance > 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                    self.right_rotate()
                    self.update_height()
                    self.update_balance()
            if self.balance < -1:  # if right subtree is larger than left subtree
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                    self.left_rotate()
                    self.update_height()
                    self.update_balance()

    """
    Uses the same insertion logic as a binary search tree
    after the key is inserted, we need to check to see
    if we need to re-balance
    """

    def insert(self, key):
        new_node = Node(key)
        if not self.node:  # if there is not any node in tree
            # create two empty subtrees on either side of the tree
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:  # if there is a node and it exists, and the key passed in is less than current key
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)

        self.rebalance()


# driver code to test
tree = AVLTree()
# assertEqual(self.tree.height, -1)
tree.node = Node(5)
tree.update_height()
# assertEqual(self.tree.height, 0)

tree.node.left = AVLTree(Node(3))
tree.update_height()
# assertEqual(self.tree.node.left.height, 0)
# assertEqual(self.tree.height, 1)

tree.node.right = AVLTree(Node(6))
tree.update_height()
# assertEqual(self.tree.height, 1)

tree.node.right.node.right = AVLTree(Node(8))
tree.update_height()
tree.display()

# assertEqual(self.tree.height, 2)
