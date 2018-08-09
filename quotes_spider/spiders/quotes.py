# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        #h1_tags=response.xpath('//h1/a/text()').extract_first()
        #tags= response.xpath('//*[@class="tag-item"]/a/text()').extract_first()
        #yield{"h1_tags":h1_tags,"tags":tags}
        quotes=response.xpath('//*[@class="quote"]')
        for q in quotes:
            text=q.xpath('.//*[@class="text"]/text()').extract_first()
            auth=q.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags=q.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
            print("""******************************************""")
            yield{'text':text,
            'author':auth,
            'tags':tags}
            print("******************************************")


        next_page_url=response.xpath('.//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url=response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)    