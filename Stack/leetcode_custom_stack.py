class CustomStack:

    def __init__(self, maxSize: int):
        self.items = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.items)<self.maxSize:
            self.items.append(x)
        

    def pop(self) -> int:
        if self.items == []:
            return -1
        else:
            return self.items.pop()
        

    def increment(self, k: int, val: int) -> None:
       
        if k > len(self.items):
            k = len(self.items)

    
        for i in range(k):
            self.items[i] = self.items[i] + val


c = CustomStack(12)
c.push(83)
c.increment(2,60)
c.increment(9,61)
c.increment(1,61)
c.push(82)
c.push(21)
c.push(58)
c.increment(8,8)
c.push(22)
c.push(80)
c.increment(1,64)
c.pop()
c.pop()
c.push(24)