class MinHeap:
    def __init__(self, values=None):
        if values is None:
            self._heap = []
        else:
            self._heap = values.copy()
            self.heapify()

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _bubble_up(self, index):
        while index > 0:
            parent = self._parent(index)

            if self._heap[parent] <= self._heap[index]:
                break

            self._swap(parent, index)
            index = parent

    def insert(self, value):
        self._heap.append(value)
        self._bubble_up(len(self._heap) - 1)

    def _bubble_down(self, index):
        while True:
            left = self._left(index)
            right = self._right(index)

            if left >= len(self._heap):
                break

            smallest = left

            if right < len(self._heap) and self._heap[right] < self._heap[left]:
                smallest = right

            if self._heap[index] <= self._heap[smallest]:
                break

            self._swap(index, smallest)
            index = smallest

    def remove_min(self):
        if not self._heap:
            return None

        if len(self._heap) == 1:
            return self._heap.pop()

        min_value = self._heap[0]
        self._heap[0] = self._heap.pop()

        self._bubble_down(0)

        return min_value

    def heapify(self):
        current = len(self._heap) // 2 - 1

        while current >= 0:
            self._bubble_down(current)
            current -= 1

    def heap_sort(arr):
        heap = MinHeap(arr)

        result = []

        while heap._heap:
            result.append(heap.remove_min())

        return result
