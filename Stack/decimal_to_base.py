class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def decimal_2_base(decimal_num,base):
    rem_stack = Stack()
    symbol_str = "0123456789ABCDEF"

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num //base

    new_str = ""
    while not rem_stack.is_empty():
        new_str += symbol_str[rem_stack.pop()]

    return new_str

print(decimal_2_base(26,26))
# print(decimal_2_base(255,16))

