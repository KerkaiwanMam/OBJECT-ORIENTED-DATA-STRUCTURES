class stack:
    def __init__ (self,list =None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        s = ''
        for i in self.items:
            s += str(i)
        return s
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else :
            return "Empty"
        
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
    
def postFixeval(st):
    s = stack()

    for i in st :
        if i == '+':
            x = s.pop()
            y = s.pop()
            ans = float(x) + float(y)
            s.push(ans)
        elif i == '-':
            x = s.pop()
            y = s.pop()
            ans = float(y) - float(x)
            s.push(ans)
        elif i == '*':
            x = s.pop()
            y = s.pop()
            ans = float(x) * float(y)
            s.push(ans)
        
        elif i == '/':
            x = s.pop()
            y = s.pop()
            ans = float(y) / float(x)
            s.push(ans)
        else:
            s.push(i)
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))