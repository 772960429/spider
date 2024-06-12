from lxml import etree
import os
from util import download_pdf

def process_data(res, url_info):
    release_date = ''
    datas = []
    tree=etree.HTML(res)
    content_container=tree.xpath('//*[@id="paragraph-8921"]/div/div/div/div')[0]
    i = 0
    for child in content_container.iter('h3', 'div'):
        if child.tag == 'h3':
            release_date = child.get('id')
        if child.tag == 'div':
            # 用xpath查找元素
            if (child.get('class') == 'gao-search-result'):
                per_page_total = child.xpath('//div/div/strong[1]')[0].text
            if (child.get('class') == 'views-row'):
                header_href = child.xpath('.//h4[@class="c-search-result__header"]/a')[0].get('href')
                download_pdf_url = 'https://www.gao.gov{}.pdf'.format(header_href.replace('products', 'assets'))
                header = child.xpath('.//h4[@class="c-search-result__header"]/a')[0].text
                download_pdf(download_pdf_url, os.path.join(url_info['name'], header.replace(':', '_') + '.pdf'), url_info['name'])
                subheading_part_1 = child.xpath('.//span[@class="d-block text-small"]')[0].text.replace('\n', '')
                subheading_part_2_list = child.xpath('.//span[@class="text-small"]/child::node()')
                subheading_part_2 = ''
                for item in subheading_part_2_list:
                    try:
                        subheading_part_2 += item.text.replace('\n', '')
                        subheading_part_2 += item.text
                    except AttributeError:
                        subheading_part_2 += item.replace('\n', '')
                subheading = subheading_part_1 + '\n' + subheading_part_2
                summary = child.xpath('.//div[@class="c-search-result__summary"]')[0].text.replace('\n', '')
                datas.append([release_date, header, subheading, summary])
    return datas
