hap01 = lambda a,b: a + b

print(hap01(10,20))

hap02 = lambda a,b,c: a+b+c
print(hap02(1,2,3))

gob = lambda a,b: a*b
print(gob(12,34))

a = [(1,'one',9),(2,'two',8),(3,'three',7),(4,'four',6)]
print(a)
a.sort(key=lambda a: a[1])
print(a)

#min01 = (lambda x,y: x if x < y else y)(1,3)
#print(min01)
min01 = lambda x,y: x if x < y else y
print(min01(1,3))

max01 = lambda x,y: x if x>y else y
print(max01(4,7))

b = lambda x: (lambda newx: x + newx)
print(b(13)(20))
c = b(13)
print(c)
d = c(20)
print(d)

# 1 - 100사이의 5의 배수 출력 
# i가 5의 배수이면 e(i)가 false인데 조건이 if not e(i)니까 애네만 조건 true가 되어서 리턴되고 리스트에 담김
e = lambda x: bool(x%5)
five = [i for i in range(1,101) if not e(i)]
print(five)

#빈 공간을 bool에 넣으면 false
f = lambda x: x if (x%5 != 0) else None
res = [i for i in range(1,101) if not f(i)]
print(res)

result = [i for i in range(1,101) if not (lambda x: x if(x%5 !=0) else None)(i)]
print(result)























