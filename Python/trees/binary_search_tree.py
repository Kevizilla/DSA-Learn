from trees.binary_trees import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(node, data):
            if node is None:
                return TreeNode(data)
            elif data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            return node
        _insert(self.root, data)

    def search(self, data):
        # TODO — return True/False
        pass

    def delete(self, data):
        # TODO — the hard one, save for last
        pass

    def inorder(self):
        # same as before — but now the output will come out SORTED
        pass