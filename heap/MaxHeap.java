package heap;

public class MaxHeap {
    private int[] heap;
    private int size;

    MaxHeap(int capacity) {
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
            if (heap[i] > heap[parentIndex]) {
                int temp = heap[i];
                heap[i] = heap[parentIndex];
                heap[parentIndex] = temp;
                i = parentIndex;  // move up and repeat
            } else {
                break;  // heap property satisfied, stop
            }
        }
    }

    public int extractMax() {
        // TODo
    }
    private void heapifyDown(int i) {
        // TODO — after extractMax, fix the heap downwards
    }
}
