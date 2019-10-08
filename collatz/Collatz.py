# The number we will preform the Collatz operations on.
n=20

#keep looping until we reach 1.
#Note: this assumes the collatz conjecture is true.
while n!=1:
    #Print the current value of n.
    print(n)
    #check if n is even.
    if n % 2 == 0:
        #if n is even, divide by 2.
        n=n//2 #double // removes the dec integer
    else:
        #if n is odd, multiply by 3 and add 1.
        n=(3 * n) + 1

    #Finally, print the 1.
    print (n)