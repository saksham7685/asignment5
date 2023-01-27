i=0
lis=[]
while i < 10:
    no = int(input("Enter the No: "))
    lis.append(no)
    i += 1
print(lis)

for n in lis:
    if n > 0:
        print(n, "is a positive integer")
    elif n < 0:
        print(n, "is a negative integer")
    elif n % 2 == 0:
        print(n, "is an even integer")
    elif n % 2 != 0:
        print(n, "is an odd integer")
set = set(lis)
for i in set:
    print(i, "occurs", lis.count(i), "times")
