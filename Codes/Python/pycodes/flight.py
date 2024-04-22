while(True):
    m = int(input("Enter the seat number :"))
    if(m > 72 or m < 1):
        print("Waiting...")
        break
    n = m % 8
    if(n == 1 or n == 4):
        print(f"assign LB to seat {m}")
    elif(n == 2 or n == 5):
        print(f"assign MB to seat {m}")
    elif(n == 3 or n == 6):
        print(f"assign UB to seat {m}")
    elif(n == 7):
        print(f"assign SL to seat {m}")
    elif(n == 0):
        print(f"assign SU to seat {m}")
