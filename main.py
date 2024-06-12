import requests
import config
import rand
import gaogov
from util import get_request_data, write_to_csv
import os
urls = [
    {
        'url': 'https://www.gao.gov/reports-testimonies',
        'base_url': 'https://www.gao.gov',
        'file_name': os.path.join('gaogov', 'gaogov.xlsx'),
        'title': ['Released Time', 'header', 'subheading','summary'],
        'name': 'gaogov'
    },
    {
        'url': 'https://www.rand.org/pubs.html',
        'base_url': 'https://www.rand.org',
        'file_name': os.path.join('rand', 'rand.xlsx'),
        'title': ['title', 'summary'],
        'name': 'rand'
    },
]


if __name__ == '__main__':
    for url in urls:
        res = get_request_data(url['url'])
        if url['name'] == 'gaogov':
            datas= gaogov.process_data(res, url)
        else:
            datas= rand.process_data(res, url)
        write_to_csv(datas, url['title'], url['file_name'])
        print('Done!')