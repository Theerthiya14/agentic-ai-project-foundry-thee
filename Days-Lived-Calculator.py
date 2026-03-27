from datetime import datetime
a=input("ENTER DATE IN YYYY-MM-DD:")
b=input("ENTER DATE IN YYYY-MM-DD:")
a1=datetime.strptime(a,"%Y-%m-%d")
b1=datetime.strptime(b,"%Y-%m-%d")
print("NUMBER OF DAYS LIVED:",b1-a1)