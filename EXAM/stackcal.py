class StackCalc:
    s = ''
    def __init__(self):    #ใช้สำหรับสร้าง list ว่าง
        self.items = []
        
    def isEmpty(self):     #ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false
        if len(self.items) != 0:
            return False
        return True
    def size(self):        #ตรวจสอบจำนวนข้อมูลใน stack
        return len(self.items)
    def run(self,arg):
        for i in range(0,len(arg)):
            if arg[i].isnumeric():          #แทนฟังก์ชั่น PSH
                self.items.append(int(arg[i]))
            elif arg[i] in '+-*/':
                if arg[i] == '+':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x+y)
                elif arg[i] == '-':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x-y)
                elif arg[i] == '*':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(x*y)
                elif arg[i] == '/':
                    x = self.items.pop()
                    y = self.items.pop()
                    self.items.append(int(x/y))
            elif arg[i] == 'DUP':           #Duplicate (not double) ค่าบนสุดของ stack
                self.items.append(int(self.items[-1]))
            elif arg[i] == 'POP':           #Pop ค่าบนสุดออกจาก stack และ discard.
                self.items.pop()
            #elif arg[i] == 'PSH':           #ทำการ push ตัวเลขลง stack
                #self.items.append(arg[i])
            else:
                self.s = "Invalid instruction: " + arg[i]
                break
    def getValue(self):
        if len(self.items):
            return self.items[-1]
        elif len(self.s):
            return self.s
        else:
            return "0"

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())