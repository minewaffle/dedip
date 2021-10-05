#SPONSERED BY DEDPHILE https://discord.gg/8AwF9y4yhP
#Yo, it's waffle, got some cool ideas tell me ;).
import json
import urllib.request
import pyfiglet
from colorama import Fore, Style

print(Style.BRIGHT + Fore.BLUE)
print(pyfiglet.figlet_format("dedip", font="bulbhead"))
print(f"{Fore.MAGENTA}ORG {Fore.GREEN}dedphile {Fore.MAGENTA}BY {Fore.GREEN}minewaffle {Fore.YELLOW}V.1")

while True:
    ipcheck = 0
    print(Style.RESET_ALL + "*" * 30)
    ipp = input(Style.BRIGHT + Fore.BLUE + "Input Ip Address; " + Style.RESET_ALL)
    try:
        url = "https://ipinfo.io/" + ipp
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read()
            data = json.loads(data)
    except:
        print(Fore.RED + "Invalid IP Address" + Style.RESET_ALL)
        ipcheck = 1
    if (ipcheck == 0):
       try:
          print("*" * 30)
          print(Style.BRIGHT + Fore.GREEN + "IP Adress;" + Style.RESET_ALL, data['ip'])
       except:
           print(Style.BRIGHT + Fore.RED + "IP Adress; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "City;" + Style.RESET_ALL, data['city'])
       except:
          print(Style.BRIGHT + Fore.RED + "City; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "State;" + Style.RESET_ALL, data['region'])
       except:
          print(Style.BRIGHT + Fore.RED + "State; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "Country;" + Style.RESET_ALL, data['country'])
       except:
          print(Style.BRIGHT + Fore.RED + "Country; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "GPS;" + Style.RESET_ALL, data['loc'])
       except:
          print(Style.BRIGHT + Fore.RED + "GPS; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "ZIP;" + Style.RESET_ALL, data['postal'])
       except:
          print(Style.BRIGHT + Fore.RED + "ZIP; N/A" + Style.RESET_ALL)
       try:
          print(Style.BRIGHT + Fore.GREEN + "ISP;" + Style.RESET_ALL, data['org'])
       except:
          print(Style.BRIGHT + Fore.RED + "ISP; N/A" + Style.RESET_ALL)
       print("*" * 30)









