import scrapy

class QuotesSpider(scrapy.spider):
	"""docstring for QuotesSpider"""
	#name unique for spider
	name = "quotes"


	def __init__(self, arg):
		super(QuotesSpider, self).__init__()
		self.arg = arg
		
   #Returns an iterable of requests
	def startRequests(self):
		urls = [
   			'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
		]

		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
      page = response.url.split("/")[-2]
      filename = 'quotes-%s.html' % page
      with open(filename, 'wb') as f:
      f.write(response.body)
      self.log('Saved file %s' % filename)