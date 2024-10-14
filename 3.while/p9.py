# count the no of odd or even no from start to end . ask start and end no from user

start = int(input("Enter the start number"))
end = int(input("Enter the start number"))

odd_count = 0
even_count = 0

while start <= end:
    if start % 2 == 0:
        odd_count += 1
    else:
        even_count += 1
    start += 1
print(odd_count)
print(even_count)
