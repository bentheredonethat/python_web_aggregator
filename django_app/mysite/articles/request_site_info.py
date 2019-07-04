import requests 
from bs4 import BeautifulSoup 

import datetime
'''
fields needed from model:
	text (link) - done
	title - done
	pub_date -- need this
	site_name -- infer this from link
'''

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
my_ultiworld_articles = generate_ultiworld_articles()
#print ("a = Article(pub_date=\""+pub_date=timezone.now())
print("a_pub_date=\""+str(datetime.datetime.now())+"\"")

for i in my_ultiworld_articles:
#print("a_pub_date="+str(datetime.datetime.now()))
	print("a_href=\""+i['href']+"\"")
	i['text'] = i['text'].string.strip()
	print("a_text=\""+repr(i['text'])+"\"")
	print("a = Article( text=a_href, title=a_text, pub_date=a_pub_date, site_id=s)")
	print("a.save()")

