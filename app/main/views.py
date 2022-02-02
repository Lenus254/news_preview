from . import main
from flask import render_template, request, redirect, url_for
from ..requests import get_source, article_source, display_source


# our views
@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source = get_source()

    cnn=display_source('cnn')

    return render_template('index.html', sources=source, results=cnn)


@main.route('/article/<id>')
def article(id):
    '''
    View article page function that returns the various article details page and its data
    '''

    articles = article_source(id)
    return render_template('article.html', articles=articles)

