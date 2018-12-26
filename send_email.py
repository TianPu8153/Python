#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
msg_from='2223169731@qq.com'#发送方邮箱
passwd='agrompiskcqheaeb'#填入发送方邮箱的授权码
msg_to='2223169731@qq.com'#收件人邮箱
                            
subject="python邮件测试"#主题     

#msg = MIMEText(content)
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
msg.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……'))
att1 = MIMEText(open(r'C:\Users\Admin\Desktop\中文.txt', 'rb').read(), 'base64', 'utf-8')
#att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字(只能是英文名称)
#att1["Content-Disposition"] = 'attachment; filename="test.txt"'


att1["Content-Type"] = "application/octet-stream"
    # 附件名称为中文时的写法
#att1.add_header("Content-Disposition", u'attachment; filename="测试.txt"')
att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "中文.txt"))



msg.attach(att1)
 
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)#邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print ("发送成功")
except s.SMTPException as e:
    print ("发送失败")
finally:
    s.quit()
