import json
from newsapi import NewsApiClient
from utils import *

newsapi = NewsApiClient(api_key='a58184c8b6014a9ea17772a36ff15f01')


def get_headlines(country, category='general', sources=None, pageSize=20, page=None, keyword=None,):
    '''
    This function is used to get the news headlines.

    Arguments:
    q - (str) Keywords or a phrase to search for.
    country - (str) The 2-letter ISO 3166-1 code of the country you want to get headlines for. Only one optionshould be choosen. Possible options are: ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
    Note: you can't mix this param with the sources param

    category - (str) The category you want to get headlines for. Possible options are: ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    Note: you can't mix this param with the sources param

    sources - (list) A list of identifiers for the news sources or blogs you want headlines from.

    pageSize - (int) The number of results to return per page (request). 20 is the default, 100 is the maximum.

    page - (int) Use this to page through the results if the total results found is greater than the page size.


    Returns:
    status - (str) The status of the request. 'ok' if the request is processed and  'error' if any error occurs.
    articles - (dict) All the articles.

    '''
    try:
        sources = list_to_csv(sources)

        if sources:
            country = None
            category = None

        headlines = newsapi.get_top_headlines(q=keyword,
                                                country=country,
                                                category=category,
                                                sources=sources)
        status = headlines['status']
        articles = headlines['articles']

        return status, articles
    except:
        status = 'error'
        articles = None
        return status, articles


'''
Example:
status, articles = get_headlines('us', category='general', sources=None)
'''