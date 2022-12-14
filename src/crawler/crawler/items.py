import scrapy


class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    timestamp = scrapy.Field()

    title_keywords = scrapy.Field()
    content_keywords = scrapy.Field()

class HankyungItem(ArticleItem):
    pass

class SeoulItem(ArticleItem):
    pass

class FinancialItem(ArticleItem):
    pass

class HeraldItem(ArticleItem):
    pass

class AsiaItem(ArticleItem):
    pass
