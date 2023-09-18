class Node:
    def __init__(self,init_data) -> None:
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,new_data):
        self.data = new_data
    def set_next(self,new_next):
        self.next = new_next

    
class Orderedlist:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def search(self,item):
        current = self.head
        found = False
        stop = False

        while current != None and not stop and not found:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found
    
    def add(self,item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop =True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            temp = Node(item)
            temp.set_next(self.head)
            self.head = temp
        else:
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)

    def print_items(self):
        current = self.head

        while current != None:
            print("Data:",current.get_data())
            current = current.get_next()


    def remove(self,item):
        current = self.head
        previous = None
        

        while current != None :
            if current.get_data() == item:
                previous.set_next(current.get_next()) 
                break
            else:
                previous = current
                current = current.get_next()

    def size(self):
        current = self.head
        cnt = 0
        while current != None:
            cnt+=1
            current = current.get_next()

        return cnt



myobj = Orderedlist()
myobj.add(0)
myobj.add(3)
myobj.add(4)
myobj.add(5)
myobj.add(2)
myobj.print_items()
myobj.remove(3)
print("-"*20)
myobj.print_items()
print("Size:",myobj.size())