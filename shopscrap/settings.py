# -*- coding: utf-8 -*-

# Scrapy settings for shopscrap project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'shopscrap'

SPIDER_MODULES = ['shopscrap.spiders']
NEWSPIDER_MODULE = 'shopscrap.spiders'


SPLASH_URL = 'http://0.0.0.0:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # middleware id for proxy_pool
    # 'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    # 'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620
    # middleware id for user_agent_pool
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

# USER_AGENTS = [
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/57.0.2987.110 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/61.0.3163.79 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
#      'Gecko/20100101 '
#      'Firefox/55.0'),  # firefox
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/61.0.3163.91 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/62.0.3202.89 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/63.0.3239.108 '
#      'Safari/537.36'),  # chrome
# ]

CONNECTION_STRING = "{drivername}://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8".format(
    drivername="mysql",
    user="root",
    passwd="",
    host="localhost",
    port="3306",
    db_name="shopscrapdb",
)

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shopscrap (+http://www.yourdomain.com)'
USER_AGENT =  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/80.0.3987.163 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# proxys enabled
#PROXY_POOL_ENABLED = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'shopscrap.middlewares.ShopscrapSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'shopscrap.middlewares.ShopscrapDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'shopscrap.pipelines.Default_Values': 200,
   'shopscrap.pipelines.ShopScrapdb': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
