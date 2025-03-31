import time
import json
import requests
from bs4 import BeautifulSoup
from config import *

class GetReply:
    def __init__(self, user_id, **kwargs):
        self.base_url_template = BASE_URL_TEMPLATE
        self.headers = HEADERS
        self.cookies = COOKIES  # 添加 cookies 属性
        self.user_id = user_id
        self.time_param = kwargs.get('time_param', TIME_PARAM)
        self.pagination = kwargs.get('pagination', PAGINATION)
        self.timeout = kwargs.get('timeout', TIMEOUT)
        self.sleep_seconds = kwargs.get('sleep_seconds', SLEEP_SECONDS)
        self.output_file_prefix = f"{user_id}_data"  # 正确引用 user_id
        self.encoding = ENCODING
        self.data = []

    def build_url(self, page_number):
        return self.base_url_template.format(time=self.time_param, user_id=self.user_id, page=page_number)

    def fetch_page(self, page_number):
        url = self.build_url(page_number)
        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=self.timeout)  
            response.raise_for_status()
            return response.text  
        except requests.exceptions.RequestException as e:
            print(f"请求失败 (页码{page_number}): {str(e)}")
            return None

    def crawl_all_pages(self):
        for page in range(self.pagination["start_page"], self.pagination["end_page"] + 1):
            print(f"正在抓取页码 {page} ({self.user_id})")
            page_data = self.fetch_page(page)
            if page_data:
                self.data.append(page_data)
            time.sleep(self.sleep_seconds)
        return self.data

    def extract_links_from_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        links = []
        for link in soup.find_all('a', class_='blogReply-subinfo left'):
            href_value = link['href']
            print(href_value)
            links.append("https://www.tgb.cn/" + href_value)
        return links

    def save_to_file(self):
        if not self.data:
            print("没有数据需要保存")
            return

        filtered_data = []
        for page_data in self.data:
            links = self.extract_links_from_html(page_data)
            filtered_data.extend(links)

        output_file_name = f"{self.output_file_prefix}.txt"
        try:
            with open(output_file_name, 'w', encoding=self.encoding) as f:
                f.write('\n'.join(filtered_data))
            print(f"数据已保存至 {output_file_name}")
        except Exception as e:
            print(f"保存文件失败: {str(e)}")

        return output_file_name

    def run(self):
        self.crawl_all_pages()
        return self.save_to_file()
