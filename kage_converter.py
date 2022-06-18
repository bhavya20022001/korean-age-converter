age=int(input("Enter your international age :"))
bday_passed=int(input("Birthday passed -1 or Birthday not passed -0 = "))
if bday_passed:
    kage=age+1
else:
    kage=age+2
print("Your Korean age is : ",kage)