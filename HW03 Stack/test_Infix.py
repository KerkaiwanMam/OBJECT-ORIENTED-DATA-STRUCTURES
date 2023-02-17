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
            s+= str(ele) 
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

symbol = set(["+" , "-" , "*" , "/" , "^"])
priori = { '(':-99, '+':0 , '-':0 , '*':2 , '/':2 , '^':3}


def infix2postfix(exp):
    S = stack()

    postfix = ''

    for ch in exp :
        if ch in symbol:
            if S.isEmpty():
                print(ch)
                S.push(ch)
            else:
                while not S.isEmpty():
                    if S.peek() == '(':
                        break
                    else:
                        if priori[ch]<=priori[S.peek()]:
                            postfix += str(S.pop())
                        else:
                            break
                        
                S.push(ch)
        elif ch == '(' :
            S.push(ch)
        elif ch == ')' :
            while S.peek() != '(':
                postfix += str(S.pop())
            S.pop()
        else:
            print(ch)
            postfix += ch
    while not S.isEmpty():
        postfix += str(S.pop())
    return postfix
            
print(" ***Infix to Postfix***" )
exp = input('Enter Infix expression : ')

print('PostFix : ')
print(infix2postfix(exp))
    