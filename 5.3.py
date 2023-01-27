a=int(input("enter the side a"))
b=int(input("enter the side b"))
c=int(input("enter the side c"))

if a+b>c and b+c>a and a+c>b :
    print("the triangle is possible")
    s=(a+b+c)/2                            # semiperimeter
    Area= (s*(s-a)*(s-b)*(s-c))**(1/2)    # Herons formula for finding the area of triangle
    print(Area)
else :
    print("the triangle is not possible")
