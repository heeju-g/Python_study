def coffee(quantity,price):
    change = price - (quantity*100)
    if change >= 0:
        prn(quantity,change)
    else:
        prn()

def prn(quantiy=0, change=0):
    if quantiy ==0 & change == 0:
        print('돈이 부족해')
    else:
        print('커피 {}잔이 나왔습니다. \n잔돈은 {}원 입니다'.format(quantiy,change))

def start():
    q = int(input('커피 몇 잔? '))
    p = int(input('돈 (1잔당 100원)'))
    coffee(q,p)
    
if __name__ == '__main__':
    start()