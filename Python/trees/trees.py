class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.data})"


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # TODO: for a plain binary tree, no ordering rule —
        # just insert at the first available empty spot,
        # level by level (like filling a level-order layout)
        pass

    def preorder(self):
        # TODO: root -> left -> right
        pass

    def inorder(self):
        # TODO: left -> root -> right
        pass

    def postorder(self):
        # TODO: left -> right -> root
        pass

    def level_order(self):
        # TODO: breadth-first, level by level
        pass

    def height(self):
        # TODO: longest path from root to a leaf
        pass