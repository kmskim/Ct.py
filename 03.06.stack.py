class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value) #[3]
        new_head.next = self.head #[3] -> [4]
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        #head
        # 1      2   3
        if self.is_empty:
            return "stack empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data
    
    def peek(self):
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        if self.is_empty:
            return "stack empty"
        return self.head is None
    
stack = Stack()
stack.push(5)
print(stack.head.data)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())

