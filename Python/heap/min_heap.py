class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

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
        # Handle empty heap
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()
        current_index = 0
        # Bubble down
        while True:
            left_index = self._left(current_index)
            right_index = self._right(current_index)
            if left_index < len(self.heap):
                if right_index < len(self.heap):
                    if self.heap[current_index] > min(self.heap[left_index], self.heap[right_index]):
                        if self.heap[current_index] > self.heap[left_index]:
                            self._swap(current_index, left_index)
                            current_index = left_index
                        else:
                            self._swap(current_index, right_index)
                            current_index = right_index
                    else:
                        break
                else:
                    if self.heap[current_index] > self.heap[left_index]:
                        self._swap(current_index, left_index)
                        current_index = left_index
                    else:
                        break
            else:
                break

        return min_value