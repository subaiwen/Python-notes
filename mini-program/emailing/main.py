import utils

subject = 'subject'
body = '''\
你好，

麻烦将附件转发到：

receiver@name.com

谢谢
'''
send_from = 'lauXXXX@foxmail.com'
send_to = 'receiver@name.com'
cc = None # 'usr@qq.com'
files = utils.file_collector() # None 

utils.send_mail(send_from=send_from, send_to=send_to, cc=cc, subject=subject, body=body, files=files)