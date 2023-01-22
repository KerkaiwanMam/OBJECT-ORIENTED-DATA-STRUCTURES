print("*** multiplication or sum ***")
num1,num2 = map(int,input("Enter num1 num2 : ").split())

result = num1 * num2
sum1 = num1+num2
if result > 1000 :
    print("The result is", sum1)
else:
    print("The result is", result)
    
