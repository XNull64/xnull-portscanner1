import socket
import concurrent.futures
 from colorama import Fore,Style,init
init()

print(Fore.CYAN + """
██╗  ██╗███╗   ██╗██╗   ██╗██╗     ██╗     
██║  ██║████╗  ██║██║   ██║██║     ██║     
███████║██╔██╗ ██║██║   ██║██║     ██║     
██╔══██║██║╚██╗██║██║   ██║██║     ██║     
██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
               XNull PortScanner
""" + Style.RESET_ALL)

target = input(Fore.YELLOW + "[+] Hedef IP veya domain: " + Style.RESET_ALL)
start_port = int(input(Fore.YELLOW + "[+] Başlangıç portu: " + Style.RESET_ALL))
end_port = int(input(Fore.YELLOW + "[+] Bitiş portu: " + Style.RESET_ALL))

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(Fore.GREEN + f"[+] Port {port} AÇIK" + Style.RESET_ALL)
        s.close()
    except:
        pass

print(Fore.BLUE + f"\n[!] Taramaya başlandı: {target} ({start_port}-{end_port})\n" + Style.RESET_ALL)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan_port, port)

print(Fore.BLUE + "\n[!] Tarama bitti." + Style.RESET_ALL)