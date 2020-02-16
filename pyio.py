# 사용자 입력 받기

user = input("사용자 이름을 입력하세요.>")
print(user)

# 숫자를 입력받는 경우 반드시 캐스팅 필요 안할경우 문자열로 취급
num1 = int(input("number1: "))
num2 = int(input("number2: "))
print(num1 + num2)
 
langs = ["Korean", "English"]
for i, l in enumerate(langs, start = 1):
    print("{}. {}".format(i, l))

while True:
    sel = input("select language.> ")
    if not sel.isnumeric():
        continue
    sel = int(sel)
    if 0 < sel < 3:
        break
print("You selected {}.".format(langs[sel-1]))
