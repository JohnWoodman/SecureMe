#!/usr/env python
import subprocess as sub
import sys
import re
from execCommand import execute

#GET SYSTEM INFO
#Need: OS, network info, super users, etc.

def detectVersion():
	print("\n<========Getting System Info========>\n")
	version = execute("cat /etc/issue")
	priv_ip = execute("hostname -I | cut -d' ' -f1")
	ifconfig = execute("ifconfig | grep " + priv_ip[0])[0].split(" ")
	mask = ifconfig[ifconfig.index('netmask') + 1]
	broad = ifconfig[ifconfig.index('broadcast') + 1]
	pub_ip = execute("curl ifconfig.me")
	sudoers = execute("grep '^sudo:.*$' /etc/group | cut -d: -f4")
	print "Operating System:"
	print version[0] + "\n"
	print "Private IP Address:"
	print priv_ip[0] + "\n"
	print "Network Mask:"
	print mask + "\n"
	print "Broadcast Address:"
	print broad + "\n"
	print "Public IP Address:"
	print pub_ip[0] + "\n"
	print "Sudo Users:"
	print sudoers[0]
	return






