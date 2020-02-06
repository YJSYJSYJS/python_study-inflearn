
# 현재 시간이 12~13 점심을 먹고 15~16 or 아프면 휴식

time = 12
sick = True

if 12 <= time < 13 and not sick: print("lunch time")
elif 15 <= time < 16 or sick: print("break time")
else: print("work time")

a=10
if a>10:
    ret=100
else:
    ret=500

ret=100 if a>10 else 500

a=10
if a>10:
    ret=100
elif a==10:
    ret=200
else:
    ret=500

ret={a>10: 100, a<10: 500}.get(True, 200)
# {}안에 True인게 있으면 그게 실행되고, 안에 True가 없으면 get의 기본값으로 들어감

name = "abcde"
if 'a' in name:
    print("있음")
else:
    print("없음")

name = ["홍길동", "가가멜", "가제트"]
if "가제트" in name:
    print("있음")
else:
    print("없음")
if "홍길동" not in name:
    print("없음")
else:
    print("있음")

