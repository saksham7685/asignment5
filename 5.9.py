lst = []
count = 0
while True:
    x = input("Enter the word: ")
    lst.append(x)
    i = input("Do you want to continue?[Y/N]: ")
    if i.upper() == "N":
        break
len = len(lst)
emp = []
for i in lst:
    if i in emp:
        pass
    else:
        for _ in range(len):
            if i == lst[_]:
                count += 1
                emp.append(i)
        print(f"{i} occurs {count} times")
        count = 0