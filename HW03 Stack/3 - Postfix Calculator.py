'''

จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

โดยให้แสดงผลลัพธ์ตามตัวอย่าง



class Stack():

    def __init__(self, ls = None):

    def push(self,i):

    def pop(self):

    def isEmpty(self):

    def size(self):

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))

'''



class Stack():

    def __init__(self, ls = None):
        if ls ==None:
            self.items=[]
        else :
            self.items=ls
        self.sizes=0

    def push(self,i):
        self.items.append(i)
        self.sizes+=1

    def pop(self):
        if not self.isEmpty():
            self.sizes -= 1
            return self.items.pop()
        else :
            print("Stack is empty !!!")

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return self.sizes

def postFixeval(st):

    s = Stack()

    for i in st :
        if i == '+':
            x = s.pop()
            y = s.pop()
            ans = float(x)+float(y)
            s.push(ans)
        
        elif i=='-':
            x = s.pop()
            y = s.pop()
            ans = float(y)-float(x)
            s.push(ans)

        elif i=='*':
            x = s.pop()
            y = s.pop()
            ans = float(x)*float(y)
            s.push(ans)
        
        elif i=='/':
            x = s.pop()
            y = s.pop()
            ans = float(y)/float(x)
            s.push(ans)
        else :
            s.push(i)
        


    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))