check ='T'
def palindrome(i,txt):
    n = len(txt) - 1
    if txt[i] != txt[n-i]:
        return '\'' + txt + '\'' + ' is not palindrome'
    if i == n:
        return '\'' + txt + '\'' + ' is palindrome'
    return palindrome(i+1,txt)
inp = input('Enter Input : ')
print(palindrome(0,inp))