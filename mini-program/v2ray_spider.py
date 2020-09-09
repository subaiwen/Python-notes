import requests
import re

url = 'https://github.com/bannedbook/fanqiang/wiki/v2ray免费账号' #v2ray
url2 = 'https://github.com/bannedbook/fanqiang/' #翻墙信息网

res = requests.get(url)
content = res.text

pattern = '<p>vmess.+?</p>'
v2ray_url = re.findall(pattern, content) # re.search() return the first occurence
v2ray = [re.sub('<.+?>', '', i) for i in v2ray_url]

for i in v2ray:
    print('\n' + i)
