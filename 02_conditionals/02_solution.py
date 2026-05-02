Age = int(input("Enter your age here:"))
Day = input("Enter your day here:")

if Age >= 18 :
    price = 12
else:
    price = 8    

if Day =="Wednesday":
    price = price - 2

print(price, "$ is the price of your ticket...")    