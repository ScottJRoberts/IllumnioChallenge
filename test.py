from firewall import Firewall;

fw_basic = Firewall('./test.csv');



#test general
print('test general');
print(fw_basic.accept_packet("inbound", "tcp", '80', "192.168.1.2")); # matches first rule
print(fw_basic.accept_packet("inbound", "udp", '53', "192.168.2.1")) # matches third rule
print(fw_basic.accept_packet("outbound", "tcp",'10234', "192.168.10.11")) # matches second rule

print(fw_basic.accept_packet("inbound", "tcp", '81', "192.168.1.2")) 

print(fw_basic.accept_packet("inbound", "udp", '24', "52.12.48.92"))
print(fw_basic.accept_packet('badDirection', 'tcp', '80', '192.168.1.2'));
print(fw_basic.accept_packet('inbound', 'badProtocol', '80', '192.168.1.2'))
print(fw_basic.accept_packet('inbound', 'tcp', '80','0.0.0.0'));


#test ip range
print('test ip range');
print(fw_basic.accept_packet('inbound','udp','53','192.168.2.2')); # inside
print(fw_basic.accept_packet('inbound','udp','53','192.168.2.5')); #edges
print(fw_basic.accept_packet('inbound','udp','53','192.168.1.1'));

print(fw_basic.accept_packet('inbound','udp','53','192.168.2.6')); #outside

#test port range
print('test port range');
print(fw_basic.accept_packet("outbound","udp","999","52.12.48.92"));
print(fw_basic.accept_packet("outbound","udp","1000","52.12.48.92"));
print(fw_basic.accept_packet("outbound","udp","1200","52.12.48.92"));
print(fw_basic.accept_packet("outbound","udp","1900","52.12.48.92"));
print(fw_basic.accept_packet("outbound","udp","2000","52.12.48.92"));
print(fw_basic.accept_packet("outbound","udp","2001","52.12.48.92"));


fw_all_IP = Firewall('./allIPsTest.csv');

#test all IPs
print('testing all IPs');
print(fw_all_IP.accept_packet("inbound", "tcp", '80', "0.0.0.0")); 
print(fw_all_IP.accept_packet("inbound", "tcp", '80', "0.168.1.2")); 
print(fw_all_IP.accept_packet("inbound", "tcp", '80', "255.255.255.255")); 
print(fw_all_IP.accept_packet("inbound", "tcp", '81', "0.168.1.2")); 

fw_allPorts = Firewall('./allPortsTest.csv');
print('testing all ports');
print(fw_allPorts.accept_packet("inbound","udp","65535","192.168.1.1"));
print(fw_allPorts.accept_packet("inbound","udp","1","192.168.1.1"))
print(fw_allPorts.accept_packet("inbound","udp","6553","192.168.1.1"))
print(fw_allPorts.accept_packet("inbound","udp","65535","192.168.1.0"))


