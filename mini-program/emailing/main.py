import utils

subject = 'liuzhijian@gzcb.com.cn'
body = '''\
你好，

麻烦将附件转发到：

liuzhijian@gzcb.com.cn

谢谢
'''
send_from = 'lausang@foxmail.com'
send_to = 'wjzf@gzcb.com.cn'
cc = None # '446885833@qq.com'
files = utils.file_collector() # None 

utils.send_mail(send_from=send_from, send_to=send_to, cc=cc, subject=subject, body=body, files=files)