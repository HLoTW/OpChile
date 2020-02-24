import time,os
p=input('\033[92mTIME BEFORE SWITCHING:\n>')
os.system('service tor start')
while True:
 print'Sleeping for',p,'seconds before switching...'
 time.sleep(p)
 os.system('service tor restart')
 os.system('clear')