class Stack:
    def __init__(self, list = None): 
        if list == None: 
            self.items = []
        else:
            self.items = list

    def push(self, i): 
        self.items.append(i)

    def pop(self): 
        return self.items.pop()

    def isEmpty(self): 
        return self.items == [] 

    def size(self): 
        return len(self.items)
    
    def getValue(self):
        return self.items

def run(s):
        # print(s)
        # stack = []
        for i in range(len(s)):
            # print(s[i])
            if s[i].isdigit():
            #เช็คว่าเป็นตัวเลข
                machine.push(int(s[i]))
                # stack.append(int(s[i]))

            elif s[i]=="+":
                a=machine.pop()
                b=machine.pop()
                machine.push(int(a)+int(b))
                # stack.append(int(a)+int(b))

            elif s[i]=="*":
                a=machine.pop()
                b=machine.pop()
                machine.push(int(a)*int(b))
                # stack.append(int(a)*int(b))

            elif s[i]=="/":
                a=machine.pop()
                b=machine.pop()
                machine.push(int(a)//int(b))
                # stack.append(int(b)/int(a))

            elif s[i]=="-":
                a=machine.pop()
                b=machine.pop()
                # print("*")
                machine.push(int(a)-int(b))
                # stack.append(int(b)-int(a))

            elif s[i] == "DUP":
                a=machine.pop()
                # print(a)
                machine.push(int(a))
                machine.push(int(a))

            elif s[i] == "POP":
                    machine.pop()

            elif s[i] == "PSH":
                machine.push(s[i-1])

            else:
                machine.push(s[i])
                return "Invalid instruction: "+ machine.pop()
        print(machine)
        if machine.items == []:
            return 0
        else:
            return machine.pop()

print("* Stack Calculator *")
arg = list(input("Enter arguments : ").split(' '))
machine = Stack()
print(run(arg))