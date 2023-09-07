class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def matches(open,close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)

def par_checker(symbol_string):
    s = Stack()
    index = 0
    balanced = True

    while index < len(symbol_string) and balanced:
        if symbol_string[index] in "({[":
            s.push(symbol_string[index])

        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol_string[index]):
                    balanced = False
        
        index+=1
    
    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
