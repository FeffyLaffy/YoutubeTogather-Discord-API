import requests
import json

f = open('config.json')
try:
    login = json.load(f)
    email, password=login['email'], login['password']
except json.JSONDecodeError:
    email, password=input('email: '), input('password: ')
    p = open("config.json", "w")
    login={"email": email, "password": password}
    json.dump(login, p) 


voic=input("Put channel id: ")
url2=f'https://discord.com/api/v8/channels/{voic}/invites' #create invite discord API v8

aaa=None

def getyt(aaa):
    print(aaa)
    data = {'max_age': 20, 'max_uses': 3, 'target_application_id': '880218394199220334', 'target_type': 2, 'temporary': False, 'validate': None} #max_uses=max number of times this invite can be used, target_application_id=the embedded application to open for this voice channel embedded application invite check out https://github.com/NotKonishi/YoutubeTogather-Discord-API/blob/main/activity.txt for more infomation, target_type=the type of target for this voice channel invite
    ab=requests.post(url2, json=data, headers={'Authorization': f'{aaa}'})
    ca=json.loads(ab.text)
    print('https://discord.gg/' + ca['code']) #result out here

url="https://discord.com/api/v9/auth/login" #login account discord API v9
a=requests.post(url, json={'login': email, 'password': password, 'undelete': False, 'captcha_key': None})
data2 = json.loads(a.text)
print(a.text)
aaa=data2['token']
if aaa is None:
    url3='https://discord.com/api/v9/auth/mfa/totp' #sending code 2FA discord API v9 
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


