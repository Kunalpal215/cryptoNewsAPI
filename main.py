from types import NoneType
from bs4.builder import TreeBuilderRegistry
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
def newsContent():
    contentToReturn={};
    contentToReturn['newsItems']=[];
    for i in range(1, 2):
        url = f"https://www.ndtv.com/business/cryptocurrency/news/page-{i}";
        cont = requests.get(url);
        soup = BeautifulSoup(cont.text, 'lxml');
        newsItems = soup.find_all('div', class_="news_Itm");
        for eachItem in newsItems:
            itemToReturn = {};
            newsImage = eachItem.find('img');
            newsHeading = eachItem.find('h2');
            newsSource = eachItem.find(class_='posted-by');
            newsContent = eachItem.find('p', class_="newsCont");
            if(type(newsImage)!=NoneType): itemToReturn['imageURL'] = newsImage['src'];
            if(type(newsHeading)!=NoneType): itemToReturn['heading'] = newsHeading.text;
            if(type(newsSource)!=NoneType): itemToReturn['source'] = newsSource.text.strip();
            if(type(newsContent)!=NoneType): itemToReturn['description'] = newsContent.text;
            if(bool(itemToReturn)!=NoneType): contentToReturn['newsItems'].append(itemToReturn);
    return contentToReturn;
app = FastAPI()
@app.get('/')
def home():
    newsPage = newsContent()
    return newsPage;
