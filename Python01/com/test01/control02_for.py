subject = ['java','javascript','python']

for s in subject:
    print(s, end=' ')
else:
    print('재밌다')

for i in range(1,100):
    print(i, end=' ')

print('-------------------')
print('구구단')
for i in range(2,10):
    print('<<'+str(i)+'단>>')
    for j in range(1,10):
        print(i,'*',j,'=',i*j,sep=' ')
    print()
    
# range 이용해서 10 - 1 거꾸로 출력
for i in range(10,0,-1):
    print(i,end=' ')
    