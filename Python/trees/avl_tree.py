class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
    def __repr__(self):
        return f"AVLNode({self.data})"

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = 1 + max(
            self._get_height(node.left),
            self._get_height(node.right)
        )

    def _get_balance(self, node):
        if node is None:
            return 0
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return left_height - right_height

