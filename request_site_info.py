import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.ultiworld.com"



def generate_ultiworld_articles(URL):
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
					articles.append(new_article)
		 
		#print articles		
		for i in table.findAll('li', attrs = {'class':'component-list__item snippet-background'}):
			for j in i.find_all('a', href=True):
		#		print j['href']
		#		print j.findAll('h2', attrs = {'class':'snippet-background__heading'})[0]
				new_article = {}
				new_article['href'] = j['href']
				new_article['text'] = j.findAll('h2', attrs = {'class':'snippet-background__heading'})[0]
				articles.append(new_article)
		return articles

my_ultiworld_articles = generate_ultiworld_articles(URL)
