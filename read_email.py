#!usr/bin/env python
# -*- coding: utf-8 -*-
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import os, sys, string
import poplib
import re
import urllib.request

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
    if pos >= 0:
        charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# indent用于缩进显示:
def print_info(msg, indent=0):
    content=0
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        #for n, part in enumerate(parts):
        #for n, part in enumerate(parts):
        n=1
        print('%d' '%spart %s' % (n,' ' * indent, n))
        print('%d'  '%s--------------------' % (n,' ' * indent))
        content=print_info(parts[0], indent + 1)
            
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
            print('indent=:%d' % (indent))
            
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))
    return content


# pop3服务器地址
host = "pop3.163.com"
# 用户名
username = "djjdjjdjjdjjdjjdjj@163.com"
# 密码
password = ""
# 创建一个pop3对象，这个时候实际上已经连接上服务器了
pp = poplib.POP3(host)
# 设置调试模式，可以看到与服务器的交互信息
pp.set_debuglevel(1)
# 向服务器发送用户名
pp.user(username)
# 向服务器发送密码
pp.pass_(password)
# 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
ret = pp.stat()
print (ret)
# 需要取出所有信件的头部，信件id是从1开始的。
for i in range(1, ret[0]+1):
    # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
    # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
    mlist = pp.top(i, 0)
    print ('line: ', len(mlist[1]))
# 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
ret = pp.list()
print (ret)
# 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
down = pp.retr(2)
print ('lines:', len(down))
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(down[1]).decode('utf-8')
msg = Parser().parsestr(msg_content)
mycontent=print_info(msg)
print('=======%s========' % mycontent)
pp.quit()

p1=r"http.+com"
pattern1=re.compile(p1)
mystr=pattern1.findall(mycontent)
print('%s' % mystr)
url=mystr[0]
# 请求
request = urllib.request.Request(url)
 
# 爬取结果
response = urllib.request.urlopen(request)
 
data = response.read()
 
# 设置解码方式
data = data.decode('utf-8')
 
# 打印结果
print(data)
