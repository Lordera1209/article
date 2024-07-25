#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 3.11
# @Author   : Lordera
# @Datetime : 2024/7/24 下午3:15
# @Project  : streamlit_page
# @File     : article1.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def sp0(url, k):
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = "203.19.38.114:1080"
    proxy.ssl_proxy = "203.19.38.114:1080"
    
    chrome_options = Options()
    # chrome_options.binary_location = r".\chrome.exe"
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument('--proxy-server=%s' % proxy.http_proxy)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    
    # service = Service('./chromedriver_127.0.6533.72_x64.exe')
    # service = ChromeService(executable_path='./chromedriver_127.0.6533.72_x64.exe')
    # driver = webdriver.Chrome(options=chrome_options, service=service)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome()
    cookies = {
        'name': 'BAIDUID_BFESS',
        'value': 'B38D665C1D5DF6252516DBA2F5D5341B:FG=1',
    }
    
    driver.get(url=url)
    driver.add_cookie(cookies)
    driver.get(url=url)
    
    title_list, sub_title_list, suffix_list = [], [], []
    try:
        rows = driver.find_elements(By.XPATH, '//div[@class="information-flow-item"]')
        for i in range(int(k)):
            title = rows[i].text.split("\n")[0]
            sub_title = rows[i].text.split("\n")[1]
            suffix = rows[i].find_elements(By.XPATH, '//div/a[@class="article-item-description ellipsis-2"]')[
                i].get_attribute("href")
            
            title_list.append(title)
            sub_title_list.append(sub_title)
            suffix_list.append(suffix)
    
    except Exception as e:
        print(f"数据抓取过程中出错: {e}")
    
    driver.quit()
    
    return title_list, sub_title_list, suffix_list


def sp1(url):
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = "203.19.38.114:1080"
    proxy.ssl_proxy = "203.19.38.114:1080"
    
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument('--proxy-server=%s' % proxy.http_proxy)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--headless')

    service = ChromeService(executable_path=ChromeDriverManager().install())
    # service = Service('./chromedriver_127.0.6533.72_x64.exe')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    
    cookies = {
        'name': 'BAIDUID_BFESS',
        'value': 'B38D665C1D5DF6252516DBA2F5D5341B:FG=1',
    }
    
    driver.get(url=url)
    driver.add_cookie(cookies)
    driver.get(url=url)
    
    content = []
    try:
        rows = driver.find_elements(By.XPATH, '//div[@class="common-width content articleDetailContent '
                                              'kr-rich-text-wrapper"]/p')
        for row in rows:
            if row.get_attribute('class') == 'image-wrapper':
                content.append(row.find_element(By.XPATH, './img').get_attribute("src"))
            else:
                content.append(row.text)
    
    except Exception as e:
        print(f"数据抓取过程中出错: {e}")
    
    driver.quit()
    
    return content
