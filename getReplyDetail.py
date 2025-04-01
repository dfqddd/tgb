import time
import json
import requests
from bs4 import BeautifulSoup
from config import *
import os
class GetReplyDetail:
    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self.headers = HEADERS
        self.cookies = COOKIES  # 添加 cookies 属性
        self.timeout = kwargs.get('timeout', TIMEOUT)
        self.sleep_seconds = kwargs.get('sleep_seconds', SLEEP_SECONDS)
        self.user_id = kwargs.get('user_id')

    def read_links_from_file(self):
        """从文件中读取链接"""
        with open(self.file_path, 'r') as f:
            links = [line.strip() for line in f.readlines()]
        return links

    def fetch_page(self, url):
        """发送 GET 请求并返回响应内容"""
        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies, timeout=self.timeout)  
            response.raise_for_status()
            return response.text  
        except requests.exceptions.RequestException as e:
            print(f"请求失败 ({url}): {str(e)}")
            return None

    def format_html_content(self, html_string):
        """
        处理 HTML 字符串，提取文字内容及其格式，并保留结尾的图片链接（如果有的话）

        :param html_string: 包含 HTML 内容的字符串
        :return: 格式化后的内容字符串
        """
        soup = BeautifulSoup(html_string, 'html.parser')
        
        # 提取所有文本内容
        text_parts = []
        for element in soup.stripped_strings:
            text_parts.append(element)

        # 提取最后一个 <img> 标签的 src 或 data-original 属性
        img_tag = soup.find('img')
        img_url = ''
        if img_tag and ('src' in img_tag.attrs or 'data-original' in img_tag.attrs):
            img_url = img_tag['data-original'] if 'data-original' in img_tag.attrs else img_tag['src']

        formatted_text = '\n'.join(text_parts)
        if img_url:
            formatted_text += '\n\n' + img_url

        return formatted_text

    def parse_html_and_extract_content(self, html_content, identifier):
        """解析 HTML 并提取 gioMsg_R_{identifier} 内容"""
        soup = BeautifulSoup(html_content, 'html.parser')
        target_div = soup.find(id=f'gioMsg_R_{identifier}')
        print(soup)
        if target_div:
            subject_text = target_div.attrs.get('subject')
            
            # 处理 subject_text 内容
            formatted_subject_text = self.format_html_content(subject_text)
            
            return formatted_subject_text
        
        else:
            print(f"未找到标识符为 '{identifier}' 的内容.")
            return None

    def process_links(self):
        """处理所有链接，提取所需内容"""
        links = self.read_links_from_file()
        results = []
        batch_size = 5
        
        for idx, link in enumerate(links):
            identifier = link.split('#')[-1]
            response_content = self.fetch_page(link)

            if response_content:
                extracted_content = self.parse_html_and_extract_content(response_content, identifier)
                print(extracted_content)
                if extracted_content:
                    results.append(extracted_content)

            time.sleep(self.sleep_seconds)

            # 每处理完一批次的链接就写入文件
            if len(results) >= batch_size or idx == len(links) - 1:
                self.save_results_to_file(results, output_filename=f'{self.user_id}_details.txt')
                results.clear()

    def save_results_to_file(self, results, output_filename='results.txt'):
        """将结果追加到文件末尾"""
        output_filename = output_filename.replace('.txt', '') + '_' + str(self.user_id) + '.txt'
        mode = 'a+' if os.path.exists(output_filename) else 'w'
        with open(output_filename, mode, encoding=ENCODING) as f:
            for result in results:
                f.write(result + '\n')

if __name__ == '__main__':
    pass