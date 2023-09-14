Name=input("enter your name:")
Roll_no=int(input("enter your register no:"))
course=input("course:")
mark1=int(input("enter TAM mark :"))
mark2=int(input("enter ENG mark :"))
mark3=int(input("enter PHP mark:"))
mark4=int(input("enter CLIENT SERVER mark:"))
mark5=int(input("enter HTML mark:"))
mark6=int(input("enter RDBMS mark:"))
sum=mark1+mark2+mark3+mark4+mark5+mark6;
average=sum/6;
max_value=100;
if(mark1 > mark2 and mark1 >mark3 and mark1>mark4 and mark1>mark5 and mark1>mark6):
  max_value=mark1
elif(mark2>mark3 and mark2>mark4 and mark2>mark5 and mark2>mark6):
  max_value=mark2
elif(mark3>mark4 and mark3>mark5 and mark3>mark6):
  max_value=mark3
elif(mark4>mark5 and mark4>mark6):
  max_value=mark4
elif(mark5>mark6):
  max_value=mark5 
else:
  print(max_value=mark6)
print("Max_marks:",max_value)
min_value=40;
if(mark1 < mark2 and mark1 < mark3 and mark1 < mark4 and mark1 < mark5 and mark1<mark6):
  max_value=mark1
elif(mark2 < mark3 and mark2 < mark4 and mark2 < mark5 and mark2<mark6):
  max_value=mark2
elif(mark3<mark4 and mark3<mark5 and mark3<mark6):
  max_value=mark3
elif(mark4<mark5 and mark4<mark6):
  max_value=mark4
elif(mark5<mark6):
  max_value=mark5 
else:
  print(max_value=mark6)
print("Min_marks:",min_value)
print(average)

