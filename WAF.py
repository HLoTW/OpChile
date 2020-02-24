#Script by : Ala Chamtouri
import urllib
sq=['union','select','concat','group','order','by','from','where','and','or','not','/*','/*!']
k='%3C%5C'
while True:
 p=raw_input('\n\033[92mPayload:\n')
 x=0
 q=''
 h= urllib.unquote(p).decode('utf8')
 for i in h:
   q+=i.lower()
 q= q.replace(" ", "")
 for o in sq:
   if (('=-' in q) or (('=-' in q) and (((o and '+') in q)) or (o and '+') in q)) or (('-='  in q) or (('-=' in q) and (((o and '+') in q)) or (o and '+') in q)):
    x+=1
 if (('<' and ('>' or ';>' or '=' or '/)' or ')')) in q) or (('<' and '>') and ('<' and urllib.unquote(k).decode('utf8')) in q) or (('<' and '>') and ('<' and '/>') in q):
  x+=1
 if x>0:
  print'\n\033[91m[-]Nice try skid!!! xD'
 else:
  print'\n\033[94m[+]You passed!!!'