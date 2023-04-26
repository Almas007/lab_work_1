import requests
from bs4 import BeautifulSoup
from datetime import datetime
from parcers_v1.models import Resource, Items

def parce_new_from_resource(res_id:int, main_url:str, top_tag:str, bottom_tag:str, title_cut:str, date_cut:str):
    
    
    def parce_news(res_id:int, url:str, bottom_tag:str, title_cut:str, date_cut:str):
        soup_news = BeautifulSoup(requests.get(url).text, 'html')
        title = soup_news.find('div', class_ = title_cut).text        
        content = soup_news.find(bottom_tag).text
        date = soup_news.find('div', class_ = date_cut).text
        Items.objects.create(res_id=res_id, link=url, title=title, content=content, nd_date=date, s_date=date, not_date=date)
    
    soup = BeautifulSoup(requests.get(main_url).text, 'html')
    for i in soup.find_all('a', class_ = top_tag):
        url = i.get('href')
        parce_news(res_id = res_id, url=url, bottom_tag=bottom_tag, title_cut=title_cut, date_cut=date_cut)

    

def run_parcer():
    for i in Resource.objects.all():
        print(i.id, i.resource_url, i.top_tag, i.bottom_tag, i.title_cut, i.date_cut)
        parce_new_from_resource(res_id = i.id, main_url=i.resource_url, top_tag=i.top_tag, bottom_tag=i.bottom_tag, title_cut=i.title_cut, date_cut=i.date_cut)