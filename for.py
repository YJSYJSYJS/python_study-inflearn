# 반복문 for

# 순차적인 요소를 사용할 때 사용
a = "abcdef"
for i in a:
    print(i)
for i in range(1, 10, 2):
    print(i)

b = ["python","java","c/c++", "c#"]
for i in b:
    print(i)

c = [(1,2),(3,4),(5,6)]
for i in c:
    for j in i:
        print(j)

student = [{"홍길동":100},{"가제트":200},{"가가멜":300}]
for i in student:
    print(i.items())
for i in student:
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("이름: {} 점수: {}".format(name,value))
for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{} 이름: {} 점수: {}".format(s, name,value))

result1 = []
for num in range(1,6):
    result1.append(num+5)
# comprehension 표현 사용
result2 = [num+5 for num in range(1,6)]
print(result2)

result3 = [num + 5 for num in range(1, 10) if num%2==0]
print(result3)

result4 = [num*3 for num in range(1,99) if num%2==0]
print(result4)
# 풀어서 표현
for num in range(1,99):
    if num%2==0:
        result4.append(num*3)

# 구구단
for i in range(2,10):
    for j in range(2,10):
        result = i*j
        print("{} X {} = {}".format(i,j,result))

gugu = ["{} X {} = {}".format(i,j,i*j) for i in range(2,10) for j in range(1, 10)]
print(gugu)