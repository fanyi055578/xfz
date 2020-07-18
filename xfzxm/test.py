import requests
import  re

#   古诗文网爬虫
# url = 'https://www.gushiwen.org/'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36',
#     'Referer':'https://m.gushiwen.org/default_1.aspx'
# }
# a=requests.get(url,headers=headers)
#
#
# text =a.content.decode('utf-8')
#
# poems = re.findall('<div class="contson".*?>(.*?)</div>',text,re.DOTALL)
# name = re.findall('<a .*?><b>(.*?)</b></a><',text,re.DOTALL)
# denasty = re.findall('<p class="source"><a href=.*?>(.*?)</a>',text,re.DOTALL)
# author = re.findall('<p class="source">.*?</span>.*?[>](.*?)</a>', text, re.DOTALL)
#
# pt=[]
# for i in poems:
#     pe = re.sub('<br />', ' ', i).strip()
#     pt.append(pe)
#
# t = []
#
# for i in range(10):
#     poem = {
#         "name": name[i],
#         "author":author[i],
#         "denasty":denasty[i],
#         "poem":pt[i]
#     }
#     t.append(poem)
#
# print(t)
#
# #拉钩网爬虫
# url = 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=pyt'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36',
#     'Referer':'https://m.gushiwen.org/default_1.aspx'
# }
#
# resps = requests.get(url,headers=headers)
# resp = resps.content.decode('utf-8')
#
# name = re.findall('<li class="r_search"><a .*?>(.*?)</a>',resp,re.DOTALL)
# print(name)
# # reward =
# need = re.findall('<a rel="nofollow" href="javascript:;" class="active">(.*?)</a>',resp,re.DOTALL)
# print(need)
# # company =
# city = re.findall('<a .*? class="more-city-name">(.*?)</a>',resp,re.DOTALL)
# print(city)


#
# params = {
#     'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36',
#     'Refere': 'https://www.dytt8.net/css/index.css'
# }
#
#
#
#
# def paramss(url):
#     resps = requests.get(url,params=params )
#     text = resps.content.decode('GBK')
#     name = re.findall('<div class="title_all"><h1>.*?>(.*?)</font>',text,re.DOTALL)
#     main_block = re.findall('<p style="PADDING-BOTTOM: .*? PADDING-TOP: 0px">(.*?)</p>',text,re.DOTALL)
#     names.append(name)
#     blocks.append(main_block)
#
# def get_url(main_url):
#     resp = requests.get(main_url, params=params)
#     response = resp.content.decode('GBK')
#     urls = re.findall('<b>.*?<a href="(.*?)" class="ulink">.*?</a>.*?</b>', response, re.DOTALL)
#     x = 'https://www.dytt8.net'
#     y = []
#
#
# if __name__ == '__main__':
#     main_url = 'https://www.dytt8.net/html/tv/hytv/list_71_1.html'
#     resp = requests.get(main_url, params=params)
#     response = resp.content.decode('GBK')
#     urls = re.findall('<b>.*?<a href="(.*?)" class="ulink">.*?</a>.*?</b>', response, re.DOTALL)
#     x = 'https://www.dytt8.net'
#     y = []
#     for i in urls:
#         u = x + i
#         y.append(u)
#     names =[]
#     blocks = []
#     for uls in y:
#         paramss(uls)
#
#     print(names)
#     print(blocks)
#
#     for j in range(10):
#         m_url = 'https://www.dytt8.net/html/tv/hytv/list_71_'+str(j)+'.html'
#


import time, os
from socket import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Basepath = os.path.join(BASE_DIR,'')
filePath = Basepath
print(filePath)

