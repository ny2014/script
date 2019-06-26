from requests import session
from bs4 import BeautifulSoup as bs

USER = 'USERNAME HERE'
PASSWORD = 'PASSWORD HERE'

URL1 = 'https://github.com/session'
URL2 = 'https://github.com/'


with session() as s:

    req = s.get(URL1).text
    html = bs(req, features="lxml")
    token = html.find("input", {"name": "authenticity_token"}).attrs['value']
    com_val = html.find("input", {"name": "commit"}).attrs['value']        

    login_data = {'login': USER,
                  'password': PASSWORD,
                  'commit' : com_val,
                  'authenticity_token' : token}

    r1 = s.post(URL1, data = login_data)
    #print(r1.status_code)

    r2 = s.get(URL2)
    print(r2.status_code)
    print(r2.content)
