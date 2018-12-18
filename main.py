import json, re
from twisted.internet import reactor
from flask import Flask, render_template, request, jsonify
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from crawlers.blogs import GoogleBlog, OpenAI, DeepMind, Uber

DATA_FILE = "data/result.json"
PORT = 8889
TEMPLATE = "index.html"

app = Flask(__name__)

def crawl():
    """Crawl data for the blog"""
    # blog crawler
    runner = CrawlerRunner(
        {
            'FEED_FORMAT': 'json',
            'FEED_URI': DATA_FILE,
        }
    )
    runner.crawl(GoogleBlog)
    runner.crawl(OpenAI)
    runner.crawl(DeepMind)
    runner.crawl(Uber)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()

def load_data():
    """Load crawled data"""
    with open(DATA_FILE, "r") as f:
        blogs = f.read()
        blogs = blogs.replace("][", ",")
        # with open(DATA_FILE, "w") as f:
        #     f.write(blogs)
        print blogs
        blogs = json.loads(blogs)
    return blogs


@app.route("/")
def index():
    print blogs
    return render_template(TEMPLATE, blogs=blogs)

if __name__ == "__main__":
    # crawl data
    crawl()
    blogs = load_data()
    app.run(host='0.0.0.0', port=PORT, debug=True)


 