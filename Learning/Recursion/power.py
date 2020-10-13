def power(x, n):
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)
      
base = int(input("Enter the base number : \n"))
exponential = int(input("Enter the power for the base : \n"))

print(power(base, exponential))