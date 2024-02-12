"""
Name: Sinclair DeYoung
Date: 25-10-2023   dd-mm-yyyy
Class: CSC-344
Description: IN the run_ip_file are the ip addresses that will be forwarded to there ports.
 This program implements a forwarding algorithm based upon IPv4 addresses using files.
"""
import ipaddress

def read_routing_table(IP_file):
    """
    read the ip_file and create a routing table dictionary
    :param IP_file: with IP addresses
    :return: routing table
    """
    routing_table = []
    with open( 'ip_file' ,'r') as file:
        for line in file:
            try:
                ip ,mask ,prefix ,port = line.split()
                routing_table.append({'IP: ': ip,'Mask: ': mask,'Prefix: ': int(prefix),'Port: ': int(port)})
            except ValueError:
                pass
        return routing_table
def find_matching_entry(ip, routing_table):
    """
    Looking up the routing table and check for prefex length
    :param ip: pulled from the file
    :param routing_table: from the reading function
    :return: longest match
    """
    longest_match = None
    for entry in routing_table:
        # check if the IP address matches with the entry subnet
        try:
            if is_matching_ip(ip, entry['IP: '], entry['Mask: ']):
                if longest_match is None or entry['Prefix: '] > longest_match['Prefix: ']:
                    longest_match = entry
        except KeyError:
            pass
    return longest_match

def is_matching_ip(ip, subnet, mask):
    """
    checks for matching ip
    :param ip: from the find function
    :param subnet: from the find function
    :param mask: from the match function
    :return: an ip in a subnet
    """
    try:
        # parse the IP and subnet into IPv4Adddress and IPv4Network objects
        ip = ipaddress.IPv4Address(ip)
        subnet = ipaddress.IPv4Network(f"{subnet}/{mask}")
        # check if the IP address is within the given subnet
        return ip in subnet
    except ValueError:
        # handle any potential parsing errors
        return False

def validate_ip(ip):
    """
    validate the ip addresses are in ipv4 format and are valid
    :param ip: from the find function
    :return: boolean t or f
    """
    try:
        # Attempt to parse the input as an IPv4 address
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

def main():
    """
    main function that displays the output
    :return: output
    """
    txt_file = 'ip_file'
    routing_table = read_routing_table(txt_file)

    with open('run_ip_file.txt', 'r') as file:
        count = 1
        for line in file:
            ip = line.strip()
            if validate_ip(ip):
                entry = find_matching_entry(ip, routing_table)
                if entry:
                    print(f"{count}: Forward {ip} to port {entry['Port: ']}")
                elif not entry:
                    print(f"{count}: Forward {ip} to port 1")
                else:
                    print("There was an error!")
                count += 1

            else:
                print('Invalid IP address format.')

if __name__ == "__main__":
    main()