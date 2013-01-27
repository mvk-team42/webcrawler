from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from crawl.items import VideoItem

class VideoSpider(BaseSpider):
   name = "vid"
   allowed_domains = ["youtube.com"]
   start_urls = [
           "http://www.youtube.com/charts/videos_views?t=a&gl=US",
   ]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       videos = hxs.select('//div[@class="video-data"]')
       items = []
       for video in videos:
           item = VideoItem()
           item['title'] = video.select('./a[@class="video-title ellipsis"]/text()').extract()
           item['views'] = video.select('.//span[@class="viewcount"]/text()').extract()
           items.append(item)
       return items
