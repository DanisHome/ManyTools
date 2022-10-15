import os, re, random, string, time, sys, base64, httpx
from colorama import Fore
from colorama import Style
from random import randint
from lxml.html import fromstring
from threading import Thread
from httpx_socks import SyncProxyTransport


def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        os.system("title gloobus")
    else:
        print('gloobus')

    print(f'''

{Fore.WHITE} ██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗███████╗
{Fore.BLUE}██╔════╝ ██║     ██╔═══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝
{Fore.RED}██║  ███╗██║     ██║   ██║██║   ██║██████╔╝██║   ██║███████╗
{Fore.WHITE}██║   ██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║╚════██║
{Fore.BLUE}╚██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝███████║
{Fore.RED} ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
{Fore.LIGHTBLACK_EX}https://gloobus.tech
{Fore.LIGHTBLACK_EX}https://lenda-development.eu
               ''')

    time.sleep(1)
    slowprint(
        f'{Fore.LIGHTBLACK_EX}Made by: {Fore.RESET}{Fore.WHITE}Danis{Fore.RESET}', .02)
    time.sleep(1)

    operation = input(f'''
    {Fore.BLUE}Whatchu wanna do?{Fore.RESET}
{Fore.RED}     |--------------------------------------------------------------------------------------|
{Fore.RED}     |{Fore.BLUE}    [1] Nitro Gen and Checker                      {Fore.RED} |{Fore.GREEN} [-]Soon!                        {Fore.RED}|             
{Fore.RED}     |{Fore.BLUE}    [2] Token Gen and Checker                      {Fore.RED} |{Fore.GREEN} [-]Soon!                        {Fore.RED}| 
{Fore.RED}     |{Fore.BLUE}    [3] Proxy Scraper                              {Fore.RED} |{Fore.GREEN} [-]Soon!                        {Fore.RED}|
{Fore.RED}     |{Fore.BLUE}    [4] HTTP/SOCKS4/SOCKS5 Proxy Checker3          {Fore.RED} |{Fore.GREEN} [-]Soon!                        {Fore.RED}|
{Fore.RED}     |{Fore.BLUE}    [5] GeoIP{Fore.CYAN}!Updating!                            {Fore.RED} |{Fore.GREEN} [-]Soon!                        {Fore.RED}|
{Fore.RED}     |--------------------------------------------------------------------------------------|

{Fore.LIGHTMAGENTA_EX}                         [E]Exit

{Fore.LIGHTBLACK_EX}Please enter an correct Number>''')
    if str(operation) == "1":
        nitrogen()
    elif str(operation) == "2":
        tokengen()
    elif str(operation) == "3":
        proxyscraper()
    elif str(operation) == "4":
        proxychecker()
    elif str(operation) == "5":
        GeoIP()    
    elif str(operation) == "E":
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n                                                      Incorrect option")
        time.sleep(2)
        main()


def nitrogen():
    os.system('cls' if os.name == 'nt' else 'clear')
    def check(prxtype,fileproxy):
        if prxtype == 'HTTP':
            proxtype = 'http://'
        elif prxtype == 'SOCKS5':
            proxtype = 'socks5://'
        nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(19))
        try:
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            r = httpx.get(url,proxies=proxtype + random.choice(list(map(lambda x:x.strip(),open(fileproxy)))))
            if r.status_code == 200:
                with open('Valid Nitro.txt', 'a') as f:
                    f.write('https://discord.com/gifts/' + nitro + '\n')
                print(f'{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | https://discord.com/gifts/{nitro}')
            else:
                print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | https://discord.com/gifts/{nitro}')
        except:
            pass

    def nitros():
        try:
            prxtype = input('HTTP/SOCKS5: ')
        except:
            print('Invalid')
            main()
        try:
            fileproxy = input('Proxy File: ')
        except:
            print('Invalid')
            main()
        while True:
            t = Thread(target=check, args=(prxtype,fileproxy),daemon=True)
            t.start()
    nitros()
    main()


def GeoIP():
    ip_input = input('  IP> ')
    response = requests.get("https://api.iplocation.net/?ip=" + ip_input)
    response.json()
    print.pprint(response.json())
    time.sleep(10)
    main()

def tokengen():
    os.system('cls' if os.name == 'nt' else 'clear')
    def check(prxtype,fileproxy):
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(randint(100000000000000000,999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(
                string.ascii_letters).upper() + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(38))
        if prxtype == 'HTTP':
            proxtype = 'http://'
        elif prxtype == 'SOCKS5':
            proxtype = 'socks5://'

            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            try:
                r = httpx.get("https://discordapp.com/api/v6/users/@me/library", headers=header, proxies=proxtype + random.choice(list(map(lambda x:x.strip(),open(fileproxy)))))
                if r.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}Valid{Fore.RESET} | {token}')
                    with open("workingtokens.txt", "a") as f:
                        f.write(token + "\n")

                elif "rate limited." in r.text:
                    print("[-] You are being rate limited. Will wait 10 seconds!")
                    time.sleep(10)

                else:
                    print(f'{Fore.LIGHTRED_EX}Invalid{Fore.RESET} | {token}')
            except:
                pass
    def tokens():
        try:
            prxtype = input('HTTP/SOCKS5: ')
        except:
            print('Invalid')
            main()
        try:
            fileproxy = input('Proxy File: ')
        except:
            print('Invalid')
            main()
        while True:
            t = Thread(target=check, args=(prxtype,fileproxy),daemon=True)
            t.start()
    tokens()
    main()


def proxyscraper():
    os.system('cls' if os.name == 'nt' else 'clear')
    http = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=http&ssl=yes','https://api.proxyscrape.com/?request=displayproxies&proxytype=https&ssl=yes','https://sheesh.rip/new.txt','https://www.proxy-list.download/api/v1/get?type=https','https://www.proxy-list.download/api/v1/get?type=http','https://spys.me/proxy.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt','https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt','https://raw.githubusercontent.com/almroot/proxylist/master/list.txt']
    s4 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks4','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt']
    s5 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks5','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt']
    try:
        os.remove('http.txt')
        os.remove('socks4.txt')
        os.remove('socks5.txt')
    except:
        pass
    for src in http:
        r = httpx.get(src)
        with open("http.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('HTTP Scraped')
    for src in s4:
        r = httpx.get(src)
        with open("socks4.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS4 Scraped')
    for src in s5:
        r = httpx.get(src)
        with open("socks5.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS5 Scraped')
    time.sleep(2)
    main()


def proxychecker():
    os.system('cls' if os.name == 'nt' else 'clear')
    def check(PROXY,url,prxtype):
        if prxtype == 'HTTP':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownHTTP]','accept-language': 'en'},follow_redirects=True,proxies='http://'+PROXY)
        elif prxtype == 'SOCKS5':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS5]','accept-language': 'en'},follow_redirects=True,proxies='socks5://'+PROXY)
        elif prxtype == 'SOCKS4':
        	HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS4]','accept-language': 'en'},follow_redirects=True,transport=SyncProxyTransport.from_url('socks4://'+PROXY))

        with HxClient as client:
            try:
                    req = client.get(url)
                    if req.status_code == 200 and "GET" in req.text:
                        print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                        with open(f'{prxtype}_good.txt', 'a') as xX:
                            xX.write(PROXY + '\n')
                    elif req.status_code != 200 or not "GET" in req.text:
                        print (Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
                    else:
                        print(Fore.RED + '[Bad] ' + PROXY + ' ' + str(req.status_code))
            except httpx.HTTPError as exc:
                pass
            except:
                pass
    def proxer():
        try:
            prxtype = input('HTTP/SOCKS4/SOCKS5: ')
        except:
            print('Invalid')
            main()
        try:
            fileproxy = input('Proxy File: ')
        except:
            print('Invalid')
            main()
        domain = 'https://httpbin.org/anything'
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(fileproxy, 'r') as x:
            prox = x.read().splitlines()
        Threads = []
        for proxy in prox:
            t = Thread(target=check, args=(proxy,domain,prxtype),daemon=True)
            t.start()
            Threads.append(t)
        for i in Threads:
            i.join()
        print('Done!')
        time.sleep(5)
    proxer()
    main()

def exit():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowprint('Bey Bey Bey Bey Bey Bey Bey Bey Bey Bey Bey Bey Bey', .02)
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    raise SystemExit


if __name__ == '__main__':
    main()
