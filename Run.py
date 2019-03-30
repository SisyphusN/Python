#Run code in this file
import CrawlAttempt

if __name__ == '__main__':
        gp = get_photos()
        print('获取图片中:')
        gp.get_ids()
        print('图片下载中:')
        gp.download()