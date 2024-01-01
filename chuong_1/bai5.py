class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, element):
        if self.isFull():
            print('Stack is full')
            return
        self.top += 1
        self.data[self.top] = element

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return -1
        element = self.data[self.top]
        self.top -= 1
        return element

    def isFull(self):
        return self.top == self.size - 1

    def isEmpty(self):
        return self.top == -1

    def count(self):
        return self.top + 1


stack = Stack(5)
stack.push(3.0)
stack.push(2.0)
stack.push(4.0)
stack.push(2)
print(stack.pop())
print(stack.pop())
print('số phần tử trên ngăn xếp:', stack.count())
