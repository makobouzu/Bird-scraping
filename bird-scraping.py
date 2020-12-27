# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import time
import os

if __name__ == '__main__':
    url_ = "https://www.xeno-canto.org/explore?dir=0&order=xc&pg="
    page_num = 1000
    for page in range(page_num):
        page += 1
        url = url_ + str(page)
        if not os.path.isdir("page" + str(page)):
            os.mkdir("page" + str(page))
        response = requests.get(url).content
        soup = BeautifulSoup(response, "html.parser")
        a_tags = soup.select('a[download]')
        for a in a_tags:
            base_url = "https://www.xeno-canto.org"
            path = a.get('href')
            abs_path = base_url + path
            wav_file_name = a.get('download')
            urllib.request.urlretrieve(abs_path, "page" + str(page) + "/" + wav_file_name)
            print(abs_path,'is downloaded')
            time.sleep(5)
