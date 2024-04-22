class Canteen:
    items = ["Tea","Coffee","Pepsi","Coke","Snacks"]
    prices = [10,15,40,40,35]
    tot_qty = [100,100,50,50,20]

    def takeorder(self):
        for item in Canteen.items:
            print(f"{item} costs {Canteen.prices[Canteen.items.index(item)]} and we have {Canteen.tot_qty[Canteen.items.index(item)]} quantities left")
        
        order = input("Enter the items you require with the number of items with a space :").split(' ')
        print(order)
        total = 0
        for it in range(0, len(order), 2):
            if(type(order[it]) == type(1)):
                break
            else:
                total = total + (Canteen.prices[Canteen.items.index(order[it])]*int(order[it + 1]))
                Canteen.tot_qty[Canteen.items.index(order[it])]= int(Canteen.tot_qty[Canteen.items.index(order[it])]) - int(order[it + 1])
        print(f"your total bill is {total} rupees")
        for item in Canteen.items:
            print(f"{item} have {Canteen.tot_qty[Canteen.items.index(item)]} quatities left")





Canteen_obj = Canteen()
while(True):
    n = input("DO you want to order ?(Y/N) :")
    if (n == "Y"):
        Canteen_obj.takeorder()
    else:
        print("Then why are you here, get lost!!!")
        break
