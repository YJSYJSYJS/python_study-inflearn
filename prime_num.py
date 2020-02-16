# 입력한 숫자가 소수인지 확인하기


while True:
    num = input("2 이상의 숫자를 입력하세요.> ")
    if not num.isnumeric():
        continue
    num = int(num)
    if num < 2:
        continue
    break

# 에라토스테네스의 체(sieve of Eratosthenes)
# isprime = True
# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break
# if isprime:
#     print("{} is prime number".format(num))
# else:
#     print("{} is not prime number".format(num))

# 순차적으로 발견되는 소수의 배수들을 미리 제거해서 효율 증가
prime_list = [False, False] + [True] * (num-1)
primes = []

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(2 * i, num + 1, i):
            prime_list[j] = False

primes = [i for i in range(2, num + 1) if prime_list[i]==True]
print(primes)

if num in primes:
    print("{} is prime number".format(num))
else:
    print("{} is not prime number".format(num))



