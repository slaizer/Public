from colorama import init, Fore, Style
import subprocess

banner = """

 ______ ___.__. _____ _____  ______  
 \____ <   |  |/     \\__  \ \____ \ 
 |  |_> >___  |  Y Y  \/ __ \|  |_> >
 |   __// ____|__|_|  (____  /   __/ 
 |__|   \/          \/     \/|__|    

"""

# Print the banner to the console
print(Fore.CYAN + banner + Style.RESET_ALL)

# Introduction Message
print(Fore.LIGHTGREEN_EX + "Welcome to Taha Exe Python Script! \U0001F600 " + Style.RESET_ALL)

while True:
    print(Fore.YELLOW + "1-for Scanning IP available in Network Range \U0001F609 ")
    print(Fore.YELLOW + "2-for Scanning IP range or Network  with Ports and Details \U0001F44D ")
    print(Fore.YELLOW + "3- for Stealth Scan \U0001F525   ")
    print(Fore.YELLOW + "4- For Fast Scan \U0001F648   ")
    print(Fore.YELLOW + "5- For Advance Scanning Using Zombie \U00002764\U0000FE0F  ")
    print(Fore.YELLOW + "6- For Scanning TCP Port  \U0001F614 ")
    print(Fore.YELLOW + "7- For Scanning UDP Port \U0001F60E")
    print(Fore.YELLOW + "8- Advanced SCTP (Stream Control Transmission Protocol) scan \U0001F4A9")
    print(Fore.YELLOW + "9- For XMAS Scanning  \U0001F634")

    choice = input(Fore.RED + "Enter your tool number: " + Style.RESET_ALL)

    if choice == '1':



        init()

        print(Fore.LIGHTBLUE_EX + "For scanning Network Range, it should be like this: 172.16.16.0/24")
        print(Fore.LIGHTBLUE_EX + "For scanning Specific Network, it should be like this: 172.16.16.10-30")
        network_range = input(Fore.CYAN + "IP ADDRESS: ")

        # run the nmap command
        result = subprocess.run(['nmap', '-sn', network_range], capture_output=True)

        # decode the output and split it into lines
        output = result.stdout.decode()
        lines = output.splitlines()

        # Open a file to write the results
        with open("scan_results.txt", "w") as file:
            # loop through the lines and print the status of each host
            for i, line in enumerate(lines):
                if 'Host is up' in line:
                    parts = lines[i - 1].split()
                    ip_address = parts[-1].strip('()')
                    result_line = f'{ip_address}'
                    print(Fore.GREEN + result_line + Style.RESET_ALL)

                    # Write the result line to the file
                    file.write(result_line + "\n")

        print(Fore.YELLOW + "Scan results saved to scan_results.txt" + Style.RESET_ALL)

        init()

    elif choice == '2':
        import nmap
        from colorama import init, Fore, Style
        import subprocess

        init()

        print(Fore.LIGHTBLUE_EX + "For scanning Network Range, it should be like this: 172.16.16.0/24")
        print(Fore.LIGHTBLUE_EX + "For scanning Specific Network, it should be like this: 172.16.16.10-30")
        network_range = input(Fore.CYAN + "IP ADDRESS: ")

        # run the nmap command
        result = subprocess.run(['nmap', '-sn', network_range], capture_output=True)

        # decode the output and split it into lines
        output = result.stdout.decode()
        lines = output.splitlines()

        # Open a file to write the results
        with open("scan_results.txt", "w") as file:
            # loop through the lines and print the status of each host
            for i, line in enumerate(lines):
                if 'Host is up' in line:
                    parts = lines[i - 1].split()
                    ip_address = parts[-1].strip('()')
                    result_line = f'{ip_address}'
                    print(Fore.GREEN + result_line + Style.RESET_ALL)

                    # Write the result line to the file
                    file.write(result_line + "\n")

        print(Fore.YELLOW + "Scan results saved to scan_results.txt" + Style.RESET_ALL)

        init()

        print("Example for scanning the network range 172.16.16.0/24")
        print("Example for scanning port range (10-200)")
        print("Example for scanning different port ranges (10,15,80)")
        print("Example for scanning one port (10)")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("scan_results.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        port = input("Port Number:")

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sS -sV -Pn {port}')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])

    elif choice == '3':
        import nmap
        from colorama import init, Fore, Style
        import subprocess

        init()

        print(Fore.LIGHTBLUE_EX + "For scanning Network Range, it should be like this: 172.16.16.0/24")
        print(Fore.LIGHTBLUE_EX + "For scanning Specific Network, it should be like this: 172.16.16.10-30")
        network_range = input(Fore.CYAN + "IP ADDRESS: ")

        # run the nmap command
        result = subprocess.run(['nmap', '-sn', network_range], capture_output=True)

        # decode the output and split it into lines
        output = result.stdout.decode()
        lines = output.splitlines()

        # Open a file to write the results
        with open("scan_results.txt", "w") as file:
            # loop through the lines and print the status of each host
            for i, line in enumerate(lines):
                if 'Host is up' in line:
                    parts = lines[i - 1].split()
                    ip_address = parts[-1].strip('()')
                    result_line = f'{ip_address}'
                    print(Fore.GREEN + result_line + Style.RESET_ALL)

                    # Write the result line to the file
                    file.write(result_line + "\n")

        print(Fore.YELLOW + "Scan results saved to scan_results.txt" + Style.RESET_ALL)

        init()

        print("Example for scanning the network range 172.16.16.0/24")
        print("Example for scanning port range (10-200)")
        print("Example for scanning different port ranges (10,15,80)")
        print("Example for scanning one port (10)")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("scan_results.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        port = input("Port Number:")

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sS -sV -A -O -p {port}')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])

    elif choice == '4':
        import nmap
        from colorama import init, Fore, Style

        # initialize colorama
        init()

        print("use ip-list text file to add the ip that need to be scanning ")
        print("Example for scanning port range (10-200)")
        print("Happy Hunting ")


        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("ip-list.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        port = input("Port Number:")

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-F {port}')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])
    elif choice == '5':
        import nmap
        from colorama import init, Fore, Style

        # initialize colorama
        init()

        print("use ip-list text file to add the ip that need to be scanning ")
        print("Example for scanning port range (10-200)")
        print("Happy Hunting ")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("ip-list.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        port = input("Port Number:")

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sI zombie_host {port}')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])
    elif choice == '6':
         import nmap
         from colorama import init, Fore, Style

         # initialize colorama
         init()

         print("use ip-list text file to add the ip that need to be scanning ")
         print("Example for scanning port range (10-200)")
         print("Happy Hunting ")

         # create a new nmap object
         nm = nmap.PortScanner()

         # Read IP addresses from a file
         with open("ip-list.txt", "r") as file:
             ip_addresses = [line.strip() for line in file]



         for ip in ip_addresses:
             # perform an advanced scan on a target host
             nm.scan(ip, arguments=f'-sT')

             # print the results of the scan
             for host in nm.all_hosts():
                 print('Host : %s (%s)' % (host, nm[host].hostname()))
                 print('State : %s' % nm[host].state())
                 for proto in nm[host].all_protocols():
                     print('Protocol : %s' % proto)
                     lport = nm[host][proto].keys()
                     for port in sorted(lport):
                         state = nm[host][proto][port]['state']
                         if state == 'closed':
                             state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                         elif state == 'open':
                             state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                         print('port : %s\tstate : %s' % (port, state))
                         print('product : %s' % nm[host][proto][port]['product'])
                         print('version : %s' % nm[host][proto][port]['version'])
                         print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                         print('name : %s' % nm[host][proto][port]['name'])
                         print('conf : %s' % nm[host][proto][port]['conf'])
                         print('cpe : %s' % nm[host][proto][port]['cpe'])

    elif choice == '7':
        import nmap
        from colorama import init, Fore, Style

        # initialize colorama
        init()

        print("use ip-list text file to add the ip that need to be scanning ")
        print("Happy Hunting \U0001F47B ")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("ip-list.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sU')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])
    elif choice == '8':
        import nmap
        from colorama import init, Fore, Style

        # initialize colorama
        init()

        print("use ip-list text file to add the ip that need to be scanning ")
        print("Happy Hunting \U0001F47B ")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("ip-list.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sZ')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])

    elif choice == '9':
        import nmap
        from colorama import init, Fore, Style

        # initialize colorama
        init()

        print("use ip-list text file to add the ip that need to be scanning ")
        print("Happy Hunting \U0001F47B ")

        # create a new nmap object
        nm = nmap.PortScanner()

        # Read IP addresses from a file
        with open("ip-list.txt", "r") as file:
            ip_addresses = [line.strip() for line in file]

        for ip in ip_addresses:
            # perform an advanced scan on a target host
            nm.scan(ip, arguments=f'-sX')

            # print the results of the scan
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    lport = nm[host][proto].keys()
                    for port in sorted(lport):
                        state = nm[host][proto][port]['state']
                        if state == 'closed':
                            state = Fore.RED + Style.BRIGHT + state + Style.RESET_ALL
                        elif state == 'open':
                            state = Fore.GREEN + Style.BRIGHT + state + Style.RESET_ALL
                        print('port : %s\tstate : %s' % (port, state))
                        print('product : %s' % nm[host][proto][port]['product'])
                        print('version : %s' % nm[host][proto][port]['version'])
                        print('extrainfo : %s' % nm[host][proto][port]['extrainfo'])
                        print('name : %s' % nm[host][proto][port]['name'])
                        print('conf : %s' % nm[host][proto][port]['conf'])
                        print('cpe : %s' % nm[host][proto][port]['cpe'])



    else:
        print("invalid")
        continue
