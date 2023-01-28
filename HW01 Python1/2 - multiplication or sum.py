'''
รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show 
ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 
ให้ show ผลคูณของจำนวนทั้งสอง


*** multiplication or sum ***
Enter num1 num2 : 20 30
The result is 600


*** multiplication or sum ***
Enter num1 num2 : 40 60
The result is 100

'''



print("*** multiplication or sum ***")
num1,num2 = map(int,input("Enter num1 num2 : ").split())

result = num1 * num2
sum1 = num1+num2
if result > 1000 :
    print("The result is", sum1)
else:
    print("The result is", result)
    
