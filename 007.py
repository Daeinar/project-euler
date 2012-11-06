import math
def main():

  n = 600851475143
  m = math.ceil(math.sqrt(n)) # ~ sqrt(n)

  l = [0]*m

  lf = 1 # largest factor 
  p = (0,0)
  c = 0

  # solution by sieve of eratosthenes
  for i in range(2,len(l)):
    if l[i] == 0:
      #print(i,"is prime!")
      c += 1
      p = (c,i) 
      if (c == 10001): print(p)

      j = 1
      while i*j < len(l):
        l[i*j] = 1
        j += 1 



main()
