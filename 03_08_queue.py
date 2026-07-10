class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            return "empty"
        target = self.head
        self.head = self.head.next
        return target

    def peek(self):
        if self.is_empty():
            return "empty"
        return print(self.head.data)

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(5)
queue.peek()
queue.enqueue(3)
queue.enqueue(1)
queue.dequeue()
queue.peek()    
queue.dequeue()
queue.peek()    