import scrapy

from funds.items import FundsItem


class CunjinbaoSpider(scrapy.Spider):
    name="cunjinbao"
    start_urls=['http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=000930&page=1&per=1000&sdate=&edate=']

    def parse(self, response):
        item=FundsItem()
        selector=scrapy.Selector(response)
        total = selector.xpath('//table[@class="w782 comm lsjz"]/tbody/tr')
        for each in total:
            item['date']=each.xpath('td/text()').extract()[0]
            item['perPrice']=each.xpath('td/text()').extract()[1]
            item['totalPrice']=each.xpath('td/text()').extract()[2]
            yield item
