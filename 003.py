import math
def main():

  n = 600851475143
  m = math.ceil(math.sqrt(n)) # ~ sqrt(n)

  l = [0]*m

  lf = 1 # largest factor 

  # solution by sieve of eratosthenes
  for i in range(2,len(l)):
    if l[i] == 0:
      #print(i,"is prime!")

      if (n % i == 0): 
        print(i,"is a factor of m!")
        lf = i

      j = 1
      while i*j < len(l):
        l[i*j] = 1
        j += 1 


  print("Largest prime factor of",n,"is",lf,".")

main()
