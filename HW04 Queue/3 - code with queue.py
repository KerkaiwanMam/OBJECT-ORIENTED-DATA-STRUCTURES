class Queue:
    def __init__(self):
        self.inp = list()
        self.prt = list()
 
    def enqueue(self,data):
        self.inp.append(data)
    
    

q = Queue()
txt,hint = input('Enter code,hint : ').split(',')
for i in range(0,len(txt)):
    y = chr(ord(txt[i]) + ord(hint) - ord(txt[0]))
    q.enqueue(y)
    print(q.inp)
    