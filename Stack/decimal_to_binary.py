class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def decimal_2_binary(decimal_num):
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % 2
        rem_stack.push(rem)
        decimal_num = decimal_num //2

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str += str(rem_stack.pop())
    
    return bin_str


print(decimal_2_binary(233))
print(decimal_2_binary(11))




