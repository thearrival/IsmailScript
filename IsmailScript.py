#!/usr/bin/python
#!/usr/bin/env python


from bs4 import BeautifulSoup
from termcolor import colored
from urllib.request import urlopen
import os
import time
import socket
import datetime








time.sleep(.3)
print(colored("-"*50, "blue"))
print(colored("Starting time... ", "magenta"))
time.sleep(.2)
t =  datetime.datetime.now()
print(t)
print(colored("-"*50, "blue"))

print("")
print("")
time.sleep(.1)
print("                        _______                         ")
time.sleep(.1)
print("                       / .===. \                        ")
time.sleep(.1)
print("                       \/ 6 6 \/                        ")
time.sleep(.1)
print("                       ( \___/ )                        ")
time.sleep(.1)
print("  _________________ooo__\_____/_____________________    ")
time.sleep(.1)
print(" /                                                  \   ")
time.sleep(.1)
print(colored(" |         Hey, Welcome to use IsmailScript!        |   ", "blue"))
time.sleep(.1)
print(" \______________________________ooo_________________/   ")
time.sleep(.1)
print("                       |  |  |                          ")
time.sleep(.1)
print("                       |_ | _|                          ")
time.sleep(.1)
print("                       |  |  |                          ")
time.sleep(.1)
print("                       |__|__|                          ")
time.sleep(.1)
print("                       /-'Y'-\                          ")
time.sleep(.1)
print("                      (__/ \__)                         ")
time.sleep(.1)
print(colored(" By \ ", "white")) 
print(colored("Ismail Ahmed", "red"))
print(colored("V 1.1.0", "red"))


print(colored("-" * 50, "blue"))


# make a connection between server and host to grab more details

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = str(input(colored("Enter the target website :" , "yellow")))
port = 80


server_ip = socket.gethostbyname(server)
print(colored("Website IP address :" , "yellow"))
print(colored( server_ip , "green"))

print(colored("-"*50, "blue"))

socket.setdefaulttimeout(2)
request = "GET / HTTP/1.1\r\nHost: " + server_ip + "\r\n\r\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(2048)

print(colored("Banner Grabbing ... ","yellow"))
print(result)

s.close()
print(colored("-"*50, "blue"))





# start Reconnaissance!


# DNS server information

print(colored("Show DNS server info... " , "yellow"))
print(os.system("%s %s %s" % ("dig " , server_ip , " ANY")))
print(colored("-"*50, "blue"))



# DNS Zone Transfer

print(colored("Dicover DNS Zone Transfer /","yellow"))
print(os.system("%s %s" % ("nslookup ", server_ip)))
print(colored("-"*50, "blue"))



# Scrapping all URLs of any website

print(colored("Scrapping all URLs of the website... ","yellow"))
print(colored("example...","white"))
print(colored("https://www.ismail.com","white"))

html = urlopen(input("Input the URL of the Website: "))

beautiful = BeautifulSoup(html.read());

for link in beautiful.find_all('a'):
    print(link.get('href'))

print(colored("-"*50, "blue"))


# Whois information

print(colored("Whois information...","yellow"))
print(os.system("%s %s " % ("whois " , server_ip )))
print(colored("-"*50, "blue"))



# Scan network ports and service

print(colored(" Scan Website Network Ports and Services... ","yellow"))
print(os.system("%s %s" % ("nmap -sV -sC -A -p 21-1450" , server_ip )))
print(colored("-"*50, "blue"))



# Thanks for reading the code ^_^
# Don't be hesitate if you have any questions ! 
# esmail19980@gmail.com

