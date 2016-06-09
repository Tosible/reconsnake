#!/usr/bin/python
# Copyright (c) Cameron Poe 2016


# important modules/libraries here
import os
from re import search
import socket
import sys
try:
    from termcolor import colored
except ImportError:
    print(colored(str("Termcolor library not found! Closing..."), 'red'))
    sys.exit()
try:
    import whois
except ImportError:
    print(colored(str("No whois! Closing..."), 'red'))
    sys.exit()


def ipv4address():
    try:
        host = sys.argv[1]
        ip = socket.gethostbyname(host)
        print(colored(str("[+] "), 'cyan') + colored(str("IPV4 address: "), 'white') + ip)
    except socket.error as msg:
        print(colored(str("Socket Error! No Connection"), 'red'))
        sys.exit(1)
    except NameError:
        print("You must specify a domain!")
        print("Usage: " + sys.argv[0] + " <domain>")
    except IndexError:
        print("You must specify a domain!")
        print("Usage: " + sys.argv[0] + " <domain>")


def who():
    try:
        host = sys.argv[1]
        str(host)
        w = whois.whois(host)
        w.expiration_date
        w.text
        print(colored(str("Whois Information: \n"), 'yellow'))
        print(w)
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()


def ipv6address():
    try:
        host = sys.argv[1]
        ip = socket.getaddrinfo(host, None, socket.AF_INET6)
        print(colored(str("[+] "), 'cyan') + colored(str("IPV6 address: "), 'white') + str(ip))
    except socket.gaierror, err:
        print(colored(str("Error or no IPV6 address found! \n"), 'red'))
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()


def url():
    try:
        host = sys.argv[1]
        if host.startswith('http') or host.startswith('https'):
            m = search('https?\://([^/]*)/?.*', host)
            host = m.group(1)
        else:
            pass
        print(colored(str("[+] "), 'cyan') + colored(str("URL: "), 'white') + "http(s)://" + host + "/")
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()


def domain():
    try:
        domain = sys.argv[1]
        if domain.startswith('http') or domain.startswith('https'):
            m = search('https?\://([^/]*)/?.*', domain)
            domain = m.group(1)
        else:
            pass
        print(colored(str("[+] "), 'cyan') + colored(str("Domain: "), 'white') + domain)
    except NameError:
        sys.exit()
    except IndexError:
        sys.exit()


def main():
    # banner
    print(colored(str("""
    +-+-+-+-+-+-+-+-+-+-+
    |R|e|c|o|n|S|n|a|k|e|
    +-+-+-+-+-+-+-+-+-+-+ \n"""), 'green'))
    domain()
    url()
    ipv4address()
    ipv6address()
    who()


# execution
if __name__ == "__main__":
    if sys.platform == 'win32' or sys.platform == 'win64':
        os.system('cls')
        main()
    else:
        os.system('clear')
        main()
