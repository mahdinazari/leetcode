class MyStack:
    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if len(self.stack) > 0 else None

    def top(self) -> int:
        return self.stack[len(self.stack) - 1] if len(self.stack) > 0 else None

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top()) # return 2
    print(obj.pop()) # return 2
    obj.empty() # return False
