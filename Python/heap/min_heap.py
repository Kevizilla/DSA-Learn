class MinHeap:
    def __init__(self, values=None):
        if values is None:
            self.heap = []
        else:
            self.heap = values.copy()
            self.heapify()

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _bubble_down(self, index):
        while True:
            left = self._left(index)
            right = self._right(index)

            if left >= len(self.heap):
                break

            smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[index] <= self.heap[smallest]:
                break

            self._swap(index, smallest)
            index = smallest

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0:
            parent_index = self._parent(index)

            if self.heap[parent_index] > self.heap[index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def remove_min(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._bubble_down(0)

        return min_value

    def heapify(self):
        current = len(self.heap) // 2 - 1

        while current >= 0:
            self._bubble_down(current)
            current -= 1