name=input("Enter name:")
family=input("Enter family :")
ryazi=int(input("number ryazi:"))
hasabdari=int(input("number hasabdari:"))
modirit=int(input("number modirit :"))

x=ryazi+hasabdari+modirit
avrage=x/3

print(avrage)

if avrage>=17:
    print("great")
if 12<=avrage<17:
    print("normal")
if avrage<12:
    print("fail")


print("my nema is ", name,"family", family,"average", avrage,) 