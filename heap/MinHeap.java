package heap;

public class MinHeap {
    private int[] heap;
    private int size;

    MinHeap(int capacity) {
        heap = new int[capacity];
        size = 0;
    }

    private int parent(int i) { return (i - 1) / 2; }
    private int leftChild(int i) { return 2 * i + 1; }
    private int rightChild(int i) { return 2 * i + 2; }

    public void insert(int data) {
        heap[size] = data;
        heapifyUp(size);
        size++;
    }

    private void heapifyUp(int i) {
        while (i > 0) {
            int parentIndex = parent(i);
            if (heap[i] < heap[parentIndex]) {
                int temp = heap[i];
                heap[i] = heap[parentIndex];
                heap[parentIndex] = temp;
                i = parentIndex;
            } else {
                break;
            }
        }
    }

    public int extractMin() {
        if (size == 0) return -1;

        int min = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);
        return min;
    }

    private void heapifyDown(int i) {
        while (true) {
            int smallest = i;
            int left = leftChild(i);
            int right = rightChild(i);

            if (left < size && heap[left] < heap[smallest]) {
                smallest = left;
            }

            if (right < size && heap[right] < heap[smallest]) {
                smallest = right;
            }

            if (smallest != i) {
                int temp = heap[i];
                heap[i] = heap[smallest];
                heap[smallest] = temp;
                i = smallest;
            } else {
                break;
            }
        }
    }

    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print(heap[i] + " ");
        }
        System.out.println();
    }
}