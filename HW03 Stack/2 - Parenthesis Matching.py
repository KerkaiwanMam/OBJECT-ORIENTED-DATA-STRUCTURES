'''
จงเขียนโปรแกรมเพื่อตรวจสอบว่า นิพจน์มีวงเล็บครบถ้วนหรือไม่ โดยใช้ Stack ช่วยในการแก้ปัญหา

โดยสามารถแจ้งได้ว่าข้อผิดพลาดที่เกิดขึ้นเกิดจากสาเหตุใด

1. มี วงเปิดไม่ตรงชนิดกับวงเล็บปิด

2. วงเล็บปิดเกิน

3. วงเล็บเปิดเกิน

แล้วให้แสดงผลตามตัวอย่าง


Enter expresion : [[)))))
[[))))) Unmatch open-close  


Enter expresion : [[)))))
[[))))) Unmatch open-close  

Enter expresion : (())))
(()))) close paren excess

Enter expresion : )}]
)}] close paren excess

Enter expresion : (((
((( open paren excess   3 : (((

Enter expresion : (a+c)(a-b)*c(-a
(a+c)(a-b)*c(-a open paren excess   1 : (


Enter expresion : (([]))
(([])) MATCH

Enter expresion : (){}[]}
(){}[]} close paren excess
'''


class stack :
    def __init__ (self, list = None) :
        if list == None :
          self.items = []
        else :
           self.items = list
        self.sizes = 0
    
    def __str__(self):
        s = ''
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
                    print(ch)
                    print(ele)
                    print("({[".index(ch))
                    print(")}]".index(ele))
                    return "Unmatch open-close"
            else:
                
                return "close paren excess"
            
    if s1.isEmpty():
        return "MATCH"
    
    print("open paren excess   " + str(s1.size()) + ' : ',end='' )
    return s1


Ex = input("Enter expresion : ")
print(Ex,end=' ')
print(parenMatch(Ex))
    