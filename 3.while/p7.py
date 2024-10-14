# Ask number from user. Print the multiplication table of the number

num = int(input("Enter the table no want to print = "))

i = 1
while i <= 10:
    print(f"{num} x {1} = {num * i}")
    i += 1
