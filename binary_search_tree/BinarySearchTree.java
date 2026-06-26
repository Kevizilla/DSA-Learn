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

    public void inorder(){
        inorder(root);
    }
    private void inorder(Node node){
        if (node == null){
            return;
        }
        inorder(node.left);
        System.out.println(node.data);
        inorder(node.right);
    }

    public void preorder(){
        preorder(root);
    }
    private void preorder(Node node){
        if (node == null){
            return;
        }
        System.out.println(node.data);
        preorder(node.left);
        preorder(node.right);
    }

    public void postorder(){
        postorder(root);
    }
    private void postorder(Node node){
        if (node == null){
            return;
        }
        postorder(node.left);
        postorder(node.right);
        System.out.println(node.data);
    }
}
