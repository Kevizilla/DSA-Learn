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

    def preorder(self):
        result = []
        def _traverse(node):
            if node is None:
                return
            result.append(node.data)
            _traverse(node.left)
            _traverse(node.right)
        _traverse(self.root)
        return result

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