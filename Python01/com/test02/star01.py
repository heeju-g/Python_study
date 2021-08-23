'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
print('1.---------')

for i in range(5):
    print('*' * (i+1))

print('2.----------')
for i in range(5):
    print(' '* (5-(i+1)),end='')
    print('*'*(i+1))
print('3.----------')
for i in range(5):
    print('*'*(5-i))

print('4.----------')
for i in range(5):
    print(' '*i,end='')
    print('*'*(5-i))
    
print('5.----------')
for i in range(5):
    print(' '* (5-(i+1)),end='')
    print('*'*(i+1),end='')
    print('*'*(i))
    




    
    
    
    
    