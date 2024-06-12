from lxml import etree
import os
import util


def process_data(res, url_info):
    base_url = url_info['base_url']
    datas = []
    tree=etree.HTML(res)
    content_container=tree.xpath('//*[@id="pubList-1591651637-results"]')[0]
    for child in content_container.iter('li'):
        title = child.xpath('.//h3[@class="title"]')[0].text
        desc = child.xpath('.//p[@class="desc"]')[0].text
        datas.append([title, desc])
        download_page_url=child.xpath('//*[@id="pubList-1591651637-results"]/li[1]/a')[0].get('href')
        download_page_data = util.get_request_data(base_url+download_page_url)
        download_page_tree=etree.HTML(download_page_data)
        try:
            download_file_href=download_page_tree.xpath('//span[@class="format-pdf"]/a')[0].get('href')
            file_name = os.path.join(url_info['name'], '{}.pdf'.format(title.replace(':', '_')))
            util.download_pdf(base_url+download_file_href, file_name, url_info['name'])
        except:
            print('pdf download fail, file is: ', title)
    return datas
