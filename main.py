from sys import argv
from urllib import request


API_KEY =  # API key

URL = ('https://newsapi.org/v2/top-headlines?') # URL for API

# Parameters for API
def get_category(category):
    parameters = {
        'category': category,
        'sortBy': 'popularity',
        'country': 'us',
        'apiKey': API_KEY
    }
    return get_news(parameters) # Get news

def get_sources(sources):
    parameters = {
        'sources': sources,
        'sortBy': 'popularity',
        'apiKey': API_KEY
    }
    return get_news(parameters) # Get news

def get_everything(query):
    parameters = {
        'q': query,
        'sortBy': 'popularity',
        'apiKey': API_KEY
    }
    return get_news(parameters) # Get news


# Get the news
def get_news(parameters):
    response = request.get(URL, params=parameters) # Get response from API
    articles = response.json()['articles'] # Get articles from response

    results = [] 

    for article in articles: 
        result.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'urlToImage': article['urlToImage']
        })
    
    for result in results: 
        print(result['title'])
        print(result['description'])
        print(result['url'])
        print(result['urlToImage'])
        print('-------------------')


if __name__ == "__main__":
    print(f'Getting news for {argv[1]}...') # Get news for category
    get_category(argv[1]) # Get category from command line
    print('Done!') # Done getting news
    get_everything
    get_sources
    
    