class stack :
    def __init__ (self, list = None) :
        if list == None :
          self.items = []
        else :
           self.items = list
        self.sizes = 0
    
    def __str__(self):
        s = "stack of " + str(self.size()) + ' items : '
        for ele in self.items:
            s+='\n' + str(ele) + ' '

        return s
    
    def pop(self):
        if not self.isEmpty():
            self.sizes -= 1
            return self.items.pop()
        else :
            print("Stack is empty !!!")

    def peek(self):
        return self.items[-1]

    def push (self,data):
        self.items.append(data)
        self.sizes += 1

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return self.sizes

s=stack()

s.push('a')

s.pop()
s.pop()

s.push('b')
s.push('c')
print(s.isEmpty())

print(s.size())
print(s.items)


