
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import Node
from mininet.topolib import Mininet


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

if __name__ == '__main__':
    lg.setLogLevel( 'info')
    net = MiniNet()
    print "*** Firewall rules have been applied"
    CLI( net )
    stopNAT( rootnode )
    net.stop() 
