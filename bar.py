#!/usr/bin/python

from requests import session
from bs4 import BeautifulSoup as bs

 
USER = ''
PASSWORD = ''

URL1 = 'https://www.costco.com/LogonForm'
URL2 = 'https://www.costco.com'
URL3 = 'https://www.costco.com/OrderStatusCmd?fromYear=2019&fromMonth=0&toYear=2019&toMonth=5'
headers = {'User-Agent': 
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

with session() as s:

    r0 = s.get(URL1, headers = headers, verify=True)
    req = r0.text
    print(r0.status_code)
    
    #print(r0.content)
    html = bs(req, features="lxml")
    token = html.find("input", {"name": "authToken"}).attrs['value']
    #com_val = html.find("input", {"value": "Sign In"}).attrs['value']        

    #print(token)


    login_data = {'logonId': USER,
                  'logonPassword': PASSWORD,
                  'authToken' : token}

    cookies = s.cookies.get_dict()
    # print(cookies)

    # print("___________")
    # print(r0.cookies)

    r1 = s.post('https://www.costco.com/Logon', data = login_data, cookies = cookies, headers = headers)
    print(r1.status_code)

    #r2 = s.get(URL2)
    #print(r2.status_code)
    #print(r2.content)

    r3 = s.get(URL3, cookies = cookies, headers = headers, verify = True)
    print(r3.status_code)
    print(r3.content)
