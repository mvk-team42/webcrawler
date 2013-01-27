from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from crawl.items import VideoItem

class VideoSpider(CrawlSpider):
   name = "vid"
   allowed_domains = ["youtube.com"]
   start_urls = [
           "http://www.youtube.com/charts/videos_views?t=a&gl=US",
   ]

   rules = (
        Rule(SgmlLinkExtractor(allow=('/watch?v=', )), callback='parse_item'),
   )

   def parse_item(self, response):
      self.log('Response from' + response.url)
      hxs = HtmlXPathSelector(response)
      item = VideoItem()
      item['title'] = hxs.select('//title/text()').extract()
      item['top_comment'] = hxs.select('//li[@class="comment" and @data-tag="top"]')[0]
      return item
