# Run the fibonacci sequence

nterms = int(input("Enter the number of times:"'\n'))

n1, n2 = 0, 1
count = 0

# check if the inputs is valid
if nterms <= 0:
   print("Please input valid number")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# Print the sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2

       n1 = n2
       n2 = nth
       count += 1