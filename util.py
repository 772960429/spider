import requests
import config
import os
import writeFileToExcel
def get_request_data(url):
    return requests.get(url=url, headers=config.get_header(), proxies=config.proxies).text

def download_pdf(url, file_name, file_path):
    # 发送GET请求  
    response = requests.get(url=url, headers=config.get_header(), proxies=config.proxies)
    # 将PDF文件内容写入到本地文件中 
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def write_to_csv(datas, title, file_name):
    start = writeFileToExcel.Openpyxl_Excel()
    start.add_data(file_name, title, datas)