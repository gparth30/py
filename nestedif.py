#write a program to findout largest trinagle from 3 given triangle's base & height (base * height * 0.5) using nested decision making.

height1=int(input("Enter Height Of triangle1.:"))
base1=int(input("Enter Base Of Triangle1.:"))
height2=int(input("Enter Height Of triangle2.:"))
base2=int(input("Enter Base Of Triangle2.:"))
height3=int(input("Enter Height Of triangle3.:"))
base3=int(input("Enter Base Of Triangle3.:"))

area1=height1*base1*.5
area2=height2*base2*.5
area3=height3*base3*.5
print(f"Area Of First Triangle={area1}")
print(f"Area Of Second Triangle={area2}")
print(f"Area Of Third Triangle={area3}")

if area1>(area2 and area3):
    print("First Triangle Is largest Triangle")
else:
    if area2>(area1 and area3):
        print("Second Triangle Is largest Triangle")
    else:
        print("Third Triangle Is Largest Triangle")