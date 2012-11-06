def main():

  i = 1
  j = 2
  n = 0
  while j < 4000000:
    if (j % 2 ==0): n += j
    x = j
    j += i
    i = x

  print(n)


main()
