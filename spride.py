import requests
import re
import time
import os


'''请求网页'''
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}
# 告诉服务器自己的身份

def Spider(mainUrl):
  response = requests.get(mainUrl, headers=headers)
  html = response.text

  '''解析网页'''

  dir_name = re.findall('<link rel="alternate".*?href="(.*?)">', html)[-1].split('/')[-1]
  if not os.path.exists(dir_name):
    os.mkdir(dir_name)

  urls = re.findall('<img src="(.*?)" alt=".*?">', html)
  urls = [url for url in urls if url[:5] == 'https']

  '''保存图片'''
  for url in urls:
    '''获取图片的名字'''
    time.sleep(0.5)
    file_name = url.split('/')[-1].split('?')[0]
    print(file_name)
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
      f.write(response.content)
      pass
    pass
  pass

def Go():
  response = requests.get('https://www.zhenai.com/zhenghun/', headers=headers)
  html = response.text
  citys = re.findall('<a target="_blank" href="(.*?)" data-v-f53df81a>', html)
  for city in citys:
    if '\"' in city:
      continue
      pass
    if city.split('/')[-1] == 'zhenghun':
      continue
      pass
    Spider(city)
  pass


Go()


'''
学完基础进阶之后 爬虫
web
数据分析（人工智能）
很多工作都需要爬虫
'''
# Spider('https://www.zhenai.com/zhenghun/aba')
# Spider('https://www.zhenai.com/zhenghun/akesu')
# Spider('https://www.zhenai.com/zhenghun/alashanmeng')
# Spider('https://www.zhenai.com/zhenghun/aletai')
# Spider('https://www.zhenai.com/zhenghun/anhui')
# Spider('https://www.zhenai.com/zhenghun/ankang')
# Spider('https://www.zhenai.com/zhenghun/anqing')










