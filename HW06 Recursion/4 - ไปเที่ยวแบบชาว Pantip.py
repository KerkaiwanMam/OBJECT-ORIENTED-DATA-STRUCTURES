count = 0
def printSack(path, maxi):
  global arr, count
  count += 1
  for i in range(maxi+1):
    print(arr[path[i]], end = ' ')
  print()

def pantip(path, i, k, n):
  global N, arr

  if n< N:    
    price = arr[n]   

    if k < price:               # ถ้าเงินไม่พอให้ไป index ต่อไป
      pantip(path, i, k, n+1) 
    else:                       # ถ้าซื้อได้
      k -= price  
      path[i] = n 

      if k == 0:                # ซื้อครบ
        printSack(path, i)
      else:           
        pantip(path, i+1, k, n+1)   # ถ้าเงินยังเหลือ
        
      pantip(path, i, k+price, n+1)   
  return count


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
N = len(arr)         # จำนวนสินค้า
path = N*[-1]        # ข้อมูลที่เก็บมา (ว่าง)
k = int(inp[0])      # จำนวนเงิน
i = 0                # index ข้อมูล
n = 0                # index สินค้า

pattern = pantip(path, i, k,n)
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))