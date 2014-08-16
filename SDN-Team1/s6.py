#!/usr/bin/python
import os
os.system('clear')
os.system('mn -c')
customer = 'Pi'
servertype = 1
apptype = 1
servicelevel = 1
s1 = '0'
s2 = '0'
#
from mininet.node import Controller
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.topolib import Topolib
from mininet.cli import CLI
from mininet.node import Node
from mininet.log import lg

def header():
	os.system('clear')
	print "     ___         ____    __    ____         _______.   ____    ____  ___   "
	print "    /   \        \   \  /  \  /   /        /       |   \   \  /   / |__ \  "
	print "   /  ^  \        \   \/    \/   /        |   (----`    \   \/   /     ) | "
	print "  /  /_\  \        \            /          \   \         \      /     / /  "
	print " /  _____  \        \    /\    /       .----)   |         \    / __  / /_  "
	print "/__/     \__\        \__/  \__/        |_______/           \__/ (__)|____| "
	print "                                                                           "

def customer():
	header()
	print "###############################"
	print "#                             #"
	print "# Input customer name:        #"
	print "#                             #"
	print "###############################"
	customer = raw_input("Input name: ")
	print 'Selection: %s ' % customer
	print " "
	a = raw_input ("Hit Enter to confirm!")

def servertype():
	header()
	print "###############################"
	print "#                             #"
	print "# Pick server type:           #"
	print "# 1) Apache Web Server        #"
	print "# 2) MySQL Database Server    #"
	print "# 3) App Server               #"
	print "#                             #"
	print "###############################"
	servertype = input("Number selection: ")
	print 'Selection: %s ' % servertype
	print " "
	a = raw_input ("Hit Enter to confirm!")

def getapptype( apptype ):
	header()
	print "###############################"
	print "#                             #"
	print "# Pick App                    #"
	print "# 1) ERP                      #"
	print "# 2) eMail                    #"
	print "#                             #"
	print "###############################"
	apptype = input("Number selection: ")
	print 'Selection: %s ' % apptype
	print " "

def sla():
	header()
	print "###############################"
	print "#                             #"
	print "# Pick service level:         #"
	print "# 1) Gold                     #"
	print "# 2) Silver                   #"
	print "# 3) Bronze                   #"
	print "#                             #"
	print "###############################"
	servicelevel = input("Number selection: ")
	print 'Selection: %s ' % servicelevel
	print " "
	a = raw_input ("Hit Enter to confirm!")

def createapp1( net, s1, s2):
	print '*** Adding Host\n'
	h1 = net.addHost( 'h1' )
	print '*** Linking to Switch\n'
	#s1 = net.Switch( 's1' )
	net.addLink( h1, s1 )

def createapp2( net, s1, s2 ):
	print '*** Adding Host\n'
	h5 = net.addHost( 'h5' )
	h6 = net.addHost( 'h6' )
	h7 = net.addHost( 'h7' )
	print '*** Linking to Switch\n'
	#s1 = net.Switch( 's1' )
	l1 = net.addLink( h5, s1 )
	#s2 = net.Switch( 's2' )
	l2 = net.addLink( h6, s2 )
	l3 = net.addLink( h7, s2 )

def startest( net ):
	print "# Testing IP connectivity.... #"
	#print h1.cmd( 'ping -c3', h1.IP() )
	a = raw_input ("Hit Enter to continue")
#	h1 = net.get( "h1" )
#	h2 = net.get( "h2" )
#	net.iperf()
#	print h1.cmd( 'ping -c3', h1.IP() )

def createnet( net, s1, s2 ):
	net.addController( 'c0' )
	# Create internal LAN switch
	s1 = net.addSwitch( 's1' )
	# Create internal DMZ switch
	s2 = net.addSwitch( 's2' )

def startfw( root, inetIntf='eth0', subnet='10.0/8' ):
    localIntf =  root.defaultIntf()
    root.cmd( 'iptables -F' )
    root.cmd( 'iptables -t nat -F' )
    root.cmd( 'iptables -A INPUT -i', localIntf, '-p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT')
    root.cmd( 'iptables -A OUTPUT -o', localIntf, '-p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT' )
    root.cmd( 'iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT' )
    root.cmd( 'iptables -P INPUT DROP' )
    root.cmd( 'iptables -P OUTPUT DROP' )
    root.cmd( 'iptables -P FORWARD DROP' )
    root.cmd( 'sysctl net.ipv4.ip_forward=1' )

def stopfw( root ):
    root.cmd( 'iptables -F' )
    root.cmd( 'iptables -t nat -F' )
    root.cmd( 'sysctl net.ipv4.ip_forward=0' )


if __name__ == "__main__":
	while apptype > 0:
		print '*** Starting network\n'
		net = Mininet()
		createnet( net, s1, s2 )
		CLI( net )
		net.start()
		while apptype > 0:
			getapptype( apptype )
			CLI( net )
			if apptype == 1:
				createapp1( net, s1, s2 )
				startfw ( root )
			elif apptype == 2:
				createapp2( net, s1, s2 )
				startfw ( root )
			startest( net )	
			CLI( net )
		
		print '*** Stopping network'
		stopfw( root )
		net.stop()
