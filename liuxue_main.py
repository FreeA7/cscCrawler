#liuxue_main
import liuxue_spider
import liuxue_outputer
import urllib.request
from bs4 import BeautifulSoup

class LiuxueMain(object):
    def __init__(self):
        self.spider = liuxue_spider.LiuxueSpider
        self.outputer = liuxue_outputer.LiuxueOutputer

    def craw(self,root_url):
        fir_html = urllib.request.urlopen(root_url)
        fir_soup = BeautifulSoup(fir_html,'html.parser',from_encoding = 'utf-8')
        nodes = fir_soup.find_all('div',class_ = 'q_list')
        count = 0
        f = self.outputer.open()
        for node in nodes:
            urls = []
            url_nodes = node.find('ul').find_all('li')
            for url_node in url_nodes:
                urls.append(url_node.find('a')['href'])
            for url in urls:
                #try:
                    data = {}
                    data = self.spider.spider_html(url)
                    data['shengfen'] = node.find('div').find('strong').get_text()
                    self.outputer.collect(f,data)
                    count = count + 1
                    #print (data)
                    print ('craw '+data['school_name']+data['key']+' succeed , craw took '+str(count)+' altogether !')
                #except:
                    #print ('craw failed!')
        self.outputer.close(f)

if __name__ == "__main__":
        root_url = "http://www.csc.edu.cn/Laihua/universityen.aspx"
        obj_spider = LiuxueMain()
        obj_spider.craw(root_url)
                
            
        
