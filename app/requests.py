import urllib.request, json

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]
    
def get_news():
    """Function that gets the json response to our url request"""
    get_news_url = base_url.format(api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['results']:
            news_results_list = get_news_response['results']
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
    
    news_list = []
    pass