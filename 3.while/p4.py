# ask for the start and end no from user. calculate the total sum of all the numbers from start to end

start = int(input("Enter the start number"))
end = int(input("Enter the start number"))

total_sum = 0

while start <= end:
    total_sum = total_sum + start
    start += 1
print(total_sum)
