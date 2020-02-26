# 사용자 함수

def 함수명():
    print("함수호출")
    return True

a = 함수명()

def add(a,b):
    return a+b

c = 10
def add2(a,b):
    c = a+b
    # 지역변수의 개념
    return c


b = add(1,10)
print(b, c)

d = 20
def add3(a,b):
    global d
    # 전역 번수를 사용할 때 global 사용
    d = a+b
    return d
    
r = add3(1,1)
print(r,d)
