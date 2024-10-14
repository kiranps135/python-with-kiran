# print even no only

# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


num = int(input("enter the no as you want=  "))

count = 0

while num <= 100:
    if num % 2 == 0:
        count = count + num
print(count)
