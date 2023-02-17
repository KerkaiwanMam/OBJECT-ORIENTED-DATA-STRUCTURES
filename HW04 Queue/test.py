class QUEUE :
    def __inti__(self):
        self.items = list()
    
    def deQueue(self):
        return self.items.popleft()
    
    def enQueue(self,data):
        self.items.append(data)
    
    def isEmpty(self):
        return len(self.items) == 0

qDeq = QUEUE()

for i in range(1000):
    qDeq.enQueue(i)