import urllib.request
import re
from bs4 import BeautifulSoup


#url = http://www.csc.edu.cn/Laihua/scholarshiplist.aspx?cid=94&PageNo=1

url = 'http://www.csc.edu.cn/laihua/scholarshiplisten.aspx?cid=106'

name = []
urls = []
count = 0
p_p_p = re.compile('\s+')
for i in range(13):
    url_now = url + '&PageNo=' + str(i+1)
    html = urllib.request.urlopen(url_now)
    soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
    nodes = soup.find_all('div',class_ = 'g_nr_left')
    for node in nodes:
        name.append(node.get_text())
        urls.append(re.sub(p_p_p,'%20',node.find('a')['href']))
        count = count + 1

for i in range(count):
    filename = re.sub(r'[\/]','',name[i])
    f = open('D:/workplace/liuxue/奖学金en/University Scholarships+'+filename+'.txt','w',errors='ignore')
    html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+urls[i])
    soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
    cont = soup.find('div',class_ = 'right_bass').get_text()
    f.write(cont)
    f.close

