def main():

  x = 0

  for i in range(100,1000):

    for j in range(100,1000):

      n = str(i*j)
      if (len(n) % 2 == 0):

        # slice string
        low = n[0:int(len(n)/2):1]
        hi = n[int(len(n)/2):len(n)+1:1]

        # reverse low
        low = low[::-1]

        if hi == low and x < i*j: x = i*j


  print("Largest palindrom:",x)

main()
