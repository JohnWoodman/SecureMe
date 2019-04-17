#!/usr/env python
import subprocess as sub
import sys
import re
from execCommand import execute

#CRONJOB CHECKING

def cronCheck():
	print "\n<=====Checking Suspicious Cronjobs/Crontabs=====>\n"
	users = execute("cut -f1 -d: /etc/passwd")

	for user in users:
		cronjob = execute("crontab -u " + user + " -l")
		if cronjob[0] != '':
			print "Found Cronjob(s) For " + user + ":"
			for line in cronjob:
				if line:
					if line[0] != '#':
						 print line + "\n"
			delete = raw_input("Would You Like To Delete All Cronjobs For " + user + "? (Y/n)").lower()
			if delete == "y" or delete == "yes":
				execute("crontab -u " + user + " -r")
				print "\nAll Cronjobs Deleted For " + user + "\n"
	return
