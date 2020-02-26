# 사용자 함수2

def get_input_user(msg, casting):
    '''사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 리턴합니다.

    Args:
        msg(str) : input 시 출력할 문구
        casting(class): 사용자에게 입력 받은 값의 자료형

    Returns:
        user (casting-value): 사용자에게 입력받은 값
    '''
    # casting=int로 설정하면 호출시 int생략 가능
    while True:
        try:
            user = casting(input(msg))
            return user
        except:
            continue

def is_prime_number(num):
    prime_lists = [False, False] + [True]*(num-1)
    primes = []
    for i in range(2, num + 1):
        if prime_lists[i]:
            for j in range(2*i, num+1, i):
                prime_lists[j]=False
    primes = [i for i in range(2, num+1) if prime_lists[i]==True]

    if num in primes:
        return True
    else:
        return False

num = get_input_user("2 이상의 숫자를 입력하세요>", int)

if is_prime_number(num):
    print("{}는 소수입니다.".format(num))
else:
    print("{}는 소수가 아닙니다.".format(num))

def save_winner(*args):
    print(args)

def save_winner2(**kwargs):
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])

save_winner("가")
save_winner("가", "나")
save_winner("가", "나", "다")

save_winner2(name1="홍길동", name2="가가멜")

def hi():
    print("Hello")

# 함수를 변수에 담을 때는 소괄호 생략
hello = hi
hello()
print(type(hello))

def add(a, b):
    return a+b

def cal(func, a, b):
    print("결과 {}".format(func(a, b)))

cal(add, 1, 5)

# 함수 안에 함수
# closure
def outer_function(func):
    def inner_function(*args, **kwargs):
        print("function name: {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function

f = outer_function(add)
f(10, 20)
