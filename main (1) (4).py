# factorial using recursion
def factorial_rec(n):
   if n==0 or n==1:
     return 1
   else:
     return n*factorial_rec(n-1)

number =int(input("Enter a value :"))
res = factorial_rec(number)

print("The factorial of {} is {}.".format(number,res))