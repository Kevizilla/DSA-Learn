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
                i = parentIndex;
            } else {
                break;
            }
        }
    }

    public int extractMax() {
        if (size == 0) return -1;

        int max = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);
        return max;
    }
    private void heapifyDown(int i) {
        while (true) {
            int largest = i;
            int left = leftChild(i);
            int right = rightChild(i);

            if (left < size && heap[left] > heap[largest]) {
                largest = left;
            }
            if (right < size && heap[right] > heap[largest]) {
                largest = right;
            }

            if (largest != i) {
                int temp = heap[i];
                heap[i] = heap[largest];
                heap[largest] = temp;
                i = largest;
            } else {
                break;
            }
        }
    }
}
