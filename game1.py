import random

sign1=['rock','paper','cizer']
print(sign1)

any_one_sign1=random.sample(sign1, k=1)
print(any_one_sign1)


sign2=['rock','paper','cizer']
print(sign2)

any_one_sign2=random.sample(sign2, k=1)
print(any_one_sign2)

print(any_one_sign1+any_one_sign2)

if any_one_sign1==any_one_sign2:
    print("Desiciom Is Tie")
elif any_one_sign1+any_one_sign2==['rock','paper']:
    print("Person2 Is Winner")
elif any_one_sign1+any_one_sign2==['paper','rock']:
    print("Person1 is Winner")
elif any_one_sign1+any_one_sign2==['rock','cizer']:
    print("Person1 Is Winner")
elif any_one_sign1+any_one_sign2==['cizer','rock']:
    print("Person2 Is Winner")    
elif any_one_sign1+any_one_sign2==['paper','cizer']:
    print("Person2 Is Winner")
elif any_one_sign1+any_one_sign2==['cizer','paper']:
    print("Person1 Is Winner")
else:
    print("DON'T CHEATING")