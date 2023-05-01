x=int(input("Enter number :"))
y=int(input("Enter number :"))
z=int(input("Enter number :"))
if x+y>z:
    if x+z>y:
        if z+y>x:
            print(x)
            print(y)
            print(z)
            print("mosalas mishavad")
else:
    print("mosalas nist")