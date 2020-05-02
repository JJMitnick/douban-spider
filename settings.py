# -*-coding:utf-8-*-
# @time: 2020/5/2 13:43
# @author: Mitnick
# @description: 配置文件

##
# 邮箱配置信息
##
# 发送者
SENDER = '1258636566@qq.com'
# 授权码
PASSWORD = 'kgnbgyjtbmxjjdag'
# 接收者
RECEIVER = '1209108465@qq.com'
# smtp服务器
MAIL_HOST = "smtp.qq.com"

##
# 爬虫配置信息
##
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
# 搜索的API
INIT_URL = "https://www.douban.com/group/search?cat=1013&group=146409&sort=time&q={0}"
# 需要搜索的关键词
KEYWORDS = ['中山公园', '世纪大道']
# 爬虫休息时间，单位：秒
SLEEP_TIME = 60
