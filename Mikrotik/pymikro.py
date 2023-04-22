
from colorama import init, Fore, Style

banner = """
  .______   ____    ____ .___  ___.  __   __  ___ .______        ______   
   |   _  \  \   \  /   / |   \/   | |  | |  |/  / |   _  \      /  __  \  
   |  |_)  |  \   \/   /  |  \  /  | |  | |  '  /  |  |_)  |    |  |  |  | 
   |   ___/    \_    _/   |  |\/|  | |  | |    <   |      /     |  |  |  | 
   |  |          |  |     |  |  |  | |  | |  .  \  |  |\  \----.|  `--'  | 
   | _|          |__|     |__|  |__| |__| |__|\__\ | _| `._____| \______/  
                                                                           

"""

# Print the banner to the console
print(Fore.CYAN+banner+Style.RESET_ALL)

# Add an introduction message
print(Fore.LIGHTGREEN_EX+"Welcome to Taha Exe Python Script!"+ Style.RESET_ALL)
import subprocess

while True:
    # Prompt the user for their selection
    print(Fore.LIGHTBLUE_EX+"please select the path you need to access on it "+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX +"Select 1 for Mikrotik Automation and tools"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX +"select 2 for Windows Local tools "+Style.RESET_ALL)
    choice = input(Fore.RED+"Enter your tool number: "+Style.RESET_ALL)

    # Mikrotik Part include disable services and other tools
    if choice == '1':
        while True:
            print(Fore.GREEN+"welcome to Mikrotik Automation toolbox"+Style.RESET_ALL)
            print(Fore.YELLOW+"for exit select q"+Style.RESET_ALL)
            print(Fore.YELLOW+"★select 1 for Block Scan script that increase the router security"+Style.RESET_ALL)
            print(Fore.YELLOW+"★select 2 for BruteForce Detection and Firewall Policy For Protection"+Style.RESET_ALL)
            print(Fore.YELLOW+"★select 3 for Disable non used services in Mikrotik Routers "+Style.RESET_ALL)
            print(Fore.YELLOW+"★select 4 for icmp filter on Mikrotik router to increase the Security"+Style.RESET_ALL)
            print(Fore.YELLOW+"★select 5 for Apply Drop DNS Filter"+Style.RESET_ALL)
            print(Fore.YELLOW+"★ select q for exit"+Style.RESET_ALL)
            choice = input(Fore.RED+"Enter your tool number: "+Style.RESET_ALL)

            if choice == '1':
                import paramiko

                ip = input('Enter the ip address:')
                username = input('please,enter the username :')
                password = input('please, enter the password:')
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
                stdin, stdout, stderr = client.exec_command(
                    'ip firewall filter add action=drop chain=input disabled=yes src-address-list="port scanners"')
                stdin2, stdout2, stderr2 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="portsccanner list" disabled=\
                    yes protocol=tcp psd=21,3s,3,1')
                stdin3, stdout3, stderr3 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="NMAP FIN Stealth scann" \
                    disabled=yes protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg')
                stdin4, stdout4, stderr4 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment=SYN/FIN protocol=tcp \
                    tcp-flags=fin,syn')
                stdin5, stdout5, stderr5 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="SYN.RST SCAN" protocol=tcp \
                    tcp-flags=syn,rst')
                stdin6, stdout6, stderr6 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="FIN/PSH/URG SCAN " protocol=\
                    tcp tcp-flags=fin,psh,!syn,!rst,!ack')
                stdin7, stdout7, stderr7 = client.exec_command(' ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="ALL/ALL SCAN" protocol=tcp \
                    tcp-flags=fin,syn,rst,psh,ack,urg')
                stdin8, stdout8, stderr8 = client.exec_command('ip firewall filter add action=add-src-to-address-list address-list="port scanners" \
                    address-list-timeout=2w chain=input comment="NMAP NULL SCAN" protocol=tcp \
                    tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg')
                for line in stdout:
                    print(line.strip('\n'))
                for line in stdout2:
                    print(line.strip('\n'))
                for line in stdout3:
                    print(line.strip('\n'))
                for line in stdout4:
                    print(line.strip('\n'))
                for line in stdout5:
                    print(line.strip('\n'))
                for line in stdout6:
                    print(line.strip('\n'))
                for line in stdout7:
                    print(line.strip('\n'))
                for line in stdout8:
                    print(line.strip('\n'))



            elif choice == '2':
                import paramiko

                ip = input('Enter the ip address:')
                username = input('please,enter the username :')
                password = input('please, enter the password:')
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
                stdin, stdout, stderr = client.exec_command('/ip firewall filter add action=drop chain=input comment="Drop SSH Brute Force " dst-port=22 \
                    protocol=tcp src-address-list=brute-force_blacklist')
                stdin2, stdout2, stderr2 = client.exec_command(
                    'ip firewall filter add action=add-src-to-address-list address-list=brute-force_blacklist \
                    address-list-timeout=1d chain=input connection-state=new dst-port=22,23 \
                    protocol=tcp src-address-list=bruteforce_stage3')
                stdin3, stdout3, stderr3 = client.exec_command(
                    'ip firewall filter add action=add-src-to-address-list address-list=bruteforce_stage3 \
                    address-list-timeout=30s chain=input connection-state=new dst-port=22,23 \
                    protocol=tcp src-address-list=bruteforce_stage2')
                stdin4, stdout4, stderr4 = client.exec_command(
                    'ip firewall filter add action=add-src-to-address-list address-list=bruteforce_stage2 \
                    address-list-timeout=30s chain=input connection-state=new dst-port=22,23 \
                    protocol=tcp src-address-list=bruteforce_stage1')
                stdin5, stdout5, stderr5 = client.exec_command(
                    'ip firewall filter add action=add-src-to-address-list address-list=bruteforce_stage1 \
                    address-list-timeout=1m chain=input connection-state=new dst-port=22,23 \
                    protocol=tcp')
                for line in stdout:
                    print(line.strip('\n'))
                for line in stdout2:
                    print(line.strip('\n'))
                for line in stdout3:
                    print(line.strip('\n'))
                for line in stdout4:
                    print(line.strip('\n'))
                for line in stdout5:
                    print(line.strip('\n'))
            elif choice == '3':
                import paramiko

                ip = input('Enter the ip address:')
                username = input('please,enter the username :')
                password = input('please, enter the password:')
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
                stdin, stdout, stderr = client.exec_command('ip service disable api,api-ssl,www,www-ssl')
                stdin2, stdout2, stderr2 = client.exec_command('tool bandwidth-server set enabled=no')
                stdin3, stdout3, stderr3 = client.exec_command('ip dns set allow-remote-requests=no')
                stdin4, stdout4, stderr4 = client.exec_command(
                    'ip neighbor discovery-settings set discover-interface-list=none ')
                stdin5, stdout5, stderr5 = client.exec_command('snmp set enabled=no')
                for line in stdout:
                    print(line.strip('\n'))
                for line in stdout2:
                    print(line.strip('\n'))
                for line in stdout3:
                    print(line.strip('\n'))
                for line in stdout4:
                    print(line.strip('\n'))
                for line in stdout5:
                    print(line.strip('\n'))
            elif choice == '4':
                import paramiko

                ip = input('Enter the ip address:')
                username = input('please,enter the username :')
                password = input('please, enter the password:')
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
                stdin, stdout, stderr = client.exec_command(
                    'ip firewall filter add action=jump chain=forward jump-target=icmp ')
                stdin2, stdout2, stderr2 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="echo reply" icmp-options=0:0 protocol=icmp ')
                stdin3, stdout3, stderr3 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="net unreachable" icmp-options=3:0 protocol=icmp')
                stdin4, stdout4, stderr4 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="host unreachable" icmp-options=3:1 protocol=icmp  ')
                stdin5, stdout5, stderr5 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="host unreachable fragmentation required" icmp-options=3:4 protocol=icmp ')
                stdin6, stdout6, stderr6 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="allow source quench" icmp-options=4:0 protocol=icmp ')
                stdin7, stdout7, stderr7 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="allow echo request" icmp-options=8:0 protocol=icmp  ')
                stdin8, stdout8, stderr8 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="allow time exceed" icmp-options=11:0 protocol=icmp  ')
                stdin9, stdout9, stderr9 = client.exec_command(
                    'ip firewall filter add action=accept chain=icmp comment="allow parameter bad" icmp-options=12:0 protocol=icmp  ')
                stdin10, stdout10, stderr10 = client.exec_command(
                    'ip firewall filter add action=drop chain=icmp comment="deny all other types" protocol=icmp ')
                for line in stdout:
                    print(line.strip('\n'))
                for line in stdout2:
                    print(line.strip('\n'))
                for line in stdout3:
                    print(line.strip('\n'))
                for line in stdout4:
                    print(line.strip('\n'))
                for line in stdout5:
                    print(line.strip('\n'))
                for line in stdout6:
                    print(line.strip('\n'))
                for line in stdout7:
                    print(line.strip('\n'))
                for line in stdout8:
                    print(line.strip('\n'))
                for line in stdout9:
                    print(line.strip('\n'))
                for line in stdout10:
                    print(line.strip('\n'))
            elif choice == '5':
                import paramiko

                ip = input('Enter the ip address:')
                username = input('please,enter the username :')
                password = input('please, enter the password:')
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=username, password=password)
                stdin, stdout, stderr = client.exec_command('ip firewall raw add action=drop chain=prerouting comment="Drop DNS ATTACK" dst-port=53 \
                                    in-interface=ether1 protocol=udp ')
                for line in stdout:
                    print(line.strip('\n'))
            elif choice == 'q':
                exit()

            else:
                print("invalid")
                continue

    elif choice == '2':
        while True:
            print(Fore.LIGHTGREEN_EX+"welcome to Windows   Automation toolbox")
            print(Fore.YELLOW+"for exit select q")
            print("★select 1 for Getting Windows ip address ")
            print("★select 2 for release ip address for Windows ")
            print("★select 3 for Renew ip address for windows  ")
            print("★select 4 for icmp filter on Mikrotik router to increase the Security")
            print("★select 5 for Apply Drop DNS Filter")
            print("★select 2 for Getting LOCAL MAC Address ")
            print("★select 3 for Clean Cache for Google Chrome ")
            print("★select 4  for Clean Cache for Microsoft edge")
            print("★select 5 for Clean Cache for Firefox")
            choice = input("Enter your tool number: ")
            if choice == '':
                exit()

            if choice == '1':
                import socket
                import subprocess
                import re
                import uuid

                # Retrieve the IP address using a socket
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip_address = s.getsockname()[0]
                s.close()

                # Retrieve the gateway using the `route print` command
                output = subprocess.check_output("route print", shell=True).decode()
                gateway_match = re.search(r"0\.0\.0\.0\s+0\.0\.0\.0\s+(\d+\.\d+\.\d+\.\d+)\s+.*", output)
                if gateway_match:
                    gateway = gateway_match.group(1)

                else:
                    gateway = "unknown"

                # Print the results
                print("IP address:", ip_address)
                print("Gateway:", gateway)
                # Retrieve the MAC address using the `uuid` module
                mac_address = uuid.getnode()

                # Convert the MAC address to a formatted string
                mac_string = ':'.join(re.findall('..', '%012x' % mac_address))

                # Print the result
                print("MAC address:", mac_string)
                # Retrieve the DNS server addresses using the `getaddrinfo` function
                info = socket.getaddrinfo(socket.gethostname(), None)
                dns_servers = set()
                for item in info:
                    family, socktype, proto, canonname, sockaddr = item
                    if family == socket.AF_INET and socktype == socket.SOCK_DGRAM and proto == socket.IPPROTO_UDP:
                        dns_servers.add(sockaddr[0])

                # Print the result
                print("DNS server addresses:", ", ".join(dns_servers))



            elif choice == '2':

                subprocess.call("ipconfig /release")

            elif choice == '3':
                subprocess.call("ipconfig /renew")

            elif choice == '3':

                command = 'start chrome --disk-cache-dir="C:\chrome_cache\data"'  # replace with the command you want to run
                command2 = 'taskkill /f /im chrome.exe'
                p = subprocess.Popen(["cmd", "/c", command2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p = subprocess.Popen(["cmd", "/c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = p.communicate()

                print(output.decode("utf-8"))
            elif choice == '4':
                command = 'start msedge --disk-cache-dir="C:\msedge_cache\data"'  # replace with the command you want to run
                command2 = 'taskkill /f /im msedge.exe'
                p = subprocess.Popen(["cmd", "/c", command2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                p = subprocess.Popen(["cmd", "/c", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = p.communicate()

                print(output.decode("utf-8"))


    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

