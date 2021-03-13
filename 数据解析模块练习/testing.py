import requests

url = 'https://pic.netbian.com/4kmeinv/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.3'}
res = requests.get(url, headers=headers, verify=False)
print(res.content.decode('gbk'))