#!/usr/bin/python
import os
os.system('clear')
customer = 'Pi'
servertype = 1
apptype = 1
servicelevel = 1
#
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

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

def getapptype():
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

def createapp1():
	net = Mininet()
	print '*** Adding Host\n'
	h1 = net.addHost( 'h1' )
	print '*** Linking to Switch\n'
	net.addLink( h1, s1 )

def createapp2():
	net = Mininet()
	print '*** Adding Host\n'
	h1 = net.addHost( 'h1' )
	h1 = net.addHost( 'h2' )
	print '*** Linking to Switch\n'
	net.addLink( h1, s1 )
	net.addLink( h2, s2 )

def startest():
	net.start()
	print "# Testing IP connectivity.... #"
	print h1.cmd( 'ping -c3', h1.IP() )
	
	a = raw_input ("Hit Enter to continue")

def createnet():
	net.addController( 'c0' )
	# Create internal LAN switch
	s1 = net.addSwitch( 's1' )
	# Create internal DMZ switch
	s2 = net.addSwitch( 's2' )

if __name__ == "__main__":
	while apptype > 0:
		print '*** Starting network\n'
		net.start()
		while apptype > 0:
			getapptype()
			if apptype == 1:
				createapp1()
			elif apptype == 2:
				createapp2()

			startest()	

		print '*** Running CLI\n'
		CLI( net )
		print '*** Stopping network'
		net.stop()
