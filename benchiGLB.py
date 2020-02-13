# -*- coding: utf-8 -*-
import scrapy
from bmw_lianxi.items import BmwLianxiItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class BenchiglbSpider(CrawlSpider):
    name = 'benchiGLB'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/5348.html#pvareaid=3454438']
    #rules元组如果只有一项必须给个逗号
    rules = (
        #允许详情页图片域名
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series/5348.+"),callback="parse_page",follow=True),
    )

    def parse_page(self, response):
        # uiboxs = response.xpath("//div[@class='uibox']")[1:]
        # for uibox in uiboxs:
        #     title = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
        #     urls = uibox.xpath(".//ul/li/a/img/@src").getall()
        #     urls = list(map(lambda url:response.urljoin(url),urls))#先遍历urls，将url传递给response.urljoin，通过这个函数将url补全，返回一个新的url，这时候的url是个map对象。再将map对象转换成list
        #     print(urls)
        #     item = BmwLianxiItem(title=title,urls=urls)
        #     yield item
        #获取分类
        title = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/text()").get()
        #获取图片url
        urls = response.xpath("//div[contains(@class,uibox-con)]/ul/li//img/@src").getall()
        #将图片中的部分url替换掉就是高清图
        urls = list(map(lambda x:x.replace("240x180_0_q95_c42_",""),urls))
        #将新的url通过urljoin方法补全
        urls = list(map(lambda x:response.urljoin(x),urls))
        #返回爬取的值
        yield BmwLianxiItem(title=title,urls=urls)






