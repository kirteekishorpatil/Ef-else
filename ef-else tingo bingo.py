print("navgurukul")
num=int(input("enter the num"))
if num>=200:
      print("the number is bingo")  
      if num%2==0:
            print("number is evan")
      else:
            print("number is odd ")
elif num<200:
      print("number is tingo")
      if num%2==0:
            print("number is evan")
      else:
            print("number is odd")         
else:
      print("error")