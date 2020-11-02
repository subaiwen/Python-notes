import logging
import smtplib, ssl

from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from email.header import make_header

from dotenv import load_dotenv
import os
load_dotenv()
psw = os.getenv('psw')

subject = 'This is subject'
body = '''\
This is body
'''
send_from = 'lausang@foxmail.com'
send_to = 'p1047254574@icloud.com' # wjzf@gzcb.com.cn
cc = '446885833@qq.com'
files = None # '/Users/liubeixi/Desktop/Python-notes/mini-program/问题归纳.docx' 

def file_collector():
    files = []
    print('input the absolute path of your attachments one by one')
    while True:
        file = input('>> ')
        if file == '':
            break
        files.append(file) # append会修改files本身，并且返回None。不能把返回值再赋值给files。

    return(files)

def header_checker(header_element):
    if header_element is None:
        x = [] 
    elif type(header_element) is str:
        x = [header_element]
    else:
        x = header_element
    return(x)

def send_mail(send_from=send_from, send_to=send_to, cc=cc, password=psw, subject=subject, body=body, files=files):
    '''
    send email through SMTP SSL
    Note: Don't add bcc header, it will disable the cc functionality. The rest of send_list will become bcc list!
    '''
    # header verification
    send_to = header_checker(send_to) 
    cc = header_checker(cc)
    files = header_checker(files)
 
    send_list = send_to + cc

    # Create a multipart message and set headers: should be str seperated by commas
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to) 
    msg['Cc'] = COMMASPACE.join(cc)
    msg['Subject'] = subject
    # msg['Date'] = '' formatdate(localtime=True)
    msg.attach(MIMEText(body, 'plain')) # Add body to email

    # Open file in binary mode
    for filepath in files or []:
        exist = os.path.exists(filepath)
        if exist:
            with open(filepath, 'rb') as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                filename = basename(filepath)
                part = MIMEApplication(
                            attachment.read(),
                            Name=filename
                        )
                # Add header as key/value pair to attachment part
                part['Content-Disposition'] = f'attachment; filename={make_header([(filename, "UTF-8")]).encode("UTF-8")}' 
                # Add attachment to message
                msg.attach(part)
        else:
            print(f'Attachment path {filepath} does not exist')

    try:
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.qq.com', 465, context=context) as server:
            # 使用SSL的通用配置如下：
            # 接收邮件服务器：pop.qq.com，使用SSL，端口号995
            # 发送邮件服务器：smtp.qq.com，使用SSL，端口号465或587
            # 账户名：您的QQ邮箱账户名（如果您是VIP帐号或Foxmail帐号，账户名需要填写完整的邮件地址）
            # 密码：您的QQ邮箱密码
            server.login(send_from, password)
            server.sendmail(from_addr=send_from, to_addrs=send_list, msg=msg.as_string())
            print('Successfully sent email')
    except Exception as e:
        raise e

if __name__=='__main__':
    send_mail()

# reference:
# https://docs.python.org/2/library/email.html
# https://stackoverflow.com/questions/3362600/how-to-send-email-attachments

