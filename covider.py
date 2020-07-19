#!/usr/bin/python
import os
import time

class bcolors:
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
if not os.path.isfile("/data/data/com.termux/files/usr/bin/covider"):
	os.system("cp /data/data/com.termux/files/home/covider/covider.py /data/data/com.termux/files/usr/bin/")
	os.system("mv covider.py covider")
	os.system("chmod +x covider")
	print(bcolors.OKGREEN+"You can run this tool from anywhere by typing"+bcolors.PINK+bcolors.BOLD+" covider"+bcolors.ENDC)
	time.sleep(2)
 
if not os.path.isfile("/data/data/com.termux/files/usr/bin/figlet"):
	print(bcolors.WARNING+"installing figlet ..."+bcolors.ENDC)
	os.system("apt-get install figlet -qq > /dev/null")
	print(bcolors.OKGREEN+"Done !"+bcolors.ENDC)

try:
    import requests
except ImportError:
	print(bcolors.WARNING+"installing  requests module...."+bcolors.ENDC)
	os.system("pip -q install requests")
	try :
		import requests
		print(bcolors.OKGREEN+"Done !"+bcolors.ENDC)
	except ImportError:
		print("please install requirements.txt")
		exit()
try:
	from bs4 import BeautifulSoup
except ImportError:
	print(bcolors.WARNING+"installing bs4 module....."+bcolors.ENDC)
	os.system("pip -q install bs4")
	try:
		from bs4 import BeautifulSoup
		print(bcolors.OKGREEN+"Done !"+bcolors.ENDC)
	except ImportError:
		print("please install requirements.txt")

try:
    from covid import Covid
except ImportError:
    print(bcolors.WARNING+"installing covid module..."+bcolors.ENDC)
    os.system("pip -q install covid")
    try:
        from covid import Covid
        print(bcolors.OKGREEN+"Done!"+bcolors.ENDC)
    except ImportError:
        print("please install requirements.txt")



#function state
def state_info():
	os.system("echo -e '\e[1;34m' ")
	os.system("figlet -f big Ratnapal")
	os.system("echo -e '\e[1;32m' ")
	os.system("figlet -f small Hacker ")
	os.system("echo -e '\e[0;m' ")
	print("\n")
	state_name=input(bcolors.BOLD+"Enter state name: ").lower()
	print(bcolors.ENDC+"\n")
	
	
	url = 'https://www.mohfw.gov.in/'
	try:
		soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	except :
		print(bcolors.WARNING+"[ - ]check your internet connection !"+bcolors.ENDC)
		exit()
	
	check=0
	state_list=[]
	for tr in soup.table.select('tr:has(td)'):
	    tds = [td.get_text(strip=True).lower() for td in tr.select('td')]
	    #print(tds)
	    
	    if len(tds) == 6 and tds[0].isnumeric():
	        state_list.append(tds[1].capitalize())
	        check+=1
	        if state_name in tds:
	        	print("_"*43)
	        	print("\n")
	        	print(bcolors.BOLD+'Name of state    :',tds[1].capitalize(),bcolors.ENDC)
	        	print(bcolors.WARNING+'Active cases     :'+bcolors.ENDC, bcolors.BOLD,tds[2],bcolors.ENDC)
	        	print(bcolors.OKGREEN+'Cured/discharged :'+bcolors.ENDC,bcolors.BOLD, tds[3],bcolors.ENDC)
	        	print(bcolors.FAIL+'Deaths           :'+bcolors.ENDC, bcolors.BOLD,tds[4],bcolors.ENDC)
	        	print(bcolors.BOLD+'Total cases      :', tds[5],bcolors.ENDC)
	        	print("\n")
	        	print('_'* 43)
	        	break
	        elif state_name not in tds:
	        	if check==35:
	        		print(bcolors.WARNING+"Input state is wrong !"+bcolors.ENDC)
	        		print("\n")
	        		while True:
	        			print("1) Enter 1 to see the list of states (india) :")
	        			print("2) Enter 2 for exit :")
	        			x=str(input("Enter your choice 1/2 :"))
	        			if x=="1":
	        				for state in state_list:
	        					print(str(state_list.index(state)+1)+") "+(state))
	        				break
	        			elif x=="2":
	        				print("\n")
	        				print(bcolors.BOLD+bcolors.OKGREEN+"Thank you for using us !"+bcolors.ENDC)
	        				print("developed by"+bcolors.OKBLUE+bcolors.BOLD+" Ratnapal Hacker"+bcolors.ENDC)
	        				exit()
	        			else:
	        				print(bcolors.FAIL+"wrong input !"+bcolors.ENDC)
	        				
#country
def country_info():
	try:
	    covid=Covid()
	    countries=covid.list_countries()
	except:
	    print(bcolors.FAIL+"check your internet connection !"+bcolors.ENDC)
	    exit()
	
	print("\n")
	_iput=str(input(bcolors.BOLD+"Enter country name :"+bcolors.ENDC))
	
	#list of countries
	res=[sub['name']for sub in countries]
	res2=sorted(res)
	
	
	#printing country info
	try:
	    cases=covid.get_status_by_country_name(_iput)
	    print("\n")
	    print("_"*43)
	    for x in cases:
	        if x.startswith(('a','d','r','c','t')):
	            print(x,': ',cases[x])
	    print("_"*43)
	    print("\n")
	except ValueError:
	    print(bcolors.WARNING+"[ - ]Invalid country name !"+bcolors.ENDC)
	    _inpt=str(input("Enter 1 to see the list of available cointries :"))
	    if _inpt=="1":
	        for item in res2:
	            print(str(res2.index(item)+1)+") "+item)
	except:
	    print("\n")
	    print(bcolors.FAIL+"Check your internet connection !"+bcolors.ENDC)


os.system("clear")
os.system("echo -e '\e[1;34m' ")
os.system("figlet -f big Ratnapal")
os.system("echo -e '\e[1;32m' ")
os.system("figlet -f small Hacker ")
os.system("echo -e '\e[0;m' ")

print("\n")
print(bcolors.BOLD+"1) Enter 1 to see the details  country vise: ")
print("2) Enter 2 to see the details of states(india)"+bcolors.ENDC)

limit=0
while True:
	user_input=str(input("Enter your choice 1/2 : "))
	os.system("clear")
	if user_input =="1":
		country_info()
		break
	elif user_input=="2":
		state_info()
		break
	else: 
	    print(bcolors.FAIL+"wrong input !"+bcolors.ENDC)
	    limit+=1
	    if limit == 3:
	    	print("Limit reached ! \n"+bcolors.FAIL+"Exiting...."+bcolors.ENDC)
	    	exit()