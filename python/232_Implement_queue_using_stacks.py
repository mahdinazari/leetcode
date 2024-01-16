class MyQueue:    
    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        return self.stack.pop(0)
        

    def peek(self) -> int:
        return [] if len(self.stack) == 0 else self.stack[0


    def empty(self) -> bool:
        return self.stack == []


if __name__ == '__main__':
    yQueue = MyQueue()
    push(1) # queue is: [1]
    push(2) # queue is: [1, 2] (leftmost is front of the queue)
    peek()  # return 1
    pop()   # return 1, queue is [2]
    empty() # return false
