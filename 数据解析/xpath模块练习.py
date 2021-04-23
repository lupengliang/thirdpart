import os

import requests
from lxml import etree

# # ## 练习中文乱码解决和图片二进制
# dirName = './meinvLibs'
# if not os.path.exists(dirName):
#     os.mkdir(dirName)
# url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.3'}
# for page in range(1, 11):
#     if page == 1:
#         new_url = 'https://pic.netbian.com/4kmeinv/'
#     else:
#         new_url = format(url % page)
#     page_text = requests.get(new_url, headers=headers).text
#     tree = etree.HTML(page_text)
#     a_list = tree.xpath('//div[@clas="slist"]/ul/li/a')
#     for a in a_list:
#         img_src = 'http://pic.netbian.com' + a.xpath('./img/@src')[0]
#         img_name = a.xpath('./b/text()')[0]
#         img_name = img_name.encode('iso-8859-1').decode('gbk')
#         img_data = requests.get(img_src, headers=headers).content
#         imgPath = dirName + '/' + img_name + './jpg'
#         with open(imgPath, 'wb') as fp:
#             fp.write(img_data)

page_text = requests.get('https://www.baidu.com')
print(page_text.text)