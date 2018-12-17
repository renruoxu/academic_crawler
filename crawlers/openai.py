import scrapy

class OpenAI(scrapy.Spider):
    name = "OpenAI"
    start_urls = ["https://blog.openai.com/"]

    def parse(self, response):
        for card in response.css('a.Shared-Card-anchor'):
            title = card.css('.Shared-Card-title::text').extract_first()
            url = card.css('a::attr(href)').extract_first()
            if title and url:
                yield {
                    "title": title.strip(),
                    "url": "https://blog.openai.com/{}".format(url)
                }