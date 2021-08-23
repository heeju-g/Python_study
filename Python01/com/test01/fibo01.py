


#fibonacci 수열 : 0 1 1 2 3 5 8 13 21 34

def fibo01(n):
    a,b = 0,1
    i = 1
    for i in range(n-1):
        print(a, end=' ')
        a,b = b, a+b
        i += 1
    print()  
def fibo02(n):
    lst = list()
    a,b = 0,1
    i = 1
    for i in range(n-1):
        lst.append(a)
        a,b = b, a+b
        i+=1
    print(lst)

if __name__ == '__main__':
    n = int(input('입력: '))
    fibo01(n)
    fibo02(n)





