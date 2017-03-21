#!/usr/bin/env python

ip_addr = raw_input("enter ip address:")

octets = ip_addr.split(".")

print "{:<12}{:<12}{:<12}{:<12}".format(*octets)

print

".".join(octets)

