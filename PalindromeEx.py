# Program to display if a word is a palindrome or if is not

myStr = input(("Please write a word:" '\n'))
# Making it lower case so it does not create conflicts
myStr = myStr.casefold()

# Comparing each strings with eachother
revStr = reversed(myStr)
if list(myStr) == list(revStr):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")