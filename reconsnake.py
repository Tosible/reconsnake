#!/usr/bin/python
# Copyright (c) Cameron Poe 2016

import socket, sys, whois

print """
+-+-+-+-+-+-+-+-+-+-+
|R|e|c|o|n|S|n|a|k|e|
+-+-+-+-+-+-+-+-+-+-+ \n"""
def ipv4address():
    try:
        host = sys.argv[1]
        ip = socket.gethostbyname(host)
        print "IPV4 address: " + ip
    except socket.error as msg:
        print "Socket Error! No Connection"
        sys.exit(1)
    except NameError:
        print "You must specify a domain!"
        print "Usage: " + sys.argv[0] + " <domain>"
    except IndexError:
        print "You must specify a domain!"
        print "Usage: " + sys.argv[0] + " <domain>"
def who():
    try:
        host = sys.argv[1]
        str(host)
        w = whois.whois(host)
        w.expiration_date
        w.text
        print "Whois Information: \n"
        print w
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()
def ipv6address():
    try:
        host = sys.argv[1]
        ip = socket.getaddrinfo(host, None, socket.AF_INET6)
        print "IPV6 address: " + str(ip)
    except socket.gaierror, err:
        print "Error or no IPV6 address found! \n"
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()
def url():
    try:
        host = sys.argv[1]
        print "URL: http://" + host + "/"
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()

def domain():
    try:
        domain = sys.argv[1]
        print "Domain: " + domain
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()

def main():
    domain()
    url()
    ipv4address()
    ipv6address()
    who()
main()
