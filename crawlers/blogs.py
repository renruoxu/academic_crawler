import scrapy

class GoogleBlog(scrapy.Spider):
    """Crawler for Google Blog"""
    name = "GoogleBlog"
    start_urls = ['https://ai.googleblog.com/']

    def parse(self, response):
        ARTICLE_SELECTOR = 'div.post'
        for article in response.css(ARTICLE_SELECTOR):
            title = article.css('.title a::text').extract_first().strip()
            url = article.css('.title a::attr(href)').extract_first().strip()
            yield {
                "title": title,
                "url": url,
                "tag": "Google",
                "topic": "blog"
            }

class OpenAI(scrapy.Spider):
    """Crawler for OpenAI"""
    name = "OpenAI"
    start_urls = ["https://blog.openai.com/"]

    def parse(self, response):
        for card in response.css('a.Shared-Card-anchor'):
            title = card.css('.Shared-Card-title::text').extract_first()
            url = card.css('a::attr(href)').extract_first()
            if title and url:
                yield {
                    "title": title.strip(),
                    "url": "https://blog.openai.com/{}".format(url),
                    "tag": "OpenAI",
                    "topic": "blog"
                }


class DeepMind(scrapy.Spider):
    """Crawler for DeepMind"""
    name = "DeepMind"
    start_urls = ["https://deepmind.com/blog/"]

    def parse(self, response):
        for article in response.css('article'):
            url = article.css('a.faux-link-block--link::attr(href)').extract_first().strip()
            title = article.css('a.faux-link-block--link::text').extract_first().strip()
            if title and url:
                yield {
                    "title": title.strip(),
                    "url": "https://deepmind.com/{}".format(url),
                    "tag": "DeepMind",
                    "topic": "blog"
                }


class Uber(scrapy.Spider):
    """Crawler for Uber blogs"""
    name = "Uber"
    start_urls = ["https://eng.uber.com/tag/uber-ai-labs/"]

    def parse(self, response):
        pattern = "//h3[contains(@class, 'entry-title') and contains(@class, 'td-module-title')]"
        for article in response.xpath(pattern):
            url = article.css('a::attr(href)').extract_first()
            title = article.css('a::attr(title)').extract_first()
            if title and url:
                yield {
                    "title": title.strip(),
                    "url": url.strip(),
                    "tag": "Uber",
                    "topic": "blog"
                }
