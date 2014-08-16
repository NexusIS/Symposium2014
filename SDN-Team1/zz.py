#!/usr/bin/python
servertype = 0
servicelevel = 0
#
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

net = Mininet()
#c0 = net.addController( 'c0' )
#c0 = net.AddController( 'c0', controller=RemoteController, ip='10.192.34.22' )
c0 = net.RemoteController( 'c0', ip='10.192.34.22' )
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
s1 = net.addSwitch( 's1' )
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.start()
CLI( net )
net.stop()
