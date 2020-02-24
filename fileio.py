# 파이썬에서 파일 읽고 쓰기

file = open("sample.txt", mode = "w", encoding = "utf-8")
# utf-8 -> 에디터에서 한글이 안깨진다. 안써도 파일이 깨지지는 않는다. 하지만 utf-8을 사용한 후에 다시 파일을 읽을 때는 똑같이 utf-8을 설정해야한다.
file.write("hello python")
file.close()

# 위에서 저장을 utf-8로 했기 때문에 열 때도 ANSI가 아닌 utf-8로 해줘야 함
rfile = open("sample.txt", mode = "r", encoding = "utf-8")
content = rfile.read()
# read의 소괄호 안에 숫자가 들어가면 그 만큼의 글자만 읽는다.
# 한 줄만 읽고 싶을 때: .readline()
# for l in rfile: print(l) -> print가 readline과 동일한 작용을 한다.
# for문에서 동일한 작용을 하는 이유는 파일포인터의 위치가 초기화되지 않고 계속 이동하기 때문이다.
# rfile.seek(0)으로 파일포인터를 처음위치로 변경할 수 있다.
rfile.close()

print(content)

# ---with문 사용----
# as 뒤가 변수
# with문을 빠져나오면 file이 사라지므로 따로 .close해줄 필요 없다.
with open("sample.txt", mode = "r", encoding = "utf-8") as file:
    print(file.read())

# 두 개의 파일을 다른 형식으로 열어서 동시에 읽고 쓰기를 할 수 있다.
with open("sample.txt", mode = "r", encoding = "utf-8") as s, open("sample2.txt", mode = "w", encoding="utf-8") as t:
    t.write(s.read().replace("python", "파이썬"))
# \를 사용하면 한줄 띄워서 가능
# with open("sample.txt", mode = "r", enconding = "utf-8") as s, \ 
#      open("sample2.txt", mode = "w", encoding="utf-8") as t:


