# -*- coding: utf-8 -*-
import scrapy
from icomic.items import IcomicItem

class IcomicSpiderSpider(scrapy.Spider):
    # 爬虫名不能与项目名重复
    name = 'icomic_spider'
    # 允许的域名
    allowed_domains = ['www.manhuatai.com']
    # 入口url,扔到调度器Url
    start_urls = ['https://www.manhuatai.com/sort']

    # 返回数据
    def parse(self, response):
        print(response)
        comic_list = response.xpath("//div[@id='J_comicListBox']//ul//li")
        for item in comic_list:
            icomic_item = IcomicItem()
            comic_name = item.xpath(".//h3[@class='acgn-title']//a//text()").extract_first()
            comic_home_url = item.xpath(".//h3[@class='acgn-title']//a//@href").extract_first()
            comic_home_image = item.xpath(".//a//img//@data-src").extract_first()
            icomic_item['comicName'] = comic_name
            icomic_item['comicHomeImage'] = comic_home_image
            icomic_item['comicHomeUrl'] = comic_home_url
            # 传输数据到piplines 管道
            yield icomic_item
        next_link = response.xpath("//div[@class='acgn-pages acgn-mb24 J_pages']//a[@class='acgn-next']//@href").extract()
        print(next_link)
        # if next_link:
        #     next_link = next_link[0]
        #     yield scrapy.Request("https://www.manhuatai.com/" + next_link, callback=self.parse)
