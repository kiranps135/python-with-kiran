# Ask start and end no from user, ask anothe rnumner from user . print all the number from start to end divisible by n.

start = int(input("Enter the start number"))
end = int(input("Enter the start number"))
n = int(input("Enter the start number"))

while start <= end:
    if start % n == 0:
        print(start)
    start += 1
