import os, requests, time, random, sys
import pprint


def GeoIP():
    ip_input = input('  IP> ')
    response = requests.get("https://api.iplocation.net/?ip=" + ip_input)
    response.json()
    pprint.pprint(response.json())
    time.sleep(10)
    Main()

def scraper():
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(r.text)
    p_type = input('  Type> ')
    p_timeout = input('  Timeout> ')
    f"https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}"
    with open('proxies.txt', 'w') as f:
        f.write(r.text)
        print('The proxies have been saved to \033[31m`proxies.txt`')
        time.sleep(5)
        Main()        
class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str('  @>  '))
            if(choose == str(1)):
                self.cls()
                self.start_logo()
                GeoIP()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                scraper()


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
       
   
 ██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██║     ██╔═══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝
██║  ███╗██║     ██║   ██║██║   ██║██████╔╝██║   ██║███████╗
██║   ██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║╚════██║
╚██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║
 ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝     
 by Danis
 https://gloobus.tech
 https://dsc.gg/gloobus

                                              
                                 
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def options(self):
        print(self.y + '        [1] ' + self.c +'  GeoIP')
        print(self.y + '        [2] ' + self.c + '  Proxy Scrape')

Main()
