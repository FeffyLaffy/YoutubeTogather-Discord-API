from itsdangerous import NoneAlgorithm
import requests
import json
import webbrowser

f = open('config.json')
try:
    login = json.load(f)
    email, password=login['email'], login['password']
except json.JSONDecodeError:
    email, password=input('email: '), input('password: ')
    p = open("config.json", "w")
    login={"email": email, "password": password}
    p.write(str(login))

voic=input("Put channel id: ")
url2=f'https://discord.com/api/v8/channels/{voic}/invites'

aaa=None

def getyt(aaa):
    print(aaa)
    data = {'max_age': 20, 'max_uses': 3, 'target_application_id': '880218394199220334', 'target_type': 2, 'temporary': False, 'validate': None}
    ab=requests.post(url2, json=data, headers={'Authorization': f'{aaa}'})
    ca=json.loads(ab.text)
    print('https://discord.gg/' + ca['code'])


url="https://discord.com/api/v9/auth/login"
a=requests.post(url, json={'login': email, 'password': password, 'undelete': False, 'captcha_key': None})
data2 = json.loads(a.text)
print(a.text)
aaa=data2['token']
if aaa is None:
    url3='https://discord.com/api/v9/auth/mfa/totp'
    code=input("mfa code: ")
    try:
        pa=requests.post(url3, json={'code': code, 'gift_code_sku_id': None, 'login_source': None, 'ticket': data2['ticket']})
        data22 = json.loads(pa.text)
        aaa=data22['token']
        getyt(aaa)
    except:
        print("error return not int")
else:
    getyt(aaa)


