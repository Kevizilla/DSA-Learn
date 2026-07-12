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
        def _search(node, data):
            if node is None:
                return False
            if data == node.data:
                return True
            elif data < node.data:
                return _search(node.left, data)
            else:
                return _search(node.right, data)

        return _search(self.root, data)

    def delete(self, data):
        def _find_min(node):
            while node.left is not None:
                node = node.left
            return node.data

        def _delete(node, data):
            # Base case
            if node is None:
                return None

            # Search for the node
            if data < node.data:
                node.left = _delete(node.left, data)

            elif data > node.data:
                node.right = _delete(node.right, data)

            else:
            # -------------------------
            # Found the node to delete
            # -------------------------

            # Case 1 & 2:
            # Leaf or one child
            # TODO

            # Case 3:
            # Two children

            # Find inorder successor
            # TODO

            # Replace current node's value
            # TODO

            # Delete the duplicate successor
            # TODO

            return node

        self.root = _delete(self.root, data)

    def inorder(self):
        # same as before — but now the output will come out SORTED
        pass