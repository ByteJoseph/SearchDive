from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
#from google_search import GoogleSearch
# Create your views here.

def search(request):
    query = request.GET.get('q', '')
    results = []       
    if query:
        response = requests.get('https://api.duckduckgo.com/', params={
            'q': query,
            'format': 'json',
            'no_redirect': 1,
            'no_html': 1,
            'skip_disambig': 1
        })
        data = response.json()

        results = [
            {
                'title': result.get('Text', 'No title'),
                'url': result.get('FirstURL', '#'),
                'favicon': f'https://www.google.com/s2/favicons?domain={result.get("FirstURL", "").split("/")[2]}'
            }
            for result in data.get('RelatedTopics', []) if 'FirstURL' in result
        ]
    
        return render(request, 'home/results.html', {'query': query, 'results': results})
    else:
        return render(request,"home/index.html")
