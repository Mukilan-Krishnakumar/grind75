class MyQueue:

    def __init__(self):
        self.stack1 = [] # Front of queue
        self.stack2 = [] # Back of queue

    def push(self, x: int) -> None:
        self.stack2.insert(0,x)

    def pop(self) -> int:
        if not self.stack1:
            while self.stack2:
                self.stack1.insert(0, self.stack2.pop(0))
        return self.stack1.pop(0)

    def peek(self) -> int:
        if not self.stack1:
            while self.stack2:
                self.stack1.insert(0, self.stack2.pop(0))
        return self.stack1[0]
        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
