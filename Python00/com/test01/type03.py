# list

# 생성자
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
print(a)
a[1] = 'b'
print(a)

#[]사용
b = [1,2,3,4,5]
print(b)
print(b[1]+b[3])

b.reverse()
print(b)

b.append(6)
print(b)

b.sort()
print(b)

# 중첩
c = ['a','b','c','d',['e','f','g']]
print(c)
print(c[4])
print(c[4][0])
c.append('a')
# list + list
print(b+c)
















