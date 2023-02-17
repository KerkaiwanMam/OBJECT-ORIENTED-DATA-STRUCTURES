class stack:
    def __init__(self,list = None):
        if list == None :
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        s =''
        for i in self.items:
            s += str(i)
        return s
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Empty"
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
sym = set(["+","-","*","/","^"])
pri = {'(':-99 , '+':0, '-':0,'*':2,'/':2,'^':3}

def infix2postfix(exp):
    s = stack()

    postfix = ''

    for ch in exp :
        if ch in sym:
            if s.isEmpty():
                s.push(ch)
            else:
                while not s.isEmpty():
                    if s.peek() =='(':
                        break
                    else :
                        if pri[ch] <= pri[s.peek()]:
                            postfix += str(s.pop())
                        else: break
                s.push(ch)
        elif ch == '(' :
            s.push(ch)
        elif ch == ')' :
            while s.peek() != '(' :
                postfix += str(s.pop())
            s.pop()
        else:
            postfix += ch
    while not s.isEmpty():
        postfix += str(s.pop())
    return postfix

print(" ***Infix to Postfix***" )
exp = input('Enter Infix expression : ')

print('PostFix : ',end='')
print(infix2postfix(exp))



            