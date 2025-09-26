# import libraries
from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='bf2089b057d84b63aa07f58fa7d5ec7a')


@app.route('/', methods=['GET'])
def news():
    keyword = request.args.get('keyword')
    if keyword:
        # Search news using NewsAPI everything endpoint
        results = newsapi.get_everything(q=keyword, language='en', sort_by='relevancy')
        articles = results.get('articles', [])
    else:
        # Default top headlines
        results = newsapi.get_top_headlines(sources='bbc-news')
        articles = results.get('articles', [])

    news = [art.get('title') for art in articles]
    desc = [art.get('description') for art in articles]
    img = [art.get('urlToImage') for art in articles]
    link = [art.get('url') for art in articles]

    mylist = zip(news, desc, img, link)
    return render_template('news.html', context=mylist)

if __name__ == '__main__':
   app.run()