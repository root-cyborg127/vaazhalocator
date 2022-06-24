import time
import socket


import py
import requests
import sys

from phonenumbers import carrier 
import phonenumbers

from phonenumbers import timezone


from phonenumbers import geocoder

from rich import *
from rich.progress import track
from time import sleep
import string 
import random
from rich import style
import copy
from rich import print
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Color and Codes
COLORS = { \
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
    "red-background": "\u001b[41m",
    "reset": "\u001b[0m",
}
 

logo = """

                                    $$\                      $$\                           $$\                       
                                    $$ |                     $$ |                          $$ |                      
$$\    $$\$$$$$$\  $$$$$$\ $$$$$$$$\$$$$$$$\  $$$$$$\        $$ |$$$$$$\  $$$$$$$\$$$$$$\$$$$$$\   $$$$$$\  $$$$$$\  
\$$\  $$  \____$$\ \____$$\\____$$  $$  __$$\ \____$$\        $$ $$  __$$\$$  _____\____$$\_$$  _| $$  __$$\$$  __$$\ 
 \$$\$$  /$$$$$$$ |$$$$$$$ | $$$$ _/$$ |  $$ |$$$$$$$ |      $$ $$ /  $$ $$ /     $$$$$$$ |$$ |   $$ /  $$ $$ |  \__|
  \$$$  /$$  __$$ $$  __$$ |$$  _/  $$ |  $$ $$  __$$ |      $$ $$ |  $$ $$ |    $$  __$$ |$$ |$$\$$ |  $$ $$ |      
   \$  / \$$$$$$$ \$$$$$$$ $$$$$$$$\$$ |  $$ \$$$$$$$ |      $$ \$$$$$$  \$$$$$$$\$$$$$$$ |\$$$$  \$$$$$$  $$ |      
    \_/   \_______|\_______\________\__|  \__|\_______|      \__|\______/ \_______\_______| \____/ \______/\__|     
                                                                                                                     
                                                                                                                     """

class ANSI():
     def background(code):
        return "\33[{code}m".format(code=code)
  
     def style_text(code):
        return "\33[{code}m".format(code=code)
  
     def color_text(code):
        return "\33[{code}m".format(code=code)
  
  
example_ansi = ANSI.background(
    97) + ANSI.color_text(35)  + logo
print(example_ansi)                                                                                                         
# print(logo)
print()

dev = ANSI.background(
    97) + ANSI.color_text(35) + ANSI.style_text(4) + "DEVELOPED BY ::  FEARSOME PEOPLE ON PLANET EARTH !  " + "instagram: @vishwajithshaijukumar" 
print(dev)

print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.3)
print('\u001b[32mIPLOCATOR API: Private                 YOUR IP:', IPAddr, '\u001b[0m'), time.sleep(.3)
print('\u001b[33;1mOwner(s): @vishwajithshaijukumar               Last Update: 15.03.2022\u001b[0m'), time.sleep(.3)
print('\u001b[31;1mMaintainer(s): @abinraj_vb      Telegram: milliesgreatfan\u001b[0m'), time.sleep(.3)

print()



print()

print('\u001b[33;1m-----------------------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)
print('\u001b[32m[1]\u001b[0m IPLOCATOR    - Locates any device using PUBLIC IP Address            \u001b[32m[8]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[2]\u001b[0m PHONE-INFO>>>    - INFO GATHERING OF PHONENUMBER [BASIC]             \u001b[32m[9]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[3]\u001b[0m SNEEZ            - Random PASSWD GENERATOR                           \u001b[32m[10]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[4]\u001b[0m Coming Soon🔥                                                        \u001b[32m[11]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[5]\u001b[0m Coming Soon🔥                                                        \u001b[32m[12]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[6]\u001b[0m Coming Soon🔥                                                        \u001b[32m[13]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[32m[7]\u001b[0m Coming Soon🔥                                                        \u001b[32m[X]\u001b[0m Coming Soon🔥'), time.sleep(.1)
print('\u001b[33;1m------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)











# def clear():
#     if os.name == "nt":
#         os.system("cls")
#     else:
#          os.system("clear")

def IPLOC():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] I P    L O C A T O R\u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print()

    
    
    print('\u001b[37m [ϟ] API KEY = b07e65b23f294*************#####\u001b[0m'), time.sleep(.8)

    apiKey = "b07e65b23f2940a49e58c9887005dbd3"
    ip = input("\u001b[30;1m [ϟ] \u001b[37m ENTER IP TO LOCATE ::: \u001b[0m")
 # print(ip) 
    res=requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=b07e65b23f2940a49e58c9887005dbd3&ip='+ ip)
    data=res.json()
 # print(data)
    IP_ADDRESS=data['ip']

    print("\u001b[32m IP ADDRESS :::   "+IP_ADDRESS)
    country=data['country_code3']

    print()



    print("\u001b[36mCOUNTRY:::     "+country)
    print()


    continent=data['continent_name']
    print("\u001b[34;1m CONTINENT :::   "+continent)
    print()


    countryname=data['country_name']
    print("\u001b[31;1m COUNTRY NAME :::  "+countryname)
    print()


    countrycap=data['country_capital']
    print("\u001b[37m COUNTRY CAPITAL :::   "+countrycap)
    print()


    District=data['district']
    print("\u001b[36m DISTRICT :::    "+District)
    print()


    lat=data['latitude']
    print("\u001b[30;1m LATITUDE ::: "+lat)
    print()


    lon=data['longitude']
    print("\u001b[34;1m LONGITUDE ::: "+lon)
    print()


    call=data['calling_code']
    print("\u001b[33;1m CALLING CODE :::  "+call)
    print()


    flg=data['country_flag']
    print("\u001b[35m COUNTRY FLAG ::: \u001b[0m"+flg)
    print()
    
    link=("https://maps.google.com/?q="+lat + "," + str(lon))
    print("\u001b[40m \u001b[37m GOOGLE MAPS LINK ::: \u001b[0m" + link)
    print()

    print("\u001b[33;1m [ϟ] \u001b[46;1m NOTE : -   IF YOU ARE ENTERING THE PUBLIC IP , IT WILL SHOW THE LOCATION OF THE SERVERS [ I S P ] \u001b[0m")
    print()

    support()
    sys.exit()


def PHONELOCATOR():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] P H O N E N U M B E R    I N F O R M A T I O N \u001b[0m'), time.sleep(.1)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print()

    number = input("\u001b[33;1m [ϟ] \u001b[46;1m ENTER PHONE NUMBER TO GET INFO  ::: \u001b[0m")
    print()
    
    
    print(number)




    ch_nmber = phonenumbers.parse(number," CH")
    print(geocoder.description_for_number(ch_nmber,"en"))

    
    service_nmbr = phonenumbers.parse(number,"RO")
    print(carrier.name_for_number(service_nmbr,"en"))

    gb_number = phonenumbers.parse(number,"GB")
    timezone.time_zones_for_number(gb_number)
    print(timezone.time_zones_for_number(gb_number))

    print()
    support()
    sys.exit()
   

def SOON():
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print('\u001b[34;1m [ϟ] C O M I N G   S O O N 🔥 \u001b[0m'), time.sleep(.1)
                                                      
    print ("""    \u001b[30;1m                           
    ___      ___      ___      ___       __       
  ((   ) ) //   ) ) //   ) ) //   ) ) //   ) )    
   \ \    //   / / //   / / //   / / //   / /     
//   ) ) ((___/ / ((___/ / ((___/ / //   / / (||) """)
    print('\u001b[33;1m-------------------------------------------------------------------\u001b[0m'), time.sleep(.1)
    print()
    support()

    sys.exit()
def OPTION_LIST():
    print('\u001b[33;1m-----------------------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)
    print('\u001b[32m[1]\u001b[0m IPLOCATOR    - Locates any device using PUBLIC IP Address            \u001b[32m[8]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[2]\u001b[0m PHONE-INFO>>>    - INFO GATHERING OF PHONENUMBER [BASIC]             \u001b[32m[9]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[3]\u001b[0m SNEEZ            - Random PASSWD GENERATOR                           \u001b[32m[10]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[4]\u001b[0m Coming Soon🔥                                                        \u001b[32m[11]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[5]\u001b[0m Coming Soon🔥                                                        \u001b[32m[12]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[6]\u001b[0m Coming Soon🔥                                                        \u001b[32m[13]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[32m[7]\u001b[0m Coming Soon🔥                                                        \u001b[32m[X]\u001b[0m Coming Soon🔥'), time.sleep(.1)
    print('\u001b[33;1m------------------------------------------------------------------------------------------------------------------------------------------\u001b[0m'), time.sleep(.5)

def support():
  print("\u001b[33;1m-------------------------------------------------------\u001b[0m")
  print("\u001b[32m[1]\u001b[0mϟ S U P P O R T    U S-")
  print("-------------------------------------------------------[[reset]]")
  print("\u001b[32m[1]\u001b[0mIF YOU LOVED OUR WORK, CONSIDER  SUPPORTING.")
  print("\u001b[36m INSTAGRAM:- https://instagram.com/vishwajithshaijukumar ")
  print("\u001b[35mTELEGRAM:- https://telegram.me/milliesgreatfan")
  print("\u001b[33;1m-------------------------------------------------------[[reset]]")

  sys.exit()
    
def banner():

 print(""" [blue]

      ::::::::  ::::    ::: :::::::::: :::::::::: ::::::::: 
    :+:    :+: :+:+:   :+: :+:        :+:             :+:   
   +:+        :+:+:+  +:+ +:+        +:+            +:+     
  +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#      +#+       
        +#+ +#+  +#+#+# +#+        +#+          +#+         
#+#    #+# #+#   #+#+# #+#        #+#         #+#           
########  ###    #### ########## ########## #########       

[/blue]    
""")
 print("""[red] RANDOM PASSWD GENERATOR *[/red]""")
sleep(0.01)


for _ in track(range(100), description='[green]Processing '):







  
    
 alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters_count = list(string.ascii_letters + string.digits + "!@#$%^&*()_")

def generate_random_password():
	
	length = int(input("Enter password length >> "))
	print()

	print("[#9D00FF]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[/#9D00FF]")


	alphabets_count =int(input("Enter alphabets count in password: ")) 
	print()


	print("[#9D00FF]===============================================================================================[/#9D00FF]")
	digits_count = int(input("Enter digits count in password: "))
	print()


	print("[#9D00FF]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[/#9D00FF]")

	special_characters_count = int(input("Enter special characters count in password: "))

	print()


	print("[#9D00FF]==================================================================================================[/#9D00FF]")

	characters_count = alphabets_count + digits_count + special_characters_count

	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

	password = []
	
	
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	for i in range(digits_count):
		password.append(random.choice(digits))


	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	random.shuffle(password)
	print("[#F433FF]YOUR GEN PASSWD IS >>>[/#F433FF]")
	print()



	print()
	
	print("[#00FFFF]""".join(password))
	print()


	print("[#6AFB92]#########################################################################################################[/#6AFB92]")

print("[green][+][/green] [bold magenta]Password generated ![/bold magenta]!", ":white_check_mark:")
print("[#6AFB92]#########################################################################################################[/#6AFB92]")     

sys.exit()





#option selector :-



def Option_Menu():
       OPTION_LIST() 

usrInp = input("\u001b[32m[+]\u001b[0m Enter Input:-") 
    
while True:
     try:  
             
            # If statment for option selection
             if usrInp == "1":
                
                
                IPLOC()
                

             if usrInp == "2":
                
                PHONELOCATOR()
                
             
             if usrInp == "3":
                
                banner()
               
                generate_random_password()
               
                
             if usrInp == "4":
                
                SOON()
               
             if usrInp == "5":
                
               SOON()
                
             
             if usrInp == "6":
                
                SOON()
                
             
             if usrInp == "7":
                
                SOON()
                
             if usrInp == "8":
                
                 SOON()
             if usrInp == "9":
                
                  SOON()
                
             if usrInp == "10":
                 
               
                 SOON()
             if usrInp == "11":
                
                 SOON()
                
             if usrInp == "12":
                
                  SOON()

             if usrInp == "13":
                
                   SOON()

             if usrInp == "X":
                
                  SOON()



             else:
                 
                 
                 Option_Menu()
     except KeyboardInterrupt: 
          break
    

Option_Menu()




    

   


