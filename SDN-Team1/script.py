#!/usr/bin/python
import os
os.system('clear')
customer = 'Pi'
servertype = 0
servicelevel = 0
#
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


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
print "# 2) MySQL Database Server    #"
print "# 3) App Server               #"
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
#
net = Mininet()
h1 = net.addHost( 'h1' )

s1 = net.addSwitch( 's1' )
net.addLink( h1, s1 )
print "###############################"
print "# Creating Virtual Machine... #"
print "# Creating Virtual Switch.... #"
print "# Assign IP addressing....... #"
print "# Testing IP connectivity.... #"
print "###############################"
net.start()
print h1.cmd( 'ping -c3', h1.IP() )

a = raw_input ("Hit Enter to continue")
os.system('clear')
#
#net.stop()

#
 
