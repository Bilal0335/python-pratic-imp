size = input("What size pizza you want(S/M/L)? ")
bill = 0

if size == 'S' or size == 's':
               bill+= 100
               print(f"Small Pizza price is 100 Rs.")
elif size == 'M' or size == 'm':
               bill+= 200
               print(f"Medium Pizza price is 200 Rs.")
else:
        bill+= 300
        print(f"large Pizza price is 300 Rs.")

add_pepperoni = input("Do you want paperoni(Y/N)? ")
if add_pepperoni == "Y" or add_pepperoni == "y":
        if size == 'S' or size == 's':
               bill+= 30
        else:
                bill+=50

extra_cheese = input("Do you want extra cheese(Y/N)? ")
if extra_cheese == "y" or extra_cheese == "Y":
        bill+= 20
print(f"You Final Bill is : {bill}")
