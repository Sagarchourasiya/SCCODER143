# proogram to reverse a entered num

num = int(input("Enter a number :"))
# to take input from user
temp = num
reverse = 0
while num > 0:
    # this condition will always true
    remainder = num % 10
    # to take last digit of entered number i.e 1234 so 4
    reverse = (reverse * 10) + remainder
    # to reverse 1234 to 4321 [0 * 10  + 4]
    num = num // 10
    
print(reverse) 