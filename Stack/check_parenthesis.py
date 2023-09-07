class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def check_parenthesis(my_str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(my_str) and balanced:
        if my_str[index] == "(":
            s.push(my_str[index])
        else:
            if s.is_empty():
                balanced =  False
            else:
                s.pop()

        index+=1

    if balanced and s.is_empty():
        return True 
    else:
        return False


print(check_parenthesis('((()))'))
print(check_parenthesis('(()'))

            
