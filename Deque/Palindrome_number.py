


class Deque:
    def __init__(self) -> None:
        self.items = []

    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)


def check_palindrome(string):
    deque_obj = Deque()

    for char in string:
        deque_obj.add_rear(char)

    still_equal = True

    while deque_obj.size() > 1 and still_equal:
        front = deque_obj.remove_front()
        rear = deque_obj.remove_rear()

        if front != rear:
            still_equal = False

    return still_equal

flag = check_palindrome("Ganesh")
print(flag)

    
