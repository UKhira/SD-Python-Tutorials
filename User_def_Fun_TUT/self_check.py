def maxOfTwo(n1,n2):
    if (n1 - n2)>0:
        print(n1," is max")
    elif (n1 - n2) == 0:
        print("Numbers are equal")
    else:
        print(n2," is max")

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another number: "))
maxOfTwo(num1,num2);
