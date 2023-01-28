'''
เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด

*** Fun with permute ***
input : 1,2,3
Original Cofllection:  [1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]


*** Fun with permute ***
input : 1,1,2,3
Original Cofllection:  [1, 1, 2, 3]
Collection of distinct numbers:
 [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]


'''
print("*** Fun with permute ***")
inputall= input("input : ").split(",")  # list

results = list(map(int, inputall)) # การแปลงค่าใน list เป้น int แล้วใส่ list อีกรอบ

print("Original Cofllection: ",results)

source = [[]]

for i in results:
  new_source = []
  
  for j in source:
    
    for k in range(len(j)+1):
      
      new_source.append(j[:k] + [i]+ j[k:])
      source = new_source

print("Collection of distinct numbers:\n",source)