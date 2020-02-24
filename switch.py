#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import os
import sys



# Just some colors and shit
white = '\x1b[1;97m'
green = '\x1b[1;32m'
red = '\x1b[1;31m'
red = '\x1b[31m'
yellow = '\x1b[1;33m'
end = '\x1b[1;m'
info = '\x1b[1;33m[!]\x1b[1;m'
que =  '\x1b[1;34m[?]\x1b[1;m'
bad = '\x1b[1;31m[-]\x1b[1;m'
good = '\x1b[1;32m[+]\x1b[1;m'
run = '\x1b[1;97m[~]\x1b[1;m'
print ('''%s

██████╗ ██████╗ ██████╗ ██╗  ██╗████████╗████████╗██╗  ██╗ ██████╗██╗  ██╗    ███╗   ██╗ ██████╗     ██╗██████╗ 
██╔══██╗╚════██╗██╔══██╗██║  ██║╚══██╔══╝╚══██╔══╝██║  ██║██╔════╝██║ ██╔╝    ████╗  ██║██╔═══██╗    ██║██╔══██╗
██████╔╝ █████╔╝██║  ██║███████║   ██║      ██║   ███████║██║     █████╔╝     ██╔██╗ ██║██║   ██║    ██║██████╔╝
██╔══██╗ ╚═══██╗██║  ██║╚════██║   ██║      ██║   ╚════██║██║     ██╔═██╗     ██║╚██╗██║██║   ██║    ██║██╔═══╝ 
██║  ██║██████╔╝██████╔╝     ██║   ██║      ██║        ██║╚██████╗██║  ██╗    ██║ ╚████║╚██████╔╝    ██║██║     
╚═╝  ╚═╝╚═════╝ ╚═════╝      ╚═╝   ╚═╝      ╚═╝        ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝ 

      NO IP BANNING SAYS CH405 AND T0X1C
%s''' % (white, white))
print ('''%s

 ██████╗██╗  ██╗██╗  ██╗ ██████╗ ███████╗              ████████╗ ██████╗ ██╗  ██╗ ██╗ ██████╗
██╔════╝██║  ██║██║  ██║██╔═████╗██╔════╝              ╚══██╔══╝██╔═████╗╚██╗██╔╝███║██╔════╝
██║     ███████║███████║██║██╔██║███████╗    █████╗       ██║   ██║██╔██║ ╚███╔╝ ╚██║██║     
██║     ██╔══██║╚════██║████╔╝██║╚════██║    ╚════╝       ██║   ████╔╝██║ ██╔██╗  ██║██║     
╚██████╗██║  ██║     ██║╚██████╔╝███████║                 ██║   ╚██████╔╝██╔╝ ██╗ ██║╚██████╗
 ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝ ╚══════╝                 ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═╝ ╚═════╝

%s''' % (yellow, yellow))
                                                                                                                                                                                                                                                                                                                    

class Torswitch:
	"""This program/script automates the task of changing tor nodes by doing it every few seconds."""
	def __init__(self):
		self.checkOS()
	def checkOS(self):
		if sys.platform == "win32":
			print('Windows is not supported. Sorry.')
			os.system('pause')
			os.system('cls')
			exit()
		elif sys.platform == "win64":
			print('Windows is not supported. Sorry.')
			os.system('pause')
			os.system('cls')
			exit()
		else:
			installCheck = input('Before we continue, have you already installed tor as a service before on Linux? y or n: ')
			if installCheck == "n":
				print('Ok. Then this script will attempt to install it as a service.')
				os.system('sudo apt-get install tor -y')
				os.system('clear')
				return self.Main()
			elif installCheck == "y":
				print('Ok. Then this script wont try to install it if its already on your system as a service.')
				return self.Main()
	def Main(self):
		print('Starting tor service...')
		os.system('service tor start')
		print('Service tor started...')
		while True:
			
			print('Sleeping for 30 seconds before changing nodes.')
			time.sleep(30)
			print('Changing IP...')
			os.system('service tor restart')
			os.system('clear')
Main = Torswitch()
