import urllib.request
from bs4 import BeautifulSoup
from time import sleep

#http://www.csc.edu.cn/Laihua/programsearch.aspx?PageNo=3375

f = open('D:/workplace/liuxue/output_zhuanye_en.txt','w',errors='ignore')
f.write('院校名称\t')
f.write('专业\t')
f.write('学历层次\t')
f.write('学制\t')
f.write('授课语言\t')
f.write('学费（元）\t')
f.write('入学时间\t')
f.write('申请截止时间\n')
f.flush
count = 0
#3375
for i in range(3375):
    url = 'http://www.csc.edu.cn/Laihua/programsearchen.aspx?PageNo='+str(i+1)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
    big_node = soup.find('div',class_ = 'nei_box').find('ul')
    nodes = big_node.find_all('li')
    for node in nodes:
        det_nodes = node.find('div').find_all('div')
        f.write(det_nodes[0].get_text()+'\t')
        if '*' in det_nodes[1].get_text():
            f.write(det_nodes[1].get_text()[1:]+'\t')
        else:
            f.write(det_nodes[1].get_text()+'\t')
        f.write(det_nodes[2].get_text()+'\t')
        f.write(det_nodes[3].get_text()+'\t')
        f.write(det_nodes[4].get_text()+'\t')
        f.write(det_nodes[5].get_text()+'\t')
        f.write(det_nodes[6].get_text()+'\t')
        f.write(det_nodes[7].get_text()+'\n')
        f.flush
        count = count + 1
        print ('craw '+str(count)+' !')
f.close()
    
