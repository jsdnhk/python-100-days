"""
不使用多線程的情況 - 模擬多個下載任務

Version: 0.1
Author: 駱昊
Date: 2018-03-20
"""

from random import randint
from time import time, sleep


def download_task(filename):
    print('開始下載%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('下載完成! 耗費了%d秒' % time_to_download)


def main():
    start = time()
    download_task('Python從入門到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('總共耗費了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
