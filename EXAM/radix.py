class Queue:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def deQueue (self):
        return self.items.pop(0)
    
    def enQueue (self,data):
        self.items.append(data)
    
    def isEmpty(self):
        return len(self.items) == 0
    

        
        
def radix_sort(l) :
    q = Queue(l)
    max_bits = get_max_digit(max(l))
    qq =[Queue(),Queue(),Queue(),Queue(),Queue(),
        Queue(),Queue(),Queue(),Queue(),Queue()]
    for i in range (1,max_bits+1) : 
        while not q.isEmpty() :
            num = q.deQueue()
            index_digit = get_digit(num,i)
            qq[index_digit].enQueue(num)
        for i in range (10) :
            while not qq[i].isEmpty() :
                q.enQueue(qq[i].deQueue())
    return q.items

def get_digit(n, d):
    for i in range(d-1):
        n //= 10
    return n % 10

def get_max_digit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return  i

li = [int(x) for x in input("Enter : ").split(",")]

print(radix_sort(li))
# print(str(li))