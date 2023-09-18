class Node:
    def __init__(self,init_data) -> None:
        self.data = init_data
        self.next = None

    def get_data(self) :
        return self.data
    
    
    def get_next(self):
        return self.next
    
    def set_data(self,new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next = new_next


class Unorderedlist:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) ->bool:
        return self.head == None
    
    def add(self,item) ->None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self) -> int:
        current = self.head
        count = 0

        while current != None:
            count +=1
            current = current.get_next()

        return count
    
    def search(self,item) -> bool:
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found
    
    def remove(self,item) -> None:
        current = self.head
        previous = None
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print_item(self) ->None:
        current = self.head

        i = 0
        while current != None:
            print(i," poistion : ",current.get_data())
            current = current.get_next()
            i+=1

    def append(self,item) ->None:
        current = self.head

        while current.get_next() != None:
            current = current.get_next()

        
        temp = Node(item)
        current.set_next(temp)

    def insert(self,pos,item) ->None:
        if pos  == 0:
            self.add(item)
        else:
            current = self.head

            i = 0

            while i <pos-1:
                current = current.get_next()
                i+=1

            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)

    def index(self,item):
        ind = 0
        current = self.head
       
        while current.get_data() != item :
            current = current.get_next()
            ind+=1

        return ind 
    
    def pop(self):
        current = self.head

        while current.get_next().get_next() != None:
            current = current.get_next()

        ele = current.get_next().get_data()
        current.set_next(None)
        return ele
       

            
# 10,20,30,40
        


            


mylist = Unorderedlist()

print(mylist.is_empty())

mylist.add(31)
mylist.add(77)
mylist.add(25)
mylist.add(17)
mylist.add(28)
mylist.add(98)

print("Size : ",mylist.size())
print("17 in mylist: ",mylist.search(17))
print("22 in mylist: ",mylist.search(22))

mylist.remove(28)
print("Size: ",mylist.size())
mylist.print_item()
mylist.append(12)
print("-"*20)
mylist.print_item()
mylist.insert(3,20)
print("-"*20)

print("Value Present at index : ",mylist.index(77))
print("Before pop")
mylist.print_item()
print("Popped element: ",mylist.pop())
print("Popped element: ",mylist.pop())
print("After Pop\n")
mylist.print_item()





