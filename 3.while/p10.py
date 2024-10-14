# print the following pattern , ask N from user

n = int(input("Enter the num= "))

i = 1
num = 1

while i <= n:
    print(num, end=" ")
    num *= 2
    i += 1
