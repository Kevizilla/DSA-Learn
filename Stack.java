import linkedlist.Node;


class Stack {
    private Node top;
    private int size;

    public void push(int data) {
        Node newNode = new Node(data);
        newNode.next = top;
        top = newNode;
        size++;
    }

    public int pop() {
        if (top == null){
            return -1;
        }
        int popped = top.data;
        top =  top.next;
        size--;
        return popped;
    }

    public int peek() {
        if (top == null) return -1;
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }
}