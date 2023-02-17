'''
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 5 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***

Enter Your List : -25 -10 -7 -3 2 4 8 10
[[-7, 2, 10], [-7, 4, 8]]

Enter Your List : -3 2 4 6 8 10
[[-3, 2, 6]]

Enter Your List : -100 100
Array Input Length Must More Than 2

Enter Your List : 5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
[[-5, 5, 5]]

'''


def calcu(input,num_in):
    newlist=[]
    for i in range(0,num_in):
        for j in range(i+1,num_in):
            for k in range(j+1,num_in):

                if((input[i]+input[j]+input[k])==5):
                    if((input[i]==input[j] or input[i]== input[k] or input[j]== input[k])):
                        
                        newlist.extend([input[i],input[j],input[k]])  # extend เป็น list ที่ไม่มี []              
                        newlist.sort()
                        print([newlist])          
                        exit()

                    else:
                        newlist.append([input[i],input[j],input[k]])
                else : pass

    print(newlist)

inpunumlist = input("Enter Your List : ").split()
result = list(map(int,inpunumlist)); 
k=0; 
for i in result:
   k=k+1 if(type(i)==int) else ""      
print("Array Input Length Must More Than 2")+exit() if(k<=2) else ""
manynum = len(result) # get many member

calcu(result,manynum)