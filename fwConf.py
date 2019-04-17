#!/usr/env python
import subprocess as sub
import sys
import re
from execCommand import execute

#FIREWALL CONFIGURATION

def fwConf():
	option = ""
	exit = 0

	fire_conf = raw_input("\nWould You Like To Set Firewall Rules On Your System? (Y/n) ").lower()
	if fire_conf != "y" and fire_conf != "yes":
		option = "11"

	while (option != "11"):
		print("\n<=========Set Firewall Rules=========>\n")
		print "Which Services/Ports Need To Be Accessed From Outside Your System?"
		print "1) HTTP \t(80)"
		print "2) HTTPS \t(443)"
		print "3) SSH \t\t(22)"
		print "4) Telnet \t(23)"
		print "5) DNS \t\t(53)"
		print "6) FTP \t\t(21)"
		print "7) MySQL \t(3306)"
		print "8) SMTP \t(25)"
		print "9) POP3 \t(110)"
		print "10) Other"
		print "11) Done"

		p_p = ["", ""]

		option = raw_input("Enter Option Number: ")

		if option == "11":
			break

		def switch_options(option):
			switcher = {
				"1": ["80", "tcp"],
				"2": ["443", "tcp"],
				"3": ["22", "tcp"],
				"4": ["23", "tcp"],
				"5": ["53", "udp"],
				"6": ["21", "tcp"],
				"7": ["3306", "tcp"],
				"8": ["25", "tcp"],
				"9": ["110", "tcp"]
			}
			return switcher.get(option, ["Err", "Err"])

		p_p = switch_options(option)

		if option == "10":
			p_p[0] = raw_input("Enter Port Number: ")
			p_p[1] = raw_input("Enter Protocol (tcp or udp): ").lower()

		if p_p[0] == "Err":
			print "Error, Not An Option"

		execute("sudo iptables --policy INPUT DROP")
		execute("sudo iptables --policy OUTPUT ACCEPT")
		execute("sudo iptables --policy FORWARD DROP")
		execute("sudo iptables -A INPUT -p " + p_p[1] + " --dport " + p_p[0] + " -j ACCEPT")
	return

#DDOS CONFIGURATION

def ddosConf():
	ddos_conf = raw_input("\nWould you like to implement DDoS Prevention? (Y/n) ").lower()
	if ddos_conf == "y" or ddos_conf == "yes":
		execute("sudo iptables --new-chain RATE-LIMIT")
		execute("sudo iptables --append INPUT --match conntrack --ctstate NEW --jump RATE-LIMIT")
		execute("sudo iptables --append RATE-LIMIT --match limit --limit 50/sec --limit-burst 20 --jump ACCEPT")
		execute("sudo iptables --append RATE-LIMIT --jump DROP")
	return
