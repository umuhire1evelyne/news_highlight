from flask import render_template
from ..requests import get_news, get_sources
from . import main



@main.route('/')
def index():
    """
    View root page
    :return:
    """

    articles = get_news()
    title = 'highlights - News app'
    return render_template('index.html', title=title , articles = articles)


@main.route('/sources')
def source():
    """
    view sources page
    :return:
    """

    sources = get_sources()
    title = 'News sources - News app'
    return render_template('sources.html', title = title, sources = sources)