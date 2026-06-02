price1=int(input("Enter the price of item1: "))
Qua1=int(input("Enter the quantity of item1: "))
price2=int(input("Enter the price of item2: "))
Qua2=int(input("Enter the quantity of item2: "))
price3=int(input("Enter the price of item3: "))
Qua3=int(input("Enter the quantity of item3: "))
Total=(price1*Qua1)+(price2*Qua2)+(price3*Qua3)
GST=Total*0.18
Bill=Total+GST
print("="*40)
print(f"      grocery bill       ")
print(f"Item1      {price1}    {Qua1}")
print(f"Item2      {price2}    {Qua2}")
print(f"Item3      {price3}    {Qua3}")
print(f"Total             {Total}")
print(f"BILL              {Bill}")
print("="*40)

