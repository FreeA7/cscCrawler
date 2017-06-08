#liuxue_spider
import urllib.request
from bs4 import BeautifulSoup
import re
import os

class LiuxueSpider(object):
    def spider_html(url):
        school_fir_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url)
        fir_soup = BeautifulSoup(school_fir_html,'html.parser',from_encoding = 'utf-8')
        data = {}
        data['school_name'] = fir_soup.find('p',class_ = 'daohang_p').get_text()[26:]
        node = fir_soup.find('div',class_ = 'yx_jxj font_01')
        det_text = node.get_text()
        #print (det_text)

        data['city'] = re.search(r'City：(.*)', det_text).group(1)
        data['pro_num'] = re.search(r'Degree Programs：(.*)', det_text).group(1)
        data['china_num'] = re.search(r'Number of Students：(.*)', det_text).group(1)
        data['fore_num'] = re.search(r'International Students：(.*)', det_text).group(1)
        data['net'] = re.search(r'Website：(.*)', det_text).group(1)

        a_nodes = fir_soup.find_all('a')
        for a_node in a_nodes:
            if a_node.get_text()[:5]=='Office Website':
                data['fore_net'] = a_node.get_text()[10:]
                break
            
        url = url.replace('detail','about')
        school_about_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url)
        about_soup = BeautifulSoup(school_about_html,'html.parser',from_encoding = 'utf-8')
        jianjie_nodes = about_soup.find('div',class_ = 'zhusu_box').find_all('p')
        jianjie = ''
        for jianjie_node in jianjie_nodes:
            jianjie = jianjie + jianjie_node.get_text()
        p_p_p = re.compile('[\n\r\t]+')
        data['about'] = re.sub(p_p_p,'',jianjie)

        url = url.replace('about','news')
        school_news_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url)
        news_soup = BeautifulSoup(school_news_html,'html.parser',from_encoding = 'utf-8')
    
        kecheng_nodes = news_soup.find('div',class_ = 'nei_box min-he_01').find_all('div')

        no = '无记录'
        record_count = kecheng_nodes[0].find_all('span')[0].get_text()
        data['record_count'] = record_count
        if int(record_count) <= 10:
            nodesdetail = news_soup.find_all('div',{'id':'gonggao_list'})
        if int(record_count) > 10:
            nodesdetail = news_soup.find_all('div',{'id':'gonggao_list'})
            school_news_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url+'&PageNo=2')
            news_soup = BeautifulSoup(school_news_html,'html.parser',from_encoding = 'utf-8')
            kecheng_nodes = news_soup.find('div',class_ = 'nei_box min-he_01').find_all('div')
            fin_nodes = news_soup.find_all('div',{'id':'gonggao_list'})
            for fin_node in fin_nodes:
                nodesdetail.append(fin_node)
        if int(record_count) > 20:
            record_count = 20
                
        for i in range(int(record_count)):
            data['record'+str(i+1)] = re.sub(p_p_p,'',nodesdetail[i].get_text())
            detail_url = nodesdetail[i].find('a')['href']
            detail_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+detail_url)
            news_soup = BeautifulSoup(detail_html,'html.parser',from_encoding = 'utf-8')
            detail_nodes = news_soup.find('div',class_ = 'nei_sy1').find_all('p')
            detail = ''
            for detail_node in detail_nodes:
                detail = detail + detail_node.get_text()
            data['record'+str(i+1)+'detail'] = re.sub(p_p_p,'',detail)
        for i in range(int(record_count),20):
            data['record'+str(i+1)] = no
            data['record'+str(i+1)+'detail'] = no

        url = url.replace('news','Accommodation')
        zhusu_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url)
        zhusu_soup = BeautifulSoup(zhusu_html,'html.parser',from_encoding = 'utf-8')
        zhusu_nodes = zhusu_soup.find_all('div',class_ = 'zhusu_box')[0].find_all('tr')
        zhusu_pic = zhusu_soup.find_all('div',class_ = 'zhusu_box')[1]
        zhusu_count = -1
        for zhusu_node in zhusu_nodes:
            zhusu_count = zhusu_count + 1
        data['zhusu_count'] = zhusu_count
        for i in range(int(zhusu_count)):
            data['fjlx'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[0].get_text())
            data['zsf'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[1].get_text())
            data['wsj'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[2].get_text())
            data['ys'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[3].get_text())
            data['kd'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[4].get_text())
            data['gddh'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[5].get_text())
            data['kt'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[6].get_text())
            data['qt'+str(i+1)] = re.sub(p_p_p,'',zhusu_nodes[i+1].find_all('td')[7].get_text())
        for i in range(int(zhusu_count),8):
            data['fjlx'+str(i+1)] = no 
            data['zsf'+str(i+1)] = no 
            data['wsj'+str(i+1)] = no 
            data['ys'+str(i+1)] = no 
            data['kd'+str(i+1)] = no 
            data['gddh'+str(i+1)] = no 
            data['kt'+str(i+1)] = no 
            data['qt'+str(i+1)] = no

        formart = '0123456789'
        q=''
        for c in url:
            if c in formart:
                q = q + c
        data['key'] = q

        zhusu_pictures = zhusu_pic.find_all('div',class_ = 'strip_of_thumbnails')
        pic_count = 0
        picture_nodes = []
        for zhusu_picture in zhusu_pictures:
            pic_nodes = zhusu_picture.find_all('img')
            for pic_node in pic_nodes:
                picture_nodes.append(pic_node)
                pic_count = pic_count + 1
        picture_nodes = picture_nodes[1:]
        data['pic_count'] = pic_count
        srcs = []
        for picture_node in picture_nodes:
            srcs.append(re.sub(p_p_p,'%20',picture_node['src'][:-7]+'400.jpg'))
        try:
            os.mkdir(r'D:/workplace/liuxue/'+data['key']+data['school_name'])
        except:
            pass
        
        for i in range(data['pic_count']-1):
            try:
                pic_url = 'http://www.csc.edu.cn/Laihua/'+srcs[i]
                pic = urllib.request.urlopen(pic_url)
                pic_data = pic.read()
                filename = 'D:/workplace/liuxue/'+data['key']+data['school_name']+'/'+data['school_name']+str(i+1)+'.jpg'
                f = open(filename,'wb')
                f.write(pic_data)
                f.close()
            except:
                pass

        url = url.replace('Accommodation','contectus')
        lianxi_html = urllib.request.urlopen('http://www.csc.edu.cn/Laihua/'+url)
        lianxi_soup = BeautifulSoup(lianxi_html,'html.parser',from_encoding = 'utf-8')
        lianxi_node = lianxi_soup.find('div',class_ = 'zhusu_box')
        cont = lianxi_node.get_text()
        try:
            data['man'] = re.search(r'联系人：(.*)', cont).group(1)
        except:
            data['man'] = no
        try:
            data['phone'] = re.search(r'Tel:(.*)', cont).group(1)
        except:
            data['phone'] = no
        try:
            data['email'] = re.search(r'Email:(.*)', cont).group(1)
        except:
            data['email'] = no
        try:
            data['lianxiwangzhi'] = re.search(r'Website:(.*)', cont).group(1)
        except:
            data['lianxiwangzhi'] = no
        try:
            data['youbian'] = re.search(r'邮编：(.*)', cont).group(1)
        except:
            data['youbian'] = no
        try:
            data['lianxiadress'] = re.sub(p_p_p,'',re.search(r'地址：(.*)', cont).group(1))
        except:
            data['lianxiadress'] = no

        return data        
        
        
        
            
            

        

        
            
        

        

        

        

        

        

        
        
