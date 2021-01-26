# Generic Tree Node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None  # also track parent of node for easier rotations
        self.height = 1


# AVL Tree class which supports insertion, deletion operations
class AvlTree(object):
    # def __init__(current, root=None):
    #     current.root = root

    def insert(self, root, key):
        # Step 1 — Perform normal BST
        if not root:
            return TreeNode(key)

        elif key < root.val:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        # Step 2 — Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 — Get the balance factor
        balance = self.get_balance(root)

        # Step 4 — If the node is unbalanced, then try out the 4 cases

        # Case 1 — Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Case 2 — Right Right
        if balance < -1 and key > root.left.val:
            return self.left_rotate(root)

        # Case 3 — Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 — Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Recursive function to delete a node with a given key
    # from subtree with given root.
    # It returns root of the modified subtree
    def delete(self, root, key):
        # Step 1 — Perform standard BST delete
        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        # if the tree only has one node, simply return it
        if root is None:
            return root

        # Step 2 — Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Step 3 — Get the balance factor
        balance = self.get_balance(root)

        # Step 4 — If the node is unbalanced, then try out the 4 cases

        # Case 1 — Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Case 2 — Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Case 3 — Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 — Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        # perform rotation
        y.left = z
        z.right = t2

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # return new root
        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        # perform rotation
        y.right = z
        z.left = t3

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # return the new root
        return y

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root

        return self.get_min_value_node(root.left)

    def pre_order(self, root):
        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def return_pre_order(self, root):
        if not root:
            return

        values = []

        # def inner_pre_ord(root):
        #     values.append(root.val)


# tree = AvlTree()
# root = None
# nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
#
# for num in nums:
#     root = tree.insert(root, num)
#
# # pre-order traversal
# print("Preorder Traversal after insertion - ")
# tree.pre_order(root)
# print()
#
# # delete
# key = 10
# root = tree.delete(root, key)
#
# # preorder traversal
# print("Preorder Traversal after deletion - ")
# tree.pre_order(root)
# print()
