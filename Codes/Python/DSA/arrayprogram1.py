import array as arr
a=arr.array('i',[])
print("array was declared...  ",a)
while(True):
    ans = input("Do you want to perform any operation on the array(Y/N):")
    if(ans == "Y"):
        x = input("Type(append/insert(number_Location)/pop(pop_no.of pops_side value LEFT/RIGHT)/remove/display)(space seperated) :").split(' ')
        match x[0]:
            case "append":
                for i in range (1,len(x)):
                    a.append(int(x[i]))
                print("Updated array :",a)
            case "insert":
                for i in range (1,len(x),2):
                    a.insert(int(x[i]),int(x[i+1]))
                print("Updated array :",a)
            case "pop":
                for i in range (0,int(x[1])):
                    if(x[2]=="LEFT"):
                        a.remove(int(a[0]))
                    elif(x[2]=="RIGHT"):
                        a.pop()
                    else:
                        a.pop()
                print(f"last {int(x[1])} elements were poped")
                print("Updated array :",a)
            case "remove":
                for i in range (1,len(x)):
                    a.remove(int(x[i]))
                print("Updated array :",a)
            case "display":
                print(a)
    else:
        break
            
