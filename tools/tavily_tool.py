from tavily import TavilyClient
from config import TAVILY_API_KEY

client= TavilyClient(api_key=TAVILY_API_KEY)

def tavily_search(query):
    response = client.search(
        query= query,
        max_results=5
    )
    results= []

    for i,r in enumerate(response['results'], 1):
        # title, url, and snippet extraction 
        title = r.get('title', 'Unknown')
        url = r.get('url', '')
        snippet = r.get('content', '').strip()
        if len(snippet) > 200:
            snippet = snippet[:200] + '...'

        results.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}\n")
    return "\n".join(results)