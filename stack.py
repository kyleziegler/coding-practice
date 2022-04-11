# Kyle Ziegler 5/2021
# Implementing a stack in a custom class

class Stack():
    l = []
    lowest_val = None
    # def __init__(self, data):
    #     self.data = data
    # Peek, pop, push

    def peek(self):
        if(len(self.l) > 0):
            return self.l[-1]
        else:
            raise Exception("No elements in the list")

    def push(self,data) -> None:
        
        if (self.lowest_val == None):
            self.lowest_val = data
        elif(data < self.lowest_val):
            self.lowest_val = data

        self.l.append(data)
    
    def pop(self):
        if(len(self.l) > 0):
            return self.l.pop()
        else:
            raise Exception("No elements in the list")

    def min(self):
        if(len(self.l) > 0):
            return self.lowest_val
        else:
            raise Exception("No elements in the list")

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(-1)

print(a.min())

