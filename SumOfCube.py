# Simple Python program to find sum of series 
# with cubes of first n natural numbers 

# Returns the sum of series  
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum


# A formula based Python program to find sum
# of series with cubes of first n natural  numbers

# Returns the sum of series
def sumOfCube(n):
    x = (n * (n + 1) / 2)
    return (int)(x * x)

num=int(input("Enter the number to find sum of cube of n natural numbers: "))
print("Summation is: ",sumOfCube(num))