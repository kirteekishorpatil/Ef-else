number=int(input("enter the number"))
a=number%10;
b=(number//10)%10;
c=(number//10)//10;
d=a+b+c
if number%d==0:
        print(number,"it is harshad number")
else:
        print(number,"it is not harshad number")