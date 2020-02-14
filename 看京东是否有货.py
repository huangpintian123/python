
import requests
import time

# 有货通知 收件邮箱
mail = '1006551791@qq.com'
# 商品的url, 进入网页，develop工具，Network类别，找到Stock开头的，然后按Header，那里的URL就是商品url
url = [
    'https://c0.3.cn/stock?skuId=100006252957&area=10_742_746_52348&venderId=1000146882&buyNum=1&choseSuitSkuIds=&cat=9855,9858,9924&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=15816407319111825154169&ch=1&callback=jQuery2284359'
]


def sendMail(url):
    import smtplib
    from email.mime.text import MIMEText
    # email 用于构建邮件内容
    from email.header import Header

    # 用于构建邮件头

    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '1294321305@qq.com'
    password = 'lamborghiniLP700'

    # 收信方邮箱
    to_addr = mail

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(url + ' 有口罩啦', 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('有口罩啦')

    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


flag = 0
while (1):
    try:

        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Connection": "keep-alive"
        }
        print('第' + str(flag) + '次 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        flag += 1
        for i in url:
            # 商品url
            skuidUrl = 'https://item.jd.com/' + i.split('skuId=')[1].split('&')[0] + '.html'
            response = session.get(i)
            # print('有货啦! 有货啦! 有货啦! ： ' + skuidUrl)
            # sendMail(skuidUrl)
            if (response.text.find('无货') > 0):
                print('无货 ： ' + skuidUrl)
            else:
                print('有货啦! 有货啦! 有货啦! ： ' + skuidUrl)
                sendMail(skuidUrl)

        time.sleep(5)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        print('异常')
        time.sleep(10)
