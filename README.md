#### 1. 爬虫目的
找合适的房子不容易？

您不想花钱找中介？

豆瓣租房的信息也许是目前都市白领的最好的选择之一

此爬虫能够获取豆瓣第一手的租房信息

并且把**当天的**租房信息发送邮件通知您

让您无需担心错过任何一个优质租房信息


#### 2. 如何运行
2.1 修改settings.py的邮箱配置信息
* SENDER：邮件发送者
* PASSWORD：SENDER的密码。这里使用的是授权码，授权码是QQ邮件推出用于登录第三方客户端的专用密码，详情：https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
* RECEIVER：邮件接收者
* MAIL_HOST：SMTP服务器

2.2 修改settings.py的爬虫配置信息
* INIT_URL：搜索API。默认是上海租房小组的搜索API，**如果你需要的是上海租房信息，无需更改**
* KEYWORDS：搜索关键词。支持多个关键词
* SLEEP_TIME：爬虫工作的时间间隔。建议使用默认的60s，太高频会触发反爬虫机制

2.3 运行环境
* python版本：python3.6
* 安装依赖：执行命令 `pip install -r requirements.txt`

2.4 启动爬虫
* 执行命令 `python main.py`
