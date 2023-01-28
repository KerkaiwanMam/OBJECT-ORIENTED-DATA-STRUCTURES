'''
*** Fun with Drawing ***
Enter input : 2
#####
#...#
#.#.#
#...#
#####



'''


print("*** Fun with Drawing ***")
num1 = int(input("Enter input : "))

sum = num1 + (num1-1)*3

sub = sum/2


pos = [[False for i in range(sum)] for j in range(sum)]

for i in range(sum) :
    for j in range(sum):
        if i==j and i%2 ==0 :
            for k in range(j,sum-i) :
                pos[i][k] = True
                pos[k][i] = True
            pos[i][sum-1] = True
            for l in range(j,sum-i) :
                pos[k][l] = True
                pos[l][k] = True
            break
for x in range(len(pos)):
    for y in range(len(pos)):
        if pos[x][y]:
            print("#",end='')
        else:
            print(".",end='')
    print()


