class MyQueue:

    def __init__(self):
        self.stack1 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        x = self.stack1[0]
        del self.stack1[0]
        return x

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()