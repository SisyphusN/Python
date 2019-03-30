# -*- coding:UTF-8 -*-
import requests, json
import urllib.request

class get_photos(object):
    
    def __init__(self):
        self.urlimg = []
        self.path = 'https://m.weibo.cn/api/container/getIndex?uid=6455785468&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%89%87%E5%AF%84%E5%87%89%E5%A4%AA&type=uid&value=6455785468&containerid=1076036455785468&page=yyyyy'
    
    """
    Function: get urls of photos
    Parameters:
        None
    Returns:
        None
    """
    def get_ids(self):
        for page in range(2, 7):
            target = self.path.replace("yyyyy", str(page + 1))
            req = requests.get(url = target)
            html = json.loads(req.text)
            
            for item in html['data']['cards']['card_type' == 9]['mblog']['pics']:
                self.urlimg.append(item['large']['url'])
            tempurl = html['data']['cards']['card_type' == 9]['mblog']['original_pic']
            self.urlimg.append(tempurl)
    
    """
    Function: Download images
    Parameters:
        None
    Returns:
        None
    """
    def download(self):
        count = 0
        for item in self.urlimg:
            response = urllib.request.urlopen(item)
            cat_img = response.read()
            count = count + 1
            with open('%s.jpg' %str(count), 'wb') as f:
                f.write(cat_img)

if __name__ == '__main__':
        gp = get_photos()
        print('获取图片中:')
        gp.get_ids()
        print('图片下载中:')
        gp.download()