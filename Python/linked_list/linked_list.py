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
        try:
            if index == self.length:
                self.append(data)
                return
            elif index == 0:
                self.prepend(data)
            elif index > self.length or index < 0:
                raise IndexError("Index out of range")
            else:
                new_node = Node(data)
                current_node = self.head
                i = 1
                while current_node.next is not None:
                    if index == i:
                        new_node.next = current_node.next
                        current_node.next = new_node
                        self.length += 1
                        return
                    i += 1
                    current_node = current_node.next

        except IndexError:
            print("Index out of range")


    def delete(self, data):
        # TODO: remove first node matching this value
        pass

    def find(self, data):
        # TODO: return index of first match, or -1
        pass

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


    def __repr__(self):
        # TODO: return something like "1 -> 2 -> 3 -> None"
        pass

    def __len__(self):
        return self.length