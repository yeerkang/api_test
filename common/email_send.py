import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


def send_email(filepath):

    # 第一步 连接smtp服务器
    s = smtplib.SMTP()
    s.connect('smtp.qq.com',25)

    # 第二步 登录到smtp服务器
    user = '413536502@qq.com'
    pwd = 'xnjcgomhbautbheb'
    s.login(user=user,password=pwd)
    # 第三步 发送邮件

    # 1.构建邮件
    content = '测试报告'
    text_content = MIMEText(content,_charset='utf8')
    # 构建附件
    part = MIMEApplication(open(filepath,'rb').read(),_subtype = False)
    part.add_header('content-disposition','attachment',filename='测试报告附件.html')
    # 封装一封邮件
    msg = MIMEMultipart()
    # 加入附件和文本内容
    msg.attach(text_content)
    msg.attach(part)
    # 发件人
    msg['From'] = '413536502@qq.com'
    # 收件人
    msg['To'] = 'yeerkang@qiakr.com'
    # 邮件主题
    msg['Subject'] = Header('测试报告','utf8')

    # 2.发送邮件
    s.sendmail(from_addr='413536502@qq.com',to_addrs='yeerkang@qiakr.com',msg=msg.as_string())


if __name__ == '__main__':
    send_email('report.html')