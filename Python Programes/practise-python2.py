# Part 1 =  Calculate the factorial of a given number
# Part 2 = Find the number of trailing zeroes in the factorial
"""
Trailing zeroes means how many zeroes are there in the factorial of a number - If we do the prime factorisation of the factorial we will find that jitne 5 honge uske factorisationmein utne hi zeroes honge kyuki har dusre number mein 2 to milega hi milega
"""

# 7 = 7*6*5*4*3*2*1 =

def factorial(n):
    if n==0 or n==1:
        return 1
    if n>1:
        return n * factorial(n-1)

def TrailingZeroesFactorial(n):
    """
    This program is not useful because computer is not able to generate factorial of big numbers


     fac = factorial(n)
     print(fac)
     count = 0
     while(fac%10 == 0):
         count = count + 1
         fac = fac/10
     return count
    """
    i = 5
    count = 0
    while(n//i  != 0 ):
        count += n//i
        i = i*5
    return count




if __name__ == '__main__':
    num1 = int(input("Enter the number:\n"))
    try:
        fac = factorial(num1)
        print(f"Factorial of {num1} is {fac}")# It will not be handle big numbers
        print(f"Factorial Trailing Zeroes of {num1} is {TrailingZeroesFactorial(num1)}")
    except Exception as e:
        print(f"Factorial Trailing Zeroes of {num1} is {TrailingZeroesFactorial(num1)}")

    """ Bade numbers ka factorial nhi niklega but uske trailing zeroes niklenge"""