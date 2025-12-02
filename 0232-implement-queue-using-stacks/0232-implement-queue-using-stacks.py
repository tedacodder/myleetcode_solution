class MyQueue:

    def __init__(self):
        self.queue=[]
        self.top=0
        self.total=0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.total+=1
        

    def pop(self) -> int:
        val=self.queue[self.top]
        self.top+=1
        return val
        

    def peek(self) -> int:
        return self.queue[self.top]
        

    def empty(self) -> bool:
        return (self.total-self.top)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()