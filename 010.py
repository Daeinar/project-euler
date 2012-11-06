import math
def main():

  m = 2000000 

  l = [0]*m

  c = 0 # sum of all primes below two million

  # solution by sieve of eratosthenes
  for i in range(2,len(l)):
    if l[i] == 0:
      #print(i,"is prime!")
      c += i

      j = 1
      while i*j < len(l):
        l[i*j] = 1
        j += 1 

  print(c)

main()
