# 유니코드(전 세계의 모든 문자를 1:1로 매칭하는 코드 표)와 인코딩(유니코드를 저장하는 방식)
# utf-8로 저장된 파일은 에디터에서도 문제없이 읽는다.

file = open("utf8.txt", mode="r", encoding = "utf-8")
print(file.read())
file.close()

file1 = open("utf8.txt", mode="rb")
# mode = rb 일경우 바이너리파일로 읽는 것이기 때문에 인코딩이 따로 필요없다.
# 하지만 바이너리 값 말고 제대로 된 값을 읽어오기 위해서는 따로 디코딩이 필요하다
print(file1.read().decode("utf-8"))
file1.close()