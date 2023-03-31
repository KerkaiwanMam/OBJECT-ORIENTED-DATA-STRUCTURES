# def print1ToN(n):
#     if n <= 1:
#         print(1, end=' ')
#     else :
#         return print1ToN(n-1), print(n,end=' ')

# def printNto1(n):
#     if n <= 1:
#         print(1)
#     else :
#         return print(n, end = ' '), printNto1(n-1)

# n = int(input("Enter Input : "))

# print1ToN(n)
# printNto1(n)

# n_max = 100
# def findmax(i,inp):
#     global n_max
#     if i == 0:
#         n_max = int(inp[0])
#     elif i == len(inp):
#         return n_max
#     else:
#         if int(inp[i]) < n_max:
#             n_max = int(inp[i])
#     i+=1
#     return findmax(i,inp)        

# inp = input('Enter Input : ').split()
# print('Max :',findmax(0,inp)) 
def mini(nums):
    if len(nums) == 1:
        return nums[0]
    
    m = mini(nums[1:])
    if m > nums[0]:
        return m
    else:
        return nums[0]



inp = list(map(int,input("Enter Input : ").split()))
print(f"Min : {mini(inp)}")

# def staircase(k,n):
#      if (abs(k)-1) == n:
#           if k > 0 :
#                return "_" * (k-n-1) + "#" * (n+1)
#           else :
#                return "_" * n + "#" * (abs(k)-n)

#      if k > 0 :
#           return "_" * (k-n-1) + "#" * (n+1) + "\n" + str(staircase(k,n+1))
#      elif k < 0 :
#           return "_" * n + "#" * (abs(k)-n) + "\n" + str(staircase(k,n+1))
#      elif k == 0 :
#           return "Not Draw!"

# print(staircase(int(input("Enter Input : ")),0))