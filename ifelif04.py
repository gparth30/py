#write a program to findout whether donor can give blood to beneficiery or not based upon blood group of both person as per below criteria

print("Enter Your Height(only In Foot & Inch)")

foot=int(input("Enter Your Height In Foot.:"))
inch=int(input("Enter Your Height In Inch.:"))

total_height=foot*12+inch
print("Height=",total_height)
weight=float(input("Enter Your Weight.:"))
print("Weight=",weight)
meter=total_height/39.37
bmi=weight/(meter*meter)
print("Your BMI Is=",bmi)

if bmi>=40:
    print("Obese Type |||")
elif bmi>=35.0:
    print("Obese Type ||")
elif bmi>=30.0:
    print("Obese Type |")
elif bmi>=25.0:
    print("Over Weight")
elif bmi>18.5:
    print("Normal Weight")
else:
     bmi<18
     print("Under Weight")


