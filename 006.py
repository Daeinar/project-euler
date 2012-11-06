import math
def main():

  x = 0 
  y = 0
  for i in range(1,101):
    x += math.pow(i,2)
    y += i

  y = math.pow(y,2)
  print(y-x)

main()


