while(True):
    z = int(0)
    n = int(input("Enter the amount :"))
    if(n > 300):
      x = int(n-300)
      y = int(x * 30)
      n = int(n - x)
      z = int(y)
    if(n >= 201):
      x = int(n-200)
      y = int(x * 20)
      n = int(n - x)
      z = int(z + y)
    if(n >= 101):
      x = int(n-100)
      y = int(x * 10)
      n = int(n - x)
      z = int(z + y)
    print(z)