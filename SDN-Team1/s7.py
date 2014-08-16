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
#from mininet.topolib import Mininet
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

def startest( net ):
	print "# Testing IP connectivity.... #"
	#print h1.cmd( 'ping -c3', h1.IP() )
	a = raw_input ("Hit Enter to continue")
#	h1 = net.get( "h1" )
#	h2 = net.get( "h2" )
#	net.iperf()
#	print h1.cmd( 'ping -c3', h1.IP() )


def startfw( h1, inetIntf='eth0', subnet='10.0/8' ):
    localIntf =  h1.defaultIntf()
    h1.cmd( 'iptables -F' )
    h1.cmd( 'iptables -t nat -F' )
    h1.cmd( 'iptables -A INPUT -i', localIntf, '-p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT')
    h1.cmd( 'iptables -A OUTPUT -o', localIntf, '-p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT' )
    h1.cmd( 'iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT' )
    h1.cmd( 'iptables -P INPUT DROP' )
    h1.cmd( 'iptables -P OUTPUT DROP' )
    h1.cmd( 'iptables -P FORWARD DROP' )
    h1.cmd( 'sysctl net.ipv4.ip_forward=1' )

def stopfw( h1 ):
    h1.cmd( 'iptables -F' )
    h1.cmd( 'iptables -t nat -F' )
    h1.cmd( 'sysctl net.ipv4.ip_forward=0' )


if __name__ == "__main__":
	while apptype > 0:
		print '*** Starting network\n'
		net = Mininet()
		net.addController( 'c0' )
		# Create internal LAN switch
		s1 = net.addSwitch( 's1' )
		# Create internal DMZ switch
		s2 = net.addSwitch( 's2' )
		CLI( net )
		net.start()
		while apptype > 0:
			getapptype( apptype )
			if apptype == 1:
				print '*** Adding Host\n'
				h1 = net.addHost( 'h1' )
				h2 = net.addHost( 'h2' )
				print '*** Linking to Switch\n'
				net.addLink( h1, s1 )
				net.addLink( h2, s1 )
				CLI( net )
				startfw ( h1 )
			elif apptype == 2:
				print '*** Adding Host\n'
				h5 = net.addHost( 'h5' )
				h6 = net.addHost( 'h6' )
				h7 = net.addHost( 'h7' )
				print '*** Linking to Switch\n'
				l1 = net.addLink( h5, s1 )
				l2 = net.addLink( h6, s2 )
				l3 = net.addLink( h7, s2 )
				startfw ( h1 )
			startest( net )	
			CLI( net )
		
		print '*** Stopping network'
		stopfw( root )
		net.stop()
