import urllib.request, json
from .models import News, Sources


api_key = None
base_url = None
sources_url = None

def configure_request(app):
    global api_key, base_url, sources_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]
    sources_url = app.config["NEWS_SOURCES_API"]
    
def get_news(category):
    """Function that gets the json response to our url request"""
    get_news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
            
    return news_results

    
def process_results(news_list):
    """
    Function to process the news result and then to a list of objects
    Args:
        news_list: A list of dictionaries containing news list
        
    Returns: 
        news_list: A list of news objects
    """
    
    news_result = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        
        news_object = News(id, name, author, title, description, url, urlToImage, publishedAt, content)
        news_result.append(news_object)
            
    return news_result

def get_sources(sources):
    """Function that gets the json response to our url request"""
    get_sources_url = sources_url.format(sources, api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_results = None
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            
    return sources_results

    
def process_sources_results(sources_list):
    """
    Function to process the source result and then to a list of objects
    Args:
        sources_list: A list of dictionaries containing source list
        
    Returns: 
        source_list: A list of news sources objects
    """
        
    sources_result = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        language = source_item.get('language')
        
        sources_object = Sources(id, name, description, url, category, country, language)
        sources_result.append(sources_object)
            
    return sources_result

