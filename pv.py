# -*- coding:utf-8 -*- 
import urllib.request
import socket
import bs4
import random
import time

agent1 = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)"
agent2 = "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19"
agent3 = "Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0 "
agent4 = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
agent5 = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"
agentlist = [agent1, agent2, agent3, agent4, agent5]

url = 'https://www.xicidaili.com/nn'
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
headers = {}
headers['User-Agent'] = User_Agent


def ips(j):
    url = 'https://www.xicidaili.com/nn/1'
    print(url)
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req).read()
    # print(res)
    soup = bs4.BeautifulSoup(res)
    ips = soup.findAll("tr")
    addr = []
    for x in range(1, len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
        # print(tds[1].contents[0] + "\t" + tds[2].contents[0])
        host = "http://" + ip_temp
        proxy_host = {"http": host}
        addr.append(proxy_host)
        # print(addr)
    return addr


# print(ips())


def visit():
    socket.setdefaulttimeout(3)
    url = 'https://blog.csdn.net/tristanly/article/details/89468860'
    # proxylist = [{"http": "120.194.18.90:81"}, {"http": "39.137.168.229:80"}]
    # proxylist = ips()
    # print(proxylist)
    # proxy = random.choice(proxylist)
    # print(proxy)
    # proxyHandler = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(proxyHandler)
    i = 0
    j = 0
    proxylist = []
    while True:
        lengh = len(proxylist)
        print(lengh)
        if lengh<=10:
            j = j + 1
            proxylist = ips(j)
        proxy = random.choice(proxylist)
        print(proxy)
        proxyHandler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxyHandler)
        agent = random.choice(agentlist)
        print(agent)
        headers = {"User-Agent": agent}
        req = urllib.request.Request(url, headers=headers)
        # response = opener.open(req).read().decode()
        try:
            response = opener.open(req).read().decode()
            opener.open(req)
            time.sleep(random.uniform(60, 70))
            i = i + 1
            print(i)
            # print('%d %s' % (i, req))
            # print(i)
        # except Exception as e:
        #     print(e.message)
        #     pass
        except urllib.error.HTTPError:
            print('urllib.error.HTTPError')
            proxylist.remove(proxy)
            print('ips num: '+str(len(proxylist)))
            # pass
        #     time.sleep(1)
        except urllib.error.URLError:
            print('urllib.error.URLError')
            proxylist.remove(proxy)
            print('ips num: '+str(len(proxylist)))
        except Exception as e:
            proxylist.remove(proxy)
            print('ips num: '+str(len(proxylist)))
            print(e)
            # pass
        #     time.sleep(1)
        # print(i)
        # i = i + 1
        time.sleep(random.uniform(0, 3))
    print('completed')


# timeout = 2
# socket.setdefaulttimeout(timeout)
visit()

