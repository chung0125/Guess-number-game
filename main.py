import random
a =  int(random.randint(1,100))
print("猜測一個介於 1 和 100之間的數字。")
guess = int(input("請猜測數字: "))
n = 0
while guess!=a:
    if a < guess:
        print('太高了,在試一次')
        guess = int(input("請猜測數字: "))
        n += 1
    if a > guess:
        print ('太低了,再試一次')
        guess = int(input("請猜測數字: "))
        n += 1
if a == guess:
     print ('恭喜！你猜對了')
     print("試了",int(n),"次")
    