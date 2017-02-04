import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://api.edmunds.com/v1/content/editorreviews?make=honda&model=accord&year=2013&fmt=json&api_key=sv3ga54hu77qybtxamykpbdg
',
        ]


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())

		makes = json_response['makes'];
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

		#wb is write and binary
        self.log('Saved file %s' % filename)
