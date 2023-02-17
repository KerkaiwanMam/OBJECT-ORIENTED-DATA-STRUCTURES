class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("-1")
            
            return 0
    
    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return 0

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

q = Queue()

lst = input("Enter Input : ").split(",")

for i in range(len(lst)):
    if (lst[i][0]=='E'):
        l = lst[i][2:]
        
        print("Add",l,"index is",q.size())
        q.enqueue(l)

    elif (lst[i][0]=='D' ):
        if (not q.isEmpty()):
            print("Pop",q.front(),"size in queue is",q.size()-1)
        q.dequeue()    
if q.isEmpty():
   print("Empty")
else:
    print("Number in Queue is : ",q.items)
        
            
