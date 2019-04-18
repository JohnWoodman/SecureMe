#!/usr/env python
import subprocess as sub
import sys
import re
from execCommand import execute

def checkUsers():
	print("Checking user permissions")
	passwd = execute("cat /etc/passwd")
	print("\nList of users with root privileges\n")
	for user in passwd:
		privilege = user.split(":")[2:4]
		if '0' in privilege:
			print user
	print("\nList of users with shell access\n")
	for user in passwd:
		shell = user.split(":")
		shell = shell[len(shell)-1:]
		if shell[0] == '/bin/bash' or shell[0] == '/bin/sh':
			print user
