# 내장 함수
# = 파이썬에서 제공하는 여러 기능들(class, )도 포함

a=0.1+0.2
print(a)

#모두 참이여야 참
t = all([True,True])
f = all([0,1])
print(t)
print(f)

# 하나만 참이여도 참
an = any([0,0])
an2 = any([1,0])

# 유니코드를 통해 숫자를 캐릭터로
ch1 = chr(97)
ch2 = chr(44032)
or1 = ord('가')
or2 = ord('a')
print

# 진수 변환
b1 = bin(44032)
b2 = bin(10)
o1 = oct(44032)
o2 = oct(10)
h1 = hex(44032)
h2 = hex(10)

# 자료형 확인
ex = 10
isinstance(ex, int)
isinstance(ex, str)

# 반올림
ex1 = 1/3
round(ex1)
# 소수 몇번째까지 반올림인지 설정 가능
round(ex1,3)
