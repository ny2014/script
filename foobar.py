#!/usr/bin/python

from requests import session
from bs4 import BeautifulSoup

USER = ''
PASS = '' 

logonFormUrl = 'https://www.costco.com/LogonForm'
logonUrl = 'https://www.costco.com/Logon'
accountInformationUrl = 'https://www.costco.com/AccountInformationView'
# orderUrl = 'https://www.costco.com/OrderStatusCmd?fromYear=2019&fromMonth=1&toYear=2019&toMonth=6'
# orderUrl = 'https://www.costco.com/OrderStatusCmd?storeId=10301&catalogId=10701&langId=-1&URL=&fromYear=2019&fromMonth=0&toMonth=5&toYear=2019&selection=1'

headers = {
    'User-Agent': 'MyServer/1.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Host': 'www.costco.com'
    # 'cache-control': 'no-cache'
}

with session() as s:
    initCookies = s.get(logonFormUrl, headers=headers)
    soup = BeautifulSoup(initCookies.text, 'html.parser')

    authToken = soup.find('input', attrs={'name': 'authToken'})
    # -1002%2C5M9R2fZEDWOZ1d8MBwy40LOFIV0%3D
    
    payload = {
        'logonId': USER,
        'logonPassword': PASS,
        'reLogonURL': 'LogonForm',
        'isPharmacy': 'false',
        'fromCheckout': '',
        'authToken': authToken,
        'URL': ''
    }

    headers['referer'] = 'https://www.costco.com/Logon'

    login = s.post(logonUrl, headers=headers, data=payload)
    
    print login.content

    accountPage = s.get(accountInformationUrl, headers=headers)

    print accountPage.content

    # print('**********************')

    # accountPage2 = s.get('https://www.costco.com/AjaxOrderStatusCmd?currentPage=2&fromYear=2019&fromMonth=0&toYear=2019&toMonth=5&monthSelection=&startMonth=&endMonth=', headers=headers)
    # print(accountPage2.content)



