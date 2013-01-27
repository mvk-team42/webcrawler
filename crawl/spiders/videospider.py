from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from crawl.items import VideoItem

class VideoSpider(CrawlSpider):
   name = "vid"
   allowed_domains = ["youtube.com"]
   start_urls = [
           "http://www.youtube.com/charts/videos_views?t=a",
   ]

   print "Starting..."

   rules = (
        Rule(SgmlLinkExtractor(allow=('watch\?v=.*', )), callback='parse_item'),
   )

   def parse_item(self, response):
      print 'Response from' + response.url
      hxs = HtmlXPathSelector(response)
      item = VideoItem()
      item['title'] = hxs.select('//title/text()').extract()

      comments = hxs.select('//li[@class="comment" and @data-tag="top"]')
      if len(comments) > 0:
          item['top_comment'] = comments[0].select('.//div[@class="comment-text"]/p/text()').extract()

      return item
