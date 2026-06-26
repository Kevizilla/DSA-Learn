package binary_search_tree;

public class BinarySearchTree {
    private Node root;

    public void insert(int data) {
    root = insert(root, data);
    }

    private Node insert(Node node, int data){
        if(node == null){
            return new Node(data);
        }
        if(data < node.data){
            node.left = insert(node.left, data);
        }
        else if(data > node.data){
            node.right = insert(node.right, data);
        }
        return node;
    }

    public boolean search(int data) {
        return search(root, data);
    }

    private boolean search(Node node, int data){
        if (node == null){
            return false;
        }
        else  if (data == node.data){
            return true;
        }
        else if (data < node.data){
            return search(node.left, data);
        }
        return  search(node.right, data);
    }

}
