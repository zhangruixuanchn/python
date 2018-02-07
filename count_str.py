#!/usr/bin/env python3

def char_count(str):
    char_list = set(str)
    for a in char_list:
        print(a,str.count(a))


if __name__ == '__main__':

    myword  = input("Enter a string")

    char_count(myword)

