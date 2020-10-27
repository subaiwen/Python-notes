import requests
import re

#v2ray
url_list = ['https://github.com/bannedbook/fanqiang/wiki/v2ray免费账号', 
            'https://github.com/iwxf/free-v2ray']

def spider(url):
    '''
    scrpe list of sub-link from a url
    :param: url
    :return: sub_list: list of sub-links
    '''
    res = requests.get(url)
    content = res.text

    pattern = 'vmess://.+?[^<]+'
    v2ray_list = re.findall(pattern, content) # re.search() return the first occurence
    v2ray_list = [re.sub('<.+?>', '', i) for i in v2ray_list]
    sub_list = []
    # apply when a str contains links split by \n
    for v2ray_str in v2ray_list:
        v2ray_str_list = [i for i in re.split('(\n)', v2ray_str) if i != '\n'] # remove an unexist element will raise error
        sub_list = sub_list + v2ray_str_list
    return sub_list

sub_link_list = []
for url in url_list:
    sub_link_list = sub_link_list + spider(url)
    
for sub_link in sub_link_list:
    print('\n' + sub_link)
