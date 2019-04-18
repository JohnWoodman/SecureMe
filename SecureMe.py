#!/usr/env python
import subprocess as sub
import sys
import re
from detectVersion import detectVersion
from cronCheck import cronCheck
from fwConf import fwConf,ddosConf
from checkUsers import checkUsers
#from execCommand import execCommand

def main():
	flags = ['--version', '-v', '--cron', '-c', '--firewall', '-f', '--ddos', '-d', '-u', '--user', '--help', '-h']
	arguments = sys.argv[1:len(sys.argv)]
	#print arguments
	for flag in arguments:
		if flag not in flags:
			print("\nusage: sudo python SecureMe.py [-h, --help][-v][-c][-f][-d]\n")
			exit()
	if len(sys.argv) == 1:
		print("Initiating Full Security Configuration")
		detectVersion()
		cronCheck()
		fwConf()
		ddosConf()
	if flags[0] in sys.argv or flags[1] in sys.argv:
		detectVersion()
	if flags[2] in sys.argv or flags[3] in sys.argv:
		cronCheck()
	if flags[4] in sys.argv or flags[5] in sys.argv:
		fwConf()
	if flags[6] in sys.argv or flags[7] in sys.argv:
		ddosConf()
	if flags[8] in sys.argv or flags[9] in sys.argv:
		checkUsers()
	if flags[10] in sys.argv or flags[11] in sys.argv:
		print("\nusage: sudo python SecureMe.py [-h, --help][-v][-c][-f][-d]\n")
		print("Options:")
		print("    -h, --help\t\tDisplay Help Message")
		print("    -c, --cron\t\tCheck/Remove Cronjobs")
		print("    -d, --ddos\t\tConfigure DDoS Protection")
		print("    -f, --firewall\tConfigure Firewall Settings")
		print("    -v, --version\tCheck System Information\n")

if __name__== "__main__":
  main()