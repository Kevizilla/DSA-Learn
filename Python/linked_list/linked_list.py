class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index == self.length:
            self.append(data)
            return
        elif index == 0:
            self.prepend(data)
        elif index > self.length:
            raise IndexError
        else:
            pass


    def delete(self, data):
        # TODO: remove first node matching this value
        pass

    def find(self, data):
        # TODO: return index of first match, or -1
        pass

    def __repr__(self):
        # TODO: return something like "1 -> 2 -> 3 -> None"
        pass

    def __len__(self):
        return self.length