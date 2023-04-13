class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        # 1 -> 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            print("1-Stack1", self.stack1)
            print("1-Stack2", self.stack2)
        # add value
        self.stack1.append(value)
        print("2-Stack1", self.stack1)
        print("2-Stack2", self.stack2)
        # 1 <- 2
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            print("3-Stack1", self.stack1)
            print("3-Stack2", self.stack2)
        return self.stack1

    def deleteHead(self) -> int:
        if not self.stack1: return -1
        print("del-Stack1", self.stack1)
        print("del-Stack2", self.stack2)
        return self.stack1.pop()
