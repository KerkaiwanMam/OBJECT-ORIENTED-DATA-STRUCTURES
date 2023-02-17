'''
ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
โดยรหัสจะประกอบไปด้วย english word that have repeat character
เช่น bon("ball") = 48 หรือ bon("aah") = 4

def bon(w):
	### Enter Your Code Here ###
secretCode = input("Enter secret code : ")
print(bon(secretCode))

'''

def bon(w):
    
    m = max(set(w),key=w.count)
    
    '''
    dataset = [1, 1, 2, 2, 3, 4, 5, 6, 2, 1, 9, 2, 3, 2, 2, 2]
    max(dataset) # 9, since 9 is the max value in this dataset
    max(dataset, key=dataset.count) # 2 since 2 occurs the most in this dataset

    # You can also use this:
    sorted(dataset, key=dataset.count)
    # [4, 5, 6, 9, 3, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    '''



    return (ord(m) -96 )*4


   
    
secretCode = input("Enter secret code : ")
print(bon(secretCode))