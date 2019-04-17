#!/usr/env python
import subprocess as sub
import sys
import re

#Execute given command
def execute(cmd):
	out, error = sub.Popen([cmd], stdout=sub.PIPE, stderr=sub.PIPE, shell=True).communicate()
	results = out.split('\n')
	if error and cmd.split(' ')[0] != "curl" and cmd.split(' ')[0] != "crontab":
		print "\n********ERROR********\n"
		print error
		print "*********************\n"
		sys.exit()
	return results