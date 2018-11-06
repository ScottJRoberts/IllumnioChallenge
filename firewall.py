import csv;


class Firewall(object):
    rules = {};

    def __init__(self, csv):
        self.setUpRules();
        with open(csv) as data:
            for row in data:
                #stip off quotes and newlines
                row = row[1:len(row)-2];
                direction, protocol, port, ip = row.split(',');
                prev_ports = self.rules[direction][protocol];
                if port in prev_ports:
                    self.rules[direction][protocol][port]+=[ip];
                else:
                    self.rules[direction][protocol][port] = [ip];
            

    def accept_packet(self, direction, protocol, port, ip):
        if direction in self.rules:

            if protocol in self.rules[direction]:
                approved_ports = self.rules[direction][protocol];
                temp = self._check_port(port, approved_ports);
                if temp in approved_ports:
                    
                    approved_IPs = self.rules[direction][protocol][temp];

                    if self._check_ip(ip, approved_IPs):
                        return True;

        return False;

    def _check_ip(self, specificAddress, possibleAddresses):
        for possibility in possibleAddresses:
            options = possibility.split('-')
            if len(options) ==1:
                if options[0] == specificAddress:
                    return True;
            else:
                if self._ip_in_range(specificAddress, possibility):
                    return True;
        return False;

        return False;


    def _ip_in_range(self, ip, range):

        low, high = range.split('-');
        return self._compare_ip(ip, low) == ip and self._compare_ip(ip, high) == high;

    def _compare_ip(self, ip1, ip2):
        
        positions1 = ip1.split('.');
        positions2 = ip2.split('.');
        if ip1 == ip2:
            return ip2;
        for x in range(len(positions1)):

            if int(positions1[x])> int(positions2[x]):
                return ip1;
        
        return ip2;

    def _check_port(self, specificPort, possiblePorts):
        possiblePorts = list(possiblePorts.keys());
        for possibility in possiblePorts:
            options = possibility.split('-');
            if len(options) == 1:
                if specificPort == possibility:
                    return possibility;
            else:

                temp = self._port_in_range(specificPort, possibility)
                if temp != specificPort:
                    return temp;

        return specificPort;

    def _port_in_range(self, port, rangeOfPorts):

        low, high = rangeOfPorts.split('-');
        if int(low) <= int(port) and int(high) >=int(port):

            return rangeOfPorts;

        return port;

    def setUpRules(self):
        self.rules["outbound"] = {}
        self.rules["inbound"] = {}
        self.rules["outbound"]["tcp"] = {}
        self.rules["outbound"]["udp"] = {}
        self.rules["inbound"]["tcp"] = {}
        self.rules["inbound"]["udp"] = {}
    





