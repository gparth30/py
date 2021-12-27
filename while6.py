#write a program to findout compond interest of given rate, year, amount 


amount=int(input("Enter Your Amount.:"))
rate=float(input("Enter Rate.:"))
prate=rate/100
year=int(input("Enter Year.:"))
ci=(amount*(1+prate)**year)-amount
print(ci)

