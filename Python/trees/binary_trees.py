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
        result = []

        def _traverse(node):
            if node is None:
                return
            _traverse(node.left)
            result.append(node.data)
            _traverse(node.right)

        _traverse(self.root)
        return result

    def postorder(self):
        result = []

        def _traverse(node):
            if node is None:
                return
            _traverse(node.left)
            _traverse(node.right)
            result.append(node.data)

        _traverse(self.root)
        return result

    def height(self):
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)
