import urllib.request
import json
from .models import NewsArticle, NewsSource, NewsItem

api_key = None

base_url = None


def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    source_url = app.config['SOURCES_URL']


def get_news():
    """
    Getting the json response
    :return:
    """
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results= None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

        return news_results


def process_results(news_list):
    """
    Transforms the list into a list of objects
    :param news_list:
    :return:
    """

    news_results = []

    for news_item in news_list:
        source = news_item.get('source.name')
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        picture = news_item.get('urlToImage')
        time = news_item.get('publishedAt')
        link = news_item.get('url')

        news_object = NewsArticle(source, title, author, description, picture, time, link)
        news_results.append(news_object)

    return news_results


def get_sources():
    """
    Gets a list of sources for the news
    :return:
    """

    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources_results= None

        if get_sources_response['sources']:
            news__sources_results_list = get_sources_response['sources']
            news_sources_results = process_source_results(news__sources_results_list)

        return news_sources_results


def process_source_results(source_list):
    """
    Transforms the list into a list of objects
    :param source_list:
    :return:
    """

    news_sources_results = []

    for source_item in source_list:
        name = source_item.get('name')
        link = source_item.get('url')
        category = source_item.get('category')

        news_source_object= NewsSource(name, link, category)
        news_sources_results.append(news_source_object)

    return news_sources_results

