class stack:
    def __init__(self,list = None):
        if list == None :
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
        return self.items.pop()
    def isEmpty(self):
        return self.items ==[]
    def size(self):
        return len(self.items)        
def parenMatch(ListEx):
    s = stack()

    for i in ListEx:
        if  i in '({[':
            s.push(i)
        elif  i in ')}]':
            if not s.isEmpty():
                ch = s.pop()
                if '({['.index(ch) != ')}]'.index(i):
                    return "Unmatch open-close "
            else :
                return "close paren excess"
    if s.isEmpty():
        return "MATCH"
    else :
        print("open paren excess   " + str(s.size())+" : ",end='')
        return s



Ex = input("Enter expresion : ")
print(Ex,end=' ')
print(parenMatch(Ex))