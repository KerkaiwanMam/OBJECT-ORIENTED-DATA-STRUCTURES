class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self) -> str:
        return str(self.items)
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else :
            return "Empty"
    def size(self):
        return len(self.items)
    
    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else :
            return "Empty"
    def isEmpty(self):
        return self.items == []
    
q = Queue()
f = Queue()
s = Queue()

inp = input("Enter people : ")
for i in inp :
    q.enqueue(i)

start = False
i = 1
j = 1

while not q.isEmpty():
    if f.size() < 5 :
        f.enqueue(q.dequeue())
    elif s.size() < 5 :
        s.enqueue(q.dequeue())
        start =True
    else :
        pass
    print(str(i)+" "+str(q)+" "+str(f)+" "+str(s))
    if j%2 == 0 and not s.isEmpty():
        s.dequeue()
    if i%3 == 0 and not f.isEmpty():
        f.dequeue()
    i+=1
    if start == True:
        j+=1



