import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_msg = """
<h2 style="color:#f00">Python自动发邮件测试</h2>
<p><a href="https://zhuanlan.zhihu.com/p/96005568?utm_campaign=shareopn&utm_medium=social&utm_oi=738424084966146048&utm_psn=1565441964052283393&utm_source=wechat_session">点我看看</a></p>
"""
utf_str = 'utf-8'
message = MIMEText(mail_msg, 'html', utf_str) \
    # 发件人名字
message['From'] = Header('Lgting', utf_str)
# 收件人名字
message['To'] = Header("小可爱", utf_str)
# 邮件标题
subject = 'Python自动发送的邮件'
message['Subject'] = Header(subject, utf_str)

# 发送方
sender = '1422284373@qq.com'
# 接收方
receivers = ['lengxihan77@163.com']
# qq邮箱地址和端口号
smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
# 发动邮箱的SMTP密码
smtpObj.login(sender, 'gusdjizfsmxgidea')
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("成功")
