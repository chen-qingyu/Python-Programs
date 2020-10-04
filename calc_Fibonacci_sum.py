def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


n = eval(input("Please enter a integer: "))
result = 0

for i in range(1, n + 1):
    result += Fibonacci(n)

print("The sum is ", result)
input()
