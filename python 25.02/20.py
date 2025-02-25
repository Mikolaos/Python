import math
a=1
b=1
c=1
if a==0:
     print("to nie jest f kwadratowa")
else:
    delta=b**2-4*a*c
    print(delta)
    if delta>0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print(x1, x2)
    elif delta==0:
        x0=-b/(2*a)
        print(x0)
    else:
        print("Brak miejsc zerowych")
