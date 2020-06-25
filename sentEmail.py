# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 17:54
# @Author  : ding
# @File    : sentEmail.py

import smtplib
import email.utils
from email.mime.text import MIMEText
from email.header import Header


class Msg(object):
    def __init__(self, zhuangtai, from_addr, to_addrs):
        self.zhuangtai = zhuangtai
        self.from_addr = from_addr
        self.to_addrs = to_addrs
    # def __init__(self, shoujianrendizhi, zhuangtai, addresser='ding',
    #              fajianrendizhi='861276842#qq.com', receiver='ding'):
    #     self.addresser = addresser
    #     self.receiver = receiver
    #     self.fajianrendizhi = fajianrendizhi
    #     self.shoujianrendizhi = shoujianrendizhi
    #     self.zhuangtai = zhuangtai

    def creat_msg(self):
        # Creat mail information
        # msg = MIMEText(self.zhuangtai, 'plain', 'utf-8')
        # msg['From'] = email.utils.formataddr((self.addresser, '861276842@qq.com'))
        # msg['To'] = email.utils.formataddr((self.receiver, '1099102769@qq.com'))
        # msg['Subject'] = self.zhuangtai
        msg = MIMEText('2020/6/3日数据入库情况：河道水文站 1230/1230，水库水文站 590/590，雨量站 720/720', 'plain', 'utf-8')
        msg['From'] = Header(self.from_addr)
        msg['TO'] = Header(",".join(self.to_addrs))
        msg['Subject'] = Header(self.zhuangtai)

        return msg


class EmailServer():
    def __init__(self):
        pass

    @staticmethod
    def config_server():
        # Configure mailbox
        config = dict()
        config['send_email'] = '861276842@qq.com'
        config['passwd'] = 'jhsvuvkeorogbbjd'

        config['smtp_server'] = 'smtp.qq.com'  # 设置服务器
        config['target_email'] = ['1099102769@qq.com, 861276842@qq.com']
        return config

    def send_email(self):
        # Use smtp to send email to the target mailbox
        config = self.config_server()
        msg1 = Msg(zhuangtai='成功', from_addr=config['send_email'], to_addrs=config['target_email'])
        msg = msg1.creat_msg()

        server = smtplib.SMTP_SSL(host=config['smtp_server'])
        server.connect(host=config['smtp_server'], port=465)
        server.login(user=config['send_email'], password=config['passwd'])
        server.set_debuglevel(True)

        try:
            server.sendmail(config['send_email'],
                            config['target_email'],
                            msg.as_string())
        finally:
            server.quit()


if __name__ == '__main__':
    emailServer = EmailServer()
    emailServer.send_email()
