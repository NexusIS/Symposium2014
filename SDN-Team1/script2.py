#!/usr/bin/python
import os
os.system('clear')
os.system('mn -c')
os.system('clear')
customer = 'Pi'
servertype = 0
servicelevel = 0
#
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller, RemoteController
#from mininet.topolib import TreeTopo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import lg
from mininet.node import Node
#
print "     ___         ____    __    ____         _______.   ____    ____  ___   "
print "    /   \        \   \  /  \  /   /        /       |   \   \  /   / |__ \  "
print "   /  ^  \        \   \/    \/   /        |   (----`    \   \/   /     ) | "
print "  /  /_\  \        \            /          \   \         \      /     / /  "
print " /  _____  \        \    /\    /       .----)   |         \    / __  / /_  "
print "/__/     \__\        \__/  \__/        |_______/           \__/ (__)|____| "
print "                                                                           "
print "###############################"
print "#                             #"
print "# Input customer name:        #"
print "#                             #"
print "###############################"
customer = raw_input("Input name: ")
print 'Selection: %s ' % customer
print " "
a = raw_input ("Hit Enter to confirm!")
os.system('clear')
#
print "     ___         ____    __    ____         _______.   ____    ____  ___   "
print "    /   \        \   \  /  \  /   /        /       |   \   \  /   / |__ \  "
print "   /  ^  \        \   \/    \/   /        |   (----`    \   \/   /     ) | "
print "  /  /_\  \        \            /          \   \         \      /     / /  "
print " /  _____  \        \    /\    /       .----)   |         \    / __  / /_  "
print "/__/     \__\        \__/  \__/        |_______/           \__/ (__)|____| "
print "                                                                           "
print "###############################"
print "#                             #"
print "# Pick server type:           #"
print "# 1) Apache Web Server        #"
print "# 2) SMTP Server              #"
print "#                             #"
print "###############################"
servertype = input("Number selection: ")
print 'Selection: %s ' % servertype
print " "
a = raw_input ("Hit Enter to confirm!")
os.system('clear')
#
print "     ___         ____    __    ____         _______.   ____    ____  ___   "
print "    /   \        \   \  /  \  /   /        /       |   \   \  /   / |__ \  "
print "   /  ^  \        \   \/    \/   /        |   (----`    \   \/   /     ) | "
print "  /  /_\  \        \            /          \   \         \      /     / /  "
print " /  _____  \        \    /\    /       .----)   |         \    / __  / /_  "
print "/__/     \__\        \__/  \__/        |_______/           \__/ (__)|____| "
print "                                                                           "
print "###############################"
print "#                             #"
print "# Pick service level:         #"
print "# 1) Gold                     #"
print "# 2) Silver                   #"
print "# 3) Bronze                   #"
print "#                             #"
print "###############################"
#
servicelevel = input("Number selection: ")
print 'Selection: %s ' % servicelevel
print " "
a = raw_input ("Hit Enter to confirm!")
os.system('clear')
#
net = Mininet( topo=None, build=False )
c0 = net.addController( 'c0' )
c1 = net.addController('c1' , controller=RemoteController, ip='10.192.34.22')
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
s1 = net.addSwitch( 's1' )
net.addLink( h1, s1 )
net.addLink( h2, s1 )
os.system('clear')

print "##################################"
print "# Creating Application Servers.. #"
print "# Creating Virtual Switch....... #"
print "# Assign IP addressing.......... #"
print "# Testing IP connectivity....... #"
print "##################################"
print " "
net.start()
#CLI( net )
print h1.cmd( 'ping -c2', h2.IP() )
print h2.cmd( 'ping -c2', h1.IP() )
print " "
a = raw_input ("Hit Enter to continue")
print " "
print "###############################"
print "# Bandwidth Test............. #"
print "###############################"
print " "
net.iperf((h1, h2))
print " "
print "###############################"
print "# Test security policy....... #"
print "###############################"
print " "
CLI( net )
#
print "##################################################################"
print "# Applying Firewall Rules and embedded DoS Protection........... #"
print "##################################################################"
#
localIntf = "eth0"

if servertype == 1:
	h1.cmd( 'iptables -F' )
	h1.cmd( 'iptables -t nat -F' )
	h1.cmd( 'iptables -A INPUT -i', localIntf, '-p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT')
	h1.cmd( 'iptables -A OUTPUT -o', localIntf, '-p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT' )
	h1.cmd( 'iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT' )
	h1.cmd( 'iptables -P INPUT DROP' )
	h1.cmd( 'iptables -P OUTPUT DROP' )
	h1.cmd( 'iptables -P FORWARD DROP' )
	h1.cmd( 'sysctl net.ipv4.ip_forward=1' )
elif servertype == 2:
	h1.cmd( 'iptables -F' )
	h1.cmd( 'iptables -t nat -F' )
	h1.cmd( 'iptables -A INPUT -i', localIntf, '-p tcp --dport 25 -m state --state NEW,ESTABLISHED -j ACCEPT')
	h1.cmd( 'iptables -A OUTPUT -o', localIntf, '-p tcp --sport 25 -m state --state ESTABLISHED -j ACCEPT' )
	h1.cmd( 'iptables -A INPUT -p tcp --dport 25 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT' )
	h1.cmd( 'iptables -P INPUT DROP' )
	h1.cmd( 'iptables -P OUTPUT DROP' )
	h1.cmd( 'iptables -P FORWARD DROP' )
	h1.cmd( 'sysctl net.ipv4.ip_forward=1' )

print " "
print "###############################"
print "# Test security policy....... #"
print "###############################"
print " "

a = raw_input ("Hit Enter to complete.")
os.system('clear')
#
net.stop()

#

