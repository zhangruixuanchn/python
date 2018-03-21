#!/usr/bin/env python3

import sys

def main():
    for arg in sys.argv[1:]:
        try:
            id_str,salary_str = arg.split(':')
            id_ = id_str
            salary = int(salary_str)
            insurance = salary * 0.165
        except:
            print("Parameter Error")
        salary1 = salary - insurance - 3500
    #know the result
        try:
            if salary1 <= 0:
                salary2 = 0
            elif salary1 <= 1500:
                salary2 = salary1*0.03- 0
            elif salary1 <= 4500:
                salary2 = salary1*0.1- 105
            elif salary1 <= 9000:
                salary2 = salary1*0.2 - 555
            elif salary1 <= 35000:
                salary2 = salary1*0.25 - 1005
            elif salary1 <= 55000:
                salary2 = salary1*0.3 - 2755
            elif salary1 <= 80000:
                salary2 = salary1*0.35 - 5505
            else:
                salary2 = salary1*0.45-13505
            print(id_ + ':' + format(salary-insurance-salary2,".2f"))
        except:
            print("what is wrong")

if __name__ == '__main__':
    main()
