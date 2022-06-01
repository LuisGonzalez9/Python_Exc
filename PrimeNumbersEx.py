# Program to check if a number is prime or not

numberU = int(input("Input your number:"'\n'))

f = False

# Prime numbers need to be greater than 1
if numberU > 1:
    for i in range(2, numberU):
        if (numberU % i) == 0:
            f = True
            break

if f:
    print(numberU, '\n'"This number is not a prime number")
else:
    print(numberU,'\n' "This number is a prime number" )