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


def parenMatch(ListEx):
    """   check parentesis return true or False 
    """
    s1 = stack()
    for ele in ListEx :
        if ele in "({[":
            s1.push(ele)
        elif ele in ")}]" :
            if not s1.isEmpty():
                ch = s1.pop()

                if "({[".index(ch) != ")}]".index(ele):
                    print("paren not match")
                    return False
            else:
                print("close exceed")
                return False #open exceed
            
    if s1.isEmpty():
        print("Match")
        return True
    print("open exceed")
    m= 0
    for ele in ListEx :
        if ele in "({[":
            
            m += 1
        elif ele in ")}]" :
            if not s1.isEmpty():
                
                m -= 1
    print(s1)
    return m

Ex = "([("
print(parenMatch(Ex))
    