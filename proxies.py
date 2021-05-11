import requests
import time
import random
from bs4 import BeautifulSoup
import concurrent.futures
from selenium import webdriver

# pegar as proxies gratuitas!!!

def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies_ = []

    for row in table:
        if row.find_all('td')[4].text == 'elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies_.append(proxy)
        else:
            pass
    return proxies_

proxy = getProxies()

print('+++++++++++++++++++++ INICIANDO +++++++++++++++++++++')
for i in proxy:
    dic = {
        'http' : 'http://'+str(i),
        'https' : 'https://'+str(i)
    }
    try:
        r = requests.get('http://httpbin.org/ip', proxies=dic, timeout = 2)
        if r.status_code == 200:
            print(f'proxies aceitas: {dic}')
            variavel_proxy = dic
            break
        else:
            print(f'PROXY FAILE: {dic}')
    except:
        print('Erro na resposta da Proxy')

# # print(getProxies())

def tProxy(proxy):
    if proxy:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server='+ proxy['http'])
            chrome = webdriver.Chrome( chrome_options=chrome_options)
            chrome.get('https://whatismyipaddress.com')

            time.sleep(100)
            chrome.close()
        except:
            print('Erro na proxy conection')
            pass

if __name__ == '__main__':
    proxies = getProxies()
    tProxy(variavel_proxy)