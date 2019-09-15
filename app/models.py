class NewsArticle:
    """
    News article class
    """

    def __init__(self, source,title,author,description,picture,time,link):
        self.source = source
        self.title= title
        self.author = author
        self.description = description
        self.picture = picture
        self.time = time
        self.link = link


class NewsSource:
    """
    News source class
    """

    def __init__(self, name, link, category):
        self.name = name
        self.link = link
        self.category = category

class NewsItem:
    """
    News item for display of cual news article
    """

    def __init__(self, title, picture, article, source):
        self.title = title
        self.picture = picture
        self.article = article
        self.source = source