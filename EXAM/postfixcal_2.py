class Stack():

    def __init__(self, ls = None):
        if ls == None :
            self.itmes = []
        else :
            self.itmes = ls

    def push(self,i):
        self.itmes.append(i)

    def pop(self):
        return self.itmes.pop()

    def isEmpty(self):
        return self.itmes == []

    def size(self):
        return len(self.itmes)

def postFixeval(st):

    s = Stack()

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