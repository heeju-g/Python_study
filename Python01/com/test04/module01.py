#import math
#math라는 모듈을 사용하겠다
#math.pi
from math import pi
#math라는 모듈에서 pi만 가져와서 사용하겠다

def circle(x):
    return pi * x * x

if __name__ == '__main__':
    r = input('반지름 : ')
    print('반지름이 %s인 원의 넓이는 %f입니다'% (r,circle(int(r))))