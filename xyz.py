#!/usr/bin/env python3

def connect(a,b):
    print("IP:",a)
    print("Ports:",b)

    a  = '10.10.10.1'
    b.append(8080)

if __name__=="__main__":
    ipaddress = '192.168.1.1'
    ports = [22,23,24]
    print("Before connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)
    print("In connect:")
    connect(ipaddress, ports)
    print("After connect:")
    print("IP: ", ipaddress)
    print("Ports: ", ports)

