class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList :
    def __init__ (self):
        self.head = None

    def __str__(self):
        if self.Empty():
            return "Empty"
        cur,s = self.head , str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def Empty(self):
        if self.head is None:
            return True
        return False
    
    def append(self, item):     
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n= n.next
        n.next = new_node
    
l = LinkedList()
r1, r2 = input('Enter Input (L1,L2) : ').split()
txt1 = r1.split('->')
s = 'L1    : '
for i in range(0,len(txt1)):
    s += txt1[i] + ' '
    l.append(txt1[i])
print(s)
txt2 = r2.split('->')
s = 'L2    : '
for i in range(0,len(txt2)):
    s += txt2[i] + ' '
for i in range(len(txt2)-1,-1,-1):
    l.append(txt2[i])
print(s)
print('Merge :' , l)
