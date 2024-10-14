# print all the numbers divisible by 2,3 and 5 from start to end . ask start and end no from user

start = int(input("Enter the start number"))
end = int(input("Enter the start number"))

while start <= end:
    if start % 2 == 0 and start % 3 == 0 and start % 5 == 0:
        print(start)
    start += 1
