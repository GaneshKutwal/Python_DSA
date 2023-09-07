

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


my_str = "STRING"

s = Stack()

i = 0
while i < len(my_str):
    s.push(my_str[i])
    i+=1


while s.is_empty() == False:
    print(s.pop(),end="")

