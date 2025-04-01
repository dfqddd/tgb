#!/usr/bin/env python3
# coding:utf-8
from getReply import GetReply
from getReplyDetail import GetReplyDetail
from config import USER_IDS, TIME_PARAM, PAGINATION, TIMEOUT, SLEEP_SECONDS, ENCODING

def main():
    for user_id in USER_IDS:
        # 获取回复链接并保存到文件
        replys = GetReply(
            user_id=user_id,
            time_param=TIME_PARAM,
            pagination=PAGINATION,
            timeout=TIMEOUT,
            sleep_seconds=SLEEP_SECONDS
        )
        # output_file_name = replys.run()
        output_file_name="8934153_data.txt"
        # 根据文件中的链接获取详情并保存
        detail_crawler = GetReplyDetail(file_path=output_file_name, timeout=TIMEOUT, sleep_seconds=SLEEP_SECONDS, user_id=user_id)
        results = detail_crawler.process_links()
        detail_crawler.save_results_to_file(results, output_filename=f'{user_id}_details.txt')



if __name__ == '__main__':
    main()
