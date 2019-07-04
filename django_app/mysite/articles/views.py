from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup 
from .models import Article, Site
# Create your views here.
def generate_ultiworld_articles():
	URL = "http://www.ultiworld.com"
	r = requests.get(URL) 
	soup = BeautifulSoup(r.content, 'html5lib')
	articles = []
	table =	soup.find('ol', attrs = {'id': 'news'})
	for i in table.findAll('li', attrs = {'class':'component-list__item collection-tag'}):
		for j in i.findAll('ul', attrs = {'class':'collection-tag__primary'}):
			for k in j.findAll('h3'):
				new_article = {}
				new_article['href'] = k.a['href']
				new_article['text'] = k.a.contents[0]
				# here get site info from href
				new_article['site_info'] = 'ultiworld.com'
# insert table1 (approvaldate)
#       values (convert(datetime,'18-06-12 10:34:09 PM',5));
				new_article['pub_date'] = '18-06-12 10:34:09 PM'
				articles.append(new_article)
	for i in table.findAll('li', attrs = {'class':'component-list__item snippet-background'}):
		for j in i.find_all('a', href=True):
			new_article = {}
			new_article['href'] = j['href']
			new_article['text'] = j.findAll('h2', attrs = {'class':'snippet-background__heading'})[0]
			# here get site info from href
			new_article['site_info'] = 'ultiworld.com'
			new_article['pub_date'] = '18-06-12 10:34:09 PM'
			articles.append(new_article)
	return articles

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)

def results(request, article_id):
    response = "You're looking at the results of article %s."
    return HttpResponse(response % article_id)

def index(request):
	# here also display article info
    ret = generate_ultiworld_articles()
    #latest_articles = Article.objects.order_by('-pub_date')[:5]
    #output = ', '.join([a.text for a in latest_articles])
    #return HttpResponse(ret)
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_articles': latest_articles}
    #return HttpResponse(template.render(context, request))
    return render(request, 'articles/index.html', context)
