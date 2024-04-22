def InputFunction():
    n = int(input("Enter the number :"))
    return n
def EvenOddFunction(n):
    if n % 2 == 0 :
        print (f"{n} is even number")
    else :
        print (f"{n} is odd number")
def EvenOddFunctionWithoutModule(n):
    if (n/2) == ((n+1)/2):
        print (f"{n} is odd number")
    else:
        print (f"{n} is even number")
def EvenOddFunctionWithoutModule2(n):
    if (((n-(n/10)*10)*5) - ((((n-(n/10)*10)*5))/10)*10) == 0:
        print (f"{n} is even number")
    else:
        print (f"{n} is even number")

if __name__ == '__main__':
    n = InputFunction()
    EvenOddFunction(n)
    EvenOddFunctionWithoutModule(n)
    EvenOddFunctionWithoutModule2(n)

        
