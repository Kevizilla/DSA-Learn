package linkedlist;

public class linkedlist{
    Node head;
    Node tail;

    void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    void insertAt(int index, int data) {
        Node newNode = new Node(data);
        if (index == 0) {
            newNode.next = head;
            head = newNode;
            if (tail == null) {
                tail = newNode;
            }
            return;
        }
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;

        if (current.next.next == null) {
            tail = newNode;
        }
    }

    void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("Null");
    }

    int len() {
        int len = 0;
        Node current = head;
        while (current != null) {
            current = current.next;
            len++;
        }
        return len;
    }

    void remove(int index) {
        if (index == 0) {
            head = head.next;
            if (head == null) tail = null;
            return;
        }
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        if (current.next == tail) tail = current;
        current.next = current.next.next;
    }

    int search(int find) {
        Node current = head;
        int index = 0;
        while (current != null) {
            if (current.data == find) return index;
            current = current.next;
            index++;
        }
        return -1;
    }
}