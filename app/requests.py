import urllib.request,json
from .sources import Source
from .articles import Articles

# Getting api key
api_key = None
# Getting source url
source_url= None
# Getting source url
cat_url= None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']


def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= 'https://newsapi.org/v2/sources?apiKey=81e26290ed0842708456e1e956750770'
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        title=source_item.get('title')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if name:
            source_object = Source(id,title,name,description,url)
            source_results.append(source_object)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=81e26290ed0842708456e1e956750770'.format(id)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        id = article.get('id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')


        if urlToImage:
            article_objects = Articles(id, author, title, description, url, urlToImage, publishedAt, content)
            article_source_results.append(article_objects)

    return article_source_results

def get_category(cat_name):
    '''
    function that gets the response to the category json
    '''
    get_category_url = cat_url.format(cat_name,api_key)
    print(get_category_url)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles_results(get_cartegory_list)

    return get_cartegory_results

def get_headlines():
    '''
    function that gets the response to the category json
    '''
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    print(get_headlines_url)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results
