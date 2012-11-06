def main():

  a = 0
  b = 0
  c = 0

  n = 500

  for c in range(1,n): 
    for b in range(1,c):
      for a in range(1,b):

        if a*a + b*b == c*c: 
          #print("a =",a,"b =",b,"c =",c,":",a*a,"+",b*b,"=",c*c)
          if a+b+c == 1000: print(a,"*",b,"*",c,"=",a*b*c)

main()
