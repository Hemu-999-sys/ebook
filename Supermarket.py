#Super Market Bill Generation

Name=input("Enter your name:")

#Displaying the list of items available in the store

lists="""
Rice    Rs 10/kg
Sugar   Rs 8/kg
Oil     RS 30/liter
Salt    Rs 25/kg
Paneer  RS 40/kg
Maggie  Rs 12/pack
Boost   Rs 200/bottle
"""

#intialising variables 
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#Dictionary containing items
items={
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200
}

while True:
    option=input("press 1 for list or 2 to exit:")

    if option=='2':
        print("Thank you for shopping")
        break
    elif option =='1':
        print(lists)
        while True:
            inp1=input("To buy press 1 or press 2 to exit:")
            if inp1 =='2':
                print("Thank you for shopping")
                break
            elif inp1 =='1':
                item=input("choose your items:").lower()
                while True:
                    quantity_input=input("Enter quantity:")
                    if quantity_input.isdigit():
                        quantity= int(quantity_input)
                        break
                    else:
                        print("please enter a valid quantity:")
                if item in items:
                    price= quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("selected item is not available,sorry for the incovenience:")
        if totalprice > 0:
            tax=(totalprice * 10) / 100
            finalamount = tax + totalprice
            print(25 * "=","pythonlife supermarket",25 * "=")
            print(28 * " ","Hyderabad")
            print("Name:", Name, 30 * " ")
            print(75 * "-")
            print("sno",10 * " ",'items',8 * " ",'quantity',8 * " ",'price')
            for i  in range(len(pricelist)):
                print(i+1,13 * " ",ilist[i],8 * " ",qlist[i],8 * " ",plist[i])
                print(75 * " -")
                print(50 * " ",'Total amount:','Rs',totalprice)
                print("Tax amount",50 * " ",'Rs',tax)
                print(75 * "-")
                print(50 * " ", 'final amount:','Rs',finalamount)
                print(75 * "-")
                print(20 * " ", "thank you & visit again")
                print(75 * "-")
                                
                                
                                                
                                        
                        

                                
                                        
                                        

                                    
                                    