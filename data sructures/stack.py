
class stack():

    def __init__(self):
        self.front_pointer =-1 
        self.stack = []

    def pop(self):
        if self.front_pointer !=-1:
            item = self.stack[self.front_pointer]
            self.stack = self.stack[0:self.front_pointer]
            self.front_pointer -= 1
            return item
        else:
            return None
            
    def push(self,value):
        self.stack.append(value)
        self.front_pointer +=1
        return self.stack
        
    def peek(self):
        if self.front_pointer !=-1:
            item = self.stack[self.front_pointer]
            return item
        else:
            return None
            
    def size(self):
        return(len(self.stack))
