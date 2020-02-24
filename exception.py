# 파이썬 예외 처리 try / except

# # try 안에 오류가 발생할 수 있는 코드를 입력
# try:
#     idx = []
#     idx[0]=100
# # Exception이 모든 error를 포괄함 생략해서 except: 만 써도 가능
# # 하지만 코드의 양이 많을 때 어떤 에러가 발생했는지 아는 것이 더 좋을 때가 있고, try except를 남용하면 혼란을 야기
# except:
#     pass

# print("OK")

try:
    file = open("sample.txt", "r")
    n="10.5"
    v=int(n)
except:
    print("error")
# 오류가 발생하지 않으면 else로 들어감
else:
    print("OK")
# 오류 발생의 여부에 관계 없어 항상 들어감, 대표적으로 file.close()가 들어간다.
finally:
    file.close()
    print("Always print")