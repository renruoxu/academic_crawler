# crawl title and url from googleAI blogs
# ------------------------------
# Author: Ruoxu Ren
# email: renruoxu@gmail.com
# -------------------------------
# To run the script
# scrapy runspider google_blog.py -o google.json
import scrapy

class GoogleBlog(scrapy.Spider):
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
                "tag": "Google"
            }
