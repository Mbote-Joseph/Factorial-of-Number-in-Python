num=int(input("Enter the number : "))
fact=1
if num<0:
    print("There are no factorials for negative numbers")
elif num==0:
    print(f"The factoria of 0 is : {fact}")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of {} is {}".format(num,fact))
