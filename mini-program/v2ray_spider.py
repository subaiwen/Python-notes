import requests
import re

#v2ray
url_list = ['https://github.com/bannedbook/fanqiang/wiki/v2ray免费账号', 
            'https://github.com/iwxf/free-v2ray']

def spider(url):
    '''
    url --> list of sub-link
    :param: url
    :return: v2ray_list: list of sub-link
    '''
    res = requests.get(url)
    content = res.text

    pattern = 'vmess://.+?[^<]+'
    v2ray_url = re.findall(pattern, content) # re.search() return the first occurence
    v2ray_list = [re.sub('<.+?>', '', i) for i in v2ray_url]

    return v2ray_list

sub_link_list = []
for url in url_list:
    v2ray_list = spider(url)
    for v2ray in v2ray_list:
        sub_link_list = sub_link_list + [i for i in re.split('(\n)', v2ray) if i != '\n'] # remove '\n'
        # remove an unexist element will raise error
    
for sub_link in sub_link_list:
    print('\n' + sub_link)
