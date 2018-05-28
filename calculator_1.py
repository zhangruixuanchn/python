#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])

except:
    print("Parameter Error")

salary1 =salary-3500

#know the result
 
try:
    if salary1 <= 1500:
        salary2 = salary1*0.03- 0

    elif 1500 < salary1 <= 4500:
        salary2 = salary1*0.1- 105

    elif 4500 < salary1 <= 9000:
        salary2 = salary1*0.2 - 555

    elif 9000 < salary1 <= 35000:
        salary2 = salary1*0.25 - 1005

    elif 35000 < salary1 <= 55000:
        salary2 = salary1*0.3 - 2755

    elif 55000 < salary1 <= 80000:
        salary2 = salary1*0.35 - 5505
    else:
        salary2 = salary1*0.45-13505

    print(format(salary2,".2f"))


except:
    print("what is wrong")









  
