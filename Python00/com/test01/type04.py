# tuple : list와 거의 같다
#생성자 사용
a = tuple()
print(a)
b = tuple([1,2,'3'])
print(b)

# tuple은 값을 추가,수정할 수 없다
#a.append(1)
#b[1]='2'
#() 사용
d = tuple(range(3,6))
print(d)
print(b+d)

#tuple -> list
e = list(d)
e.append(6)
print(e)
#list -> tuple
f = tuple(e)
print(f)

#unpacking(갯수가 같아야 에러안남)
g,h,i,j = f
print(g)
print(h)
print(i)
print(j)
















