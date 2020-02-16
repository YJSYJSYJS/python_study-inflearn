# 반복문: while, for

num = 0
while True:
    print(num)
    num += 1
    if num == 10:
        break
        #while 문을 빠져나감

for i in range(1,1000):
    print(i)
    if i == 10:
        break


for i in range(1,100):
    for j in range(100):
        print(i, j)
        if j == 10:
            break
            # j for문은 탈출하지만 i for문은 불가능

num1 = 0
while num1 < 10:
    num1 += 1
    if num1 == 5:
        continue
        # 루프의 다음 순서로 넘어감
    print(num1)

point = [80, 100, 50, 40, 60]
for p in point:
    if p < 70:
        continue
    print("{}점 입니다.".format(p))

hap = 0
for i in range(1, 100):
    if i%2 == 0:
        continue
    hap += i

print("홀수의 합은 {}".format(hap))

