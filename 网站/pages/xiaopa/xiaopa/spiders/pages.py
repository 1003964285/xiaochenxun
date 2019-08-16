# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class PagesSpider(scrapy.Spider):
    name = 'pages'  # 爬虫的名称，不可更改
    allowed_domains = ['www.zhipin.com']  # 域名称
    start_urls = ['https://www.zhipin.com/']  # 从这个网址开始执行爬虫，注意默认是http，修改成https
    # scrapy爬虫中不会主动修改页面中的链接，所以自己增加一个类变量用于将相对地址完整成为绝对地址。
    baseurl = 'https://formoon.github.io'

    def parse(self, response):
        # scrapy爬虫主要的难点是xpath和css选择器的使用，请在网上搜索相关资源弄清楚
        # 爬虫使用相关选择器在整个html中定位自己所需要的节点及获取其中的数据
        for i in response.xpath("//div[@class='job-list']//ul//li"):
            # 获取文章链接
            qian = i.xpath(".//span[@class='red']//text()").extract_first()
            # 获取文章标题
            title = i.xpath(".//div[@class='job-title']//text()").extract_first()
            # 显示结果
            print (title,qian)
