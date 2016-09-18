
# 汉诺塔 递归实现，先放着

def move(n,a='A',b='B',c='C'):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4)


# hanoi(3,'a','b','c')
#       ↓

#               ↗ hanoi(1,'a','b','c') a-->c
# hanoi(2,'a','c','b')→ hanoi(1,'a','c','b') a-->b
#               ↘ hanoi(1,'c','a','b') c-->b


# hanoi(1,'a','b','c')    a-->c


#               ↗ hanoi(1,'b','c','a') b-->a
# hanoi(2,'b','a','c')→ hanoi(1,'b','a','c') b-->c
#               ↘ hanoi(1,'a','b','c') a-->c